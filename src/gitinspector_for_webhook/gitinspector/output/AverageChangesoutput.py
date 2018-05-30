from __future__ import print_function
from __future__ import unicode_literals
import json
import textwrap
from ..localization import N_
from .. import format, gravatar, terminal
from .outputable import Outputable

INFO_TEXT = N_("This is average lines for each authors. Repository's average lines for one commit is {0:.2f}.")
NO_COMMITED_FILES_TEXT = N_("No commited files with the specified extensions were found")

class AverageChangesOutput(Outputable):
    def __init__(self, changes):
        self.changes = changes
        Outputable.__init__(self)

    def output_html(self):
        authorinfo_list = self.changes.get_authorinfo_list()
        total_changes = 0.0
        changes_xml = "<div><div class=\"box\">"
        chart_data = ""
        total_commits = 0

        for i in authorinfo_list:
            total_changes += authorinfo_list.get(i).insertions
            total_changes += authorinfo_list.get(i).deletions
            total_commits += authorinfo_list.get(i).commits

        if authorinfo_list:
            total_line = total_changes / total_commits
            changes_xml += "<p>" + _(INFO_TEXT).format(total_line) + ".</p><div><table id=\"change_chart\" class=\"git\">"
            changes_xml += "<thead><tr> <th>{0}</th> <th>{1}</th> <th>{2}</th> <th>{3}</th>".format(_("Author"), _("Author's Average lines"), _("Percentage"), _("Evaluation"))
            changes_xml += "</tr></thead><tbody>"

            for i, entry in enumerate(sorted(authorinfo_list)):
                authorinfo = authorinfo_list.get(entry)
                average = 0 if total_changes == 0 else (authorinfo.insertions + authorinfo.deletions) / authorinfo.commits

                changes_xml += "<tr " + ("class=\"odd\">" if i % 2 == 1 else ">")

                if format.get_selected() == "html":
                    changes_xml += "<td><img src=\"{0}\"/>{1}</td>".format(gravatar.get_url(self.changes.get_latest_email_by_author(entry)),entry)
                else:
                    changes_xml += "<td>" + entry + "</td>"

                changes_xml += "<td>" + "{0:.2f}".format(average) + "</td>"
                changes_xml += "<td>" + "{0:.2f}".format(average/total_line) + "</td>"
                if (average/total_line) >= 1.0:
                    changes_xml += "<td colspan=\"{0}\" style=\"{1}\">".format(3,"color:blue") + "커밋당 line 변화가 평균보다 높습니다. 계속 유지하세요" + "</td>"
                else:
                    changes_xml += "<td colspan=\"{0}\" style=\"{1}\">".format(3,"color:red") + "커밋당 line 변화가 평균보다 낮습니다. 조금 더 수정 후에 커밋하는 것이 어떨까요?" + "</td>"
                changes_xml += "</tr>"

                chart_data += "{{label: {0}, data: {1}}}".format(json.dumps(entry), "{0:.2f}".format(average/total_line))

                if sorted(authorinfo_list)[-1] != entry:
                    chart_data += ", "

            changes_xml += ("<tfoot><tr> <td colspan=\"5\">&nbsp;</td> </tr></tfoot></tbody></table>")
            changes_xml += "<div class=\"chart\" id=\"average_chart\"></div></div>"
            changes_xml += "<script type=\"text/javascript\">"
            changes_xml += "    changes_plot = $.plot($(\"#average_chart\"), [{0}], {{".format(chart_data)
            changes_xml += "        series: {"
            changes_xml += "            pie: {"
            changes_xml += "                innerRadius: 0.4,"
            changes_xml += "                show: true,"
            changes_xml += "                combine: {"
            changes_xml += "                    threshold: 0.01,"
            changes_xml += "                    label: \"" + _("Minor Authors") + "\""
            changes_xml += "                }"
            changes_xml += "            }"
            changes_xml += "        }, grid: {"
            changes_xml += "            hoverable: true"
            changes_xml += "        }"
            changes_xml += "    });"
            changes_xml += "</script>"
        else:
            changes_xml += "<p>" + _(NO_COMMITED_FILES_TEXT) + ".</p>"

        changes_xml += "</div></div>"
        print(changes_xml)

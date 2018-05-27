from ..localization import N_
from .outputable import Outputable
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

INFO_TEXT = N_("Commit that has low line changes")
NO_INFO_TEXT = N_("Repository has no commit that has low line changes")

class LowLineChangesOutput(Outputable):
    def __init__(self, low_change):
        Outputable.__init__(self)
        self.low_change = low_change


    def output_html(self):
        changes_xml = "<div><div class=\"box\">"

        if self.low_change.commit_list:
            changes_xml += "<p>" + _(INFO_TEXT) + ".</p><div><table id=\"low_change\" class=\"git\">"
            changes_xml += "<thead><tr> <th>{0}</th> <th>{1}</th> <th>{2}</th> <th>{3}</th>".format(_("Commit hash"), _("Commit Msg"), _("Change"), _("Link"))
            changes_xml += "</tr></thead><tbody>"

            for key in self.low_change.commit_list:
                changes_xml += "<tr>"
                changes_xml += "<td>" + "{0}".format(key[0:7]) + "</td>"
                changes_xml += "<td>" + "{0}".format(key[8:]) + "</td>"
                changes_xml += "<td>" + "{0}".format(self.low_change.commit_list[key]) + "</td>"
                tmp_link = self.low_change.link + key[0:7]
                changes_xml += "<td><a href=\"{0}\" target=\"_blank\"> Click </a></td>".format(tmp_link)
                changes_xml += "</tr>"
        else:
            changes_xml += "<p>" + _(NO_INFO_TEXT) + ".</p>"
        changes_xml += "</div></div>"
        print(changes_xml)

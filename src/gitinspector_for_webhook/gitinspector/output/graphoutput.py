from ..localization import N_
from .outputable import Outputable

INFO_TEXT = N_("Graph that shows the activity score")

class graphoutput(Outputable):
    def __init__(self):
        Outputable.__init__(self)

    def output_html(self):
        changes_xml = "<div><div class=\"box\">"
        changes_xml += "<p>" + _(INFO_TEXT) + ".</p><div><table id=\"graph\" class=\"git\">"
        changes_xml += "<thead><tr> <th>{0}</th> <th>{1}</th> <th>{2}</th> <th>{3}</th>".format(_("TEST"), _("Commit Msg"), _("Change"), _("Link"))
        changes_xml += "</tr></thead><tbody>"
        changes_xml += "</div></div>"

        print(changes_xml)

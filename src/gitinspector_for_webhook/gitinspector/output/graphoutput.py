from ..localization import N_
from .outputable import Outputable

INFO_TEXT = N_("Graph that shows the activity score")

class graphoutput(Outputable):
    def __init__(self):
        Outputable.__init__(self)

    def output_html(self):

        f = open("gitinspector/output/framework/d3.v4.min.js", 'r')
        d3 = f.read()
        f.close()

        f = open("gitinspector/output/Monthgraph.js", 'r', encoding='UTF8')
        graph = f.read()
        f.close()

        changes_xml = "<div><div class=\"box\">" #추가
        changes_xml += "<style>"
        changes_xml += ".axis .domain {"
        changes_xml += "display: none;}"
        changes_xml += "</style>"
        changes_xml += "<p>Below graph is representing the score of each person, per month</p>"
        changes_xml += "<svg width=\"760\" height=\"300\"></svg>"
        changes_xml += "<script>" + d3 + "</script>"
        changes_xml += "<script>" + graph + "</script>"
        changes_xml += "</div></div>"

        print(changes_xml)

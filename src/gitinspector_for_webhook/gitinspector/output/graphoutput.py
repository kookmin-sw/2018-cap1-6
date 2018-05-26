from ..localization import N_
from .outputable import Outputable

INFO_TEXT = N_("Graph that shows the activity score")

class graphoutput(Outputable):
    def __init__(self):
        Outputable.__init__(self)

    def output_html(self):
        f = open("gitinspector/output/framework/d3.v3.min.js", 'r')
        d3 = f.read()
        f.close()
        f = open("gitinspector/output/framework/nvd3_181.js", 'r')
        nvd3 = f.read()
        f.close()
        f = open("gitinspector/output/framework/jquery321.js", 'r')
        jquery = f.read()
        f.close()
        #f = open("gitinspector/output/functions.js", 'r', encoding='UTF8')
        #function = f.read()
        #f.close()
        f = open("gitinspector/output/functiontest.js", 'r', encoding='UTF8')
        function = f.read()
        f.close()
        f = open("gitinspector/output/data.js", 'r')
        data = f.read()
        f.close()
        f = open("gitinspector/output/score.js", 'r')
        score = f.read()
        f.close()
        f = open("gitinspector/output/styles/nvd3_181.css", 'r')
        nvd3_css = f.read()
        f.close()
        f = open("gitinspector/output/styles/bootstrap337.css", 'r')
        bootstrap = f.read()
        f.close()
        f = open("gitinspector/output/chart.css", 'r')
        chart = f.read()
        f.close()

        changes_xml = "<html lang=\"en\" dir=\"ltr\">"
        changes_xml += "<head>"
        changes_xml += "<meta charset=\"utf-8\">"
        changes_xml += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        changes_xml += "<title></title>"

        changes_xml += "<script>" + d3 + "</script>"
        changes_xml += "<script>" + nvd3 + "</script>"
        changes_xml += "<script>" + jquery + "</script>"
        changes_xml += "<script>"+ function + "</script>"
        changes_xml += "<script>" + data + "</script>"
        changes_xml += "<script>" + score + "</script>"

        changes_xml += "<style>"+ nvd3_css + "</style>"
        #changes_xml += "<link rel=\"stylesheet\" href=\"gitinspector/output/styles/bootstrap337.css\">"
        changes_xml += "<style>"+ bootstrap + "</style>"
        changes_xml += "<style>"+ chart + "</style>"

        changes_xml += "</head>"
        changes_xml += "<body>"
        changes_xml += "<div><div class=\"box\">" #추가
        changes_xml += "<div class=\"container\">"
        changes_xml += "<div class=\"row\">"
        changes_xml += "<div class=\"col-sm-8\">"
        changes_xml += "<h2>NVD3 demo</h2>"
        changes_xml += "<button type=\"button\" class=\"btn btn-primary\" id=\"stdperday\">일 기준 활동점수</button>"
        changes_xml += "<button type=\"button\" class=\"btn btn-primary\" id=\"stdperweek\">주 기준 활동점수</button>"
        changes_xml += "<button type=\"button\" class=\"btn btn-primary\" id=\"stdpermonth\">월 기준 활동점수</button>"
        changes_xml += "</div>"
        changes_xml += "</div>"
        changes_xml += "<div class=\"row\">"
        changes_xml += "<div class=\"col-sm-8\">"
        changes_xml += "<div class=\"panel panel-primary\">"
        changes_xml += "<div class=\"panel-heading\">NVD3 Discrete Bar Chart</div>"
        changes_xml += "<div class=\"panel-body\">"
        changes_xml += "<div id=\"chart\" >"
        changes_xml += "<svg id=\"graph1\"></svg>"
        changes_xml += "<svg id=\"graph2\"></svg>"
        changes_xml += "<svg id=\"graph3\"></svg>"
        changes_xml += "<svg id=\"graph4\"></svg>"
        changes_xml += "</div>"
        changes_xml += "</div>"
        changes_xml += "</div>"
        changes_xml += "</div>"
        changes_xml += "</div>"
        changes_xml += "</div>"
        changes_xml += "</div></div>"
        changes_xml += "</body>"
        changes_xml += "</html>"



        print(changes_xml)

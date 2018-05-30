var drawChart = function(chartData, str){
    nv.addGraph(function() {
    var chart = nv.models.discreteBarChart()
      .x(function(d) { return d.label })
      .y(function(d) { return d.value })
      .staggerLabels(true)
      .tooltips(false)
      .showValues(true)

    d3.select('#chart ' + str )
      .datum(chartData) // data이름
      .transition().duration(500)
      .call(chart)
      ;

    nv.utils.windowResize(chart.update);

    return chart;
  });
};


$(function(){
  $("#stdperday").click(function(){
    console.log("draw chart");
    drawChart(Data, "#graph1");
    drawChart(Data, "#graph2");
    drawChart(Data, "#graph3");
    drawChart(Data, "#graph4");
  });
  $("#stdperweek").click(function(){
    console.log("draw chart");
    drawChart(chartData, "#graph1");
    drawChart(chartData, "#graph2");
    drawChart(Data, "#graph3");
    drawChart(Data, "#graph4");
  });
  $("#stdpermonth").click(function(){
    console.log("draw chart");
    drawChart(chartData, "#graph1");
    drawChart(chartData, "#graph2");
    drawChart(chartData, "#graph3");
    drawChart(chartData, "#graph4");
  });
});

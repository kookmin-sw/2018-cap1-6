var drawChart = function(){
    nv.addGraph(function() {
    var chart = nv.models.discreteBarChart()
      .x(function(d) { return d.label })
      .y(function(d) { return d.value })
      .staggerLabels(true)
      .tooltips(false)
      .showValues(true)

    d3.select('#chart svg')
      .datum(Data) // data이름
      .transition().duration(500)
      .call(chart)
      ;

    nv.utils.windowResize(chart.update);

    return chart;
  });
};

var drawChart2 = function(){
    nv.addGraph(function() {
    var chart2 = nv.models.discreteBarChart()
      .x(function(d) { return d.label })
      .y(function(d) { return d.value })
      .staggerLabels(true)
      .tooltips(false)
      .showValues(true)

    d3.select('#chart #graph2')
      .datum(chartData) // data이름
      .transition().duration(500)
      .call(chart2)
      ;

    nv.utils.windowResize(chart.update);

    return chart2;
  });
};

var drawChart3 = function(){
    nv.addGraph(function() {
    var chart3 = nv.models.discreteBarChart()
      .x(function(d) { return d.label })
      .y(function(d) { return d.value })
      .staggerLabels(true)
      .tooltips(false)
      .showValues(true)

    d3.select('#chart #graph3')
      .datum(chartData) // data이름
      .transition().duration(500)
      .call(chart3)
      ;

    nv.utils.windowResize(chart.update);

    return chart3;
  });
};

$(function(){
  $("#btnLoadChart").click(function(){
    console.log("draw chart");
    drawChart();
    drawChart2();
    drawChart3();
  });
});

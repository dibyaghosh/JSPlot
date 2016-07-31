from IPython.core.magic import (register_line_magic, register_cell_magic,
                                register_line_cell_magic)
from IPython.core.display import display, HTML
from subprocess import call
import time
import os

pythonFile = """
math = Math

def setup():
    return '%s'
def inputs():
    return [%s]

%s
"""
pid = 0

@register_cell_magic
def jsPlot(line, cell):
    global pid
    pid += 1
    mode,parameter = line[:line.find(" ")], line[line.find(" "):]
    print(mode)
    print(parameter)
    pF = pythonFile%(mode,parameter,cell)
    pF = pF.replace("plot","plot"+str(pid))
    pF = pF.replace("bar","bar"+str(pid))

    fileName = 'tmp%d'%pid
    f = open(fileName+'.py','w')
    f.write(pF)
    f.close()
    call(["transcrypt", fileName+".py",'--nomin'])
    js = open("__javascript__/"+fileName+".js").read()
    js = js.replace('enumerable: true', 'enumerable: true, configurable:true')
    os.remove(fileName+'.py')
    os.remove("__javascript__/"+fileName+".js")
    print(pid)
    return HTML(ht.replace("JSSOURCE",js).replace("PID",str(pid)))



ht = """
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
	<script>JSSOURCE</script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.js"></script>
	<script src="https://cdn.rawgit.com/novus/nvd3/master/build/nv.d3.min.js"></script>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.4/nv.d3.min.css">
	<link href='http://fonts.googleapis.com/css?family=Quantico' rel='stylesheet' type='text/css'>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/jstat/1.5.3/jstat.min.js"></script>
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  <script src="numjs.min.js"></script>

	<div class="container-fluid">
	<div id="chartPID" class="col-md-9">
	<svg  style="height:500px"></svg>
	</div>
	<div id="slidersPID" class="col-md-3">
  	</div>
	</div>
	<script>\

    var historicalBarChartPID = [
        
    { 
      "key" : "" , 
      "bar": true,
      "color": "#ccf",
      "values" : []}
    ];
    var chartPID;
    function sliderToHTML(name,min,max,step){
      var htmlZ = '<div class="slider"><label>'+name+'</label><input type = "range" min="'+min+'" max="'+max+'" step="'+step+'" onchange="'+name+'valuePID.value=value;updatePID();"/><output class="slider" id="'+name+'valuePID">'+(min+max)/2+'</output></div>';
      return htmlZ;
    }
    
    function addSlider(name,min,max,step){
      var html = sliderToHTML(name,min,max,step);
      var sLoc = $('#slidersPID');
      sLoc.html(sLoc.html()+html);
    }

    function addAllSliders(){
      sls = tmpPID.inputs();
      for(i = 0; i < sls.length; i++){
        inp = sls[i];
        addSlider(inp[0],inp[1],inp[2],inp[3]);
      }
    }
    var colors = ['#aec7e8', '#7b94b5', '#486192','#aec7e8', '#7b94b5', '#486192','#aec7e8', '#7b94b5', '#486192'];
    function addplotPID(a,b,bar){
        var c = a.map(function (e, i) {
        return [a[i], b[i]];
        });
        historicalBarChartPID.push( { 
      "key" : ""+historicalBarChartPID.length , 
      "color": colors[historicalBarChartPID.length],
      "values" : c,
      "bar":bar});
      chartn = d3.select('#chartPID svg');
    chartn.datum(historicalBarChartPID).transition().duration(500).call(chartPID);
    nv.utils.windowResize(chartPID.update); 
    }
    
    
    
    function plotPID(a,b){
        addplotPID(a,b,false);
    }
    
    function barPID(a,b){
        addplotPID(a,b,true);
    }
    
    function setTypePID(type){
        clearPID();
        if(type=='l'){
            nv.addGraph(function() {
            chartPID = nv.models.lineChart()
                .x(function(d) { return d[0] })
                .y(function(d) { return d[1] })
                //.staggerLabels(historicalBarChart[0].values.length > 8)
                .duration(250)
                ;
            d3.select('#chartPID svg')
                .datum(historicalBarChartPID)
                .call(chartPID);
            nv.utils.windowResize(chartPID.update);
            updatePID();
            return chartPID;
        });
        } else if (type == 'b'){
            nv.addGraph(function() {
            chartPID = nv.models.discreteBarChart()
                .x(function(d) { return d[0] })
                .y(function(d) { return d[1] })
                //.staggerLabels(historicalBarChart[0].values.length > 8)
                .duration(250)
                ;
            d3.select('#chartPID svg')
                .datum(historicalBarChartPID)
                .call(chartPID);
            nv.utils.windowResize(chartPID.update);
            updatePID();
            return chartPID;
        });
        }
        else {
        nv.addGraph(function() {
        chartPID = nv.models.linePlusBarChart()
            .x(function(d) { return d[0] })
            .y(function(d) { return d[1] })
            .duration(250)
            ;
        d3.select('#chartPID svg')
            .datum(historicalBarChartPID)
            .call(chartPID);
        nv.utils.windowResize(chartPID.update);
        updatePID();
        return chartPID;
    });
        }
    
    }
    addAllSliders();
    function updatePID() {
        historicalBarChartPID = [];
    	var values = $.map($("#slidersPID output"), function(x){return parseFloat(x.value);});
    	tmpPID.data.apply(this,values);
	};
    
    function clearPID() {
        d3.selectAll("#chartPID svg > *").remove();
    }
    setTypePID(tmpPID.setup());
</script>

"""
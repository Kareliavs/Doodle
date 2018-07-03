(function() {
var width = 400,
    height = 300;
    //padding = 1.5, // separation between same-color nodes
    //clusterPadding = 6, // separation between different-color nodes
    //maxRadius = 15;

//var n = 67, // total number of nodes
   // m = 3; // number of distinct clusters

var svg = d3.select("#chart")
	.append("svg")
	.attr("height", height)
	.attr("width", width)
	.append("g")
	.attr("transform", "translate(0,0)")

var radiusScale = d3.scaleSqrt().domain([1, 3114]).range([1, 50])



// the simulation is a collection of forces
// about where we want our circles to go
// and how we want them to interact
// STEP ONE: get them to the middle
// STEP TWO: don't have them collide!

var forceXSplit = d3.forceX(function(d){
		if(d.Sex === "male") {
			return (width * .30)
		} else {
			return (width * .70)
		}
	}).strength(0.15)

var forceXCombine = d3.forceX((width)/2).strength(0.1)

var forceCollide = d3.forceCollide(function(d){
		return radiusScale(d.Total_Words) + 1
	})


var simulation = d3.forceSimulation()
	.force("x", forceXCombine)
	.force("y", d3.forceY(height / 2).strength(0.09))
	.force("collide", forceCollide)	



  var tooltip = d3.select("body")
    .append("div")
    .style("position", "absolute")
    .style("z-index", "20")
    .style("visibility", "hidden")
    .style("color", "white")
    .style("padding", "8px")
    .style("background-color", "rgba(0, 0, 0, 0.75)")
    .style("border-radius", "6px")
    .style("font", "12px sans-serif")
    .text("");  


d3.queue()
	.defer(d3.csv, "data.csv")
	.await(ready)

function ready (error, datapoints) {

	var circles = svg.selectAll(".Character")
	.data(datapoints)
	.enter().append("circle")
	.attr("class", "Character")
	.attr("r", function(d){
		return radiusScale(d.Total_Words)
	})
	.style("fill", function(d) { 
		var returnColor;
		if (d.Sex === "male") { returnColor = "#355C7D";
		} else if (d.Sex === "female") {returnColor = "#F67280";}
		return returnColor;
	})
	.on("mouseover", function(d) {
              tooltip.html(d.Character + "<br><br> Words Spoken: " + d.Total_Words);
              tooltip.style("visibility", "visible");
      })
      .on("mousemove", function() {
          return tooltip.style("top", (d3.event.pageY-10)+"px").style("left",(d3.event.pageX+10)+"px");
      })
      .on("mouseout", function(){return tooltip.style("visibility", "hidden");});

	

/// Adding Toggle Switches	
	
	var atRight = true

	var rect = svg.append("rect")
            .attr("x", 10)
            .attr("y", 10)
            .attr("rx", 22)
            .attr("ry", 22)
            .style("fill", "lightgray")
            .attr("width", 64)
            .attr("height", 40)
            .on("click", function(){
				if(atRight === true){
				simulation
					.force("x", forceXSplit)
					.alphaTarget(0.2)
					.force("collide", forceCollide)
				setAtRight(!atRight)
				} else {
				simulation
					.force("x", forceXCombine)
					.alphaTarget(0.07)	
				setAtRight(!atRight)
				}	
			});

    var circle = svg.append("circle")
            .attr("cx", 30)
            .attr("cy", 30)
            .attr("r", 16)
            .style("fill", "white")
            .on("click", function(){
				if(atRight === true){
				simulation 
					.restart()
					.force("x", forceXSplit)
					.alphaTarget(0.2)
					.force("collide", forceCollide)
				setAtRight(!atRight)
				} else {
				simulation
					.restart()
					.force("x", forceXCombine)
					.alphaTarget(0.2)	
				setAtRight(!atRight)
				}	
			});

    var setAtRight = function(newValue) {
        atRight = newValue;
        circle.transition().duration(250)
                .attr("cx", (atRight? (30) : (54)))
                .style("fill", "white");
        rect.transition().duration(250)
        		.style("fill", atRight? "lightgray" : "#C06C84");  
    };


    var res = {
        'getValue': function() { return atRight; },
        'setValue': setAtRight,
        'remove': function() { circle.remove(); }
    };

   
	simulation.nodes(datapoints)
		.on('tick', ticked)


	function ticked() {
		circles
			.attr("cx", function(d) {
				return d.x
			})
			.attr("cy", function(d) {
				return d.y
			})
	}	
}		


})();
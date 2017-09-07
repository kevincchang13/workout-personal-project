// var opts = ['A','B','C','D','F'];
// $.get('{{url_for("exercises.all")}}')
var opts = [];




function go(){
	addSlots($("#slots_a .wrapper"));
	moveSlots($("#slots_a .wrapper"));
	addSlots($("#slots_b .wrapper"));
	moveSlots($("#slots_b .wrapper"));
	addSlots($("#slots_c .wrapper"));
	moveSlots($("#slots_c .wrapper"));
}

$(document).ready(
function(){
	addSlots($("#slots_a .wrapper"));
	addSlots($("#slots_b .wrapper"));
	addSlots($("#slots_c .wrapper"));

}
);


function addSlots(jqo){
	for(var i = 0; i < 15; i++){
		var ctr = Math.floor(Math.random()*opts.length);
		jqo.append("<div class='slot'>"+opts[ctr]+"</div>");


	}
}

function moveSlots(jqo){
		var time = 6500;
		time += Math.round(Math.random()*1000);
	jqo.stop(true,true);

		var marginTop = parseInt(jqo.css("margin-top"), 10)

		marginTop -= (7 * 100)

	jqo.animate(
		{"margin-top":marginTop+"px"},
		{'duration' : time, 'easing' : "easeOutElastic"});

}

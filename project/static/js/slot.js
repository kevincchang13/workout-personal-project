document.addEventListener('DOMContentLoaded', function() {
	var getData = $.get('/exercises/all', function(data){

		addSlots($("#slots_a .wrapper"));
		addSlots($("#slots_b .wrapper"));
		addSlots($("#slots_c .wrapper"));

		function addSlots(slot){
			for(var i = 0; i < data.length; i++){
				var random = Math.floor(Math.random()*data.length);
				slot.append("<div class='slot'>"+data[random]+"</div>");

			}
		}

		$(".go").on('click', go)

		function go(){
			addSlots($("#slots_a .wrapper"));
			moveSlots($("#slots_a .wrapper"));
			addSlots($("#slots_b .wrapper"));
			moveSlots($("#slots_b .wrapper"));
			addSlots($("#slots_c .wrapper"));
			moveSlots($("#slots_c .wrapper"));
		}


		function moveSlots(slot){
			var time = 6500;
			time += Math.round(Math.random()*1000);
			slot.stop(true,true);

			var marginTop = parseInt(slot.css("margin-top"), 10)

			marginTop -= (7 * 100)

			slot.animate(
				{"margin-top":marginTop+"px"},
				{'duration' : time, 'easing' : "easeOutElastic"}
			);
		}

	});

})

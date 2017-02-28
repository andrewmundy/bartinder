$(document).ready(function(){	
	$("body").css({"background": "url('static/bgs/trop"+localStorage.rand+".jpg') fixed" });
	let random=(x)=>{return Math.ceil(Math.random()*x)}

	$( "#bgchange" ).on( "click", function() {
	  	localStorage.rand = random(6);
	  	$("body").css({"background": "url('static/bgs/trop"+localStorage.rand+".jpg') fixed" });
	});
});
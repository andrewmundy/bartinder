$( "#bgchange" ).on( "click", function() {
	var random = Math.ceil(Math.random()*6)
  	$("body").css({"background": "url('static/bgs/trop"+random+".jpg') fixed" } );
});
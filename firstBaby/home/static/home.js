$(function(){
	var path_name=window.location.href.split('/')[3];
	if(path_name==""){
		$('#home').addClass("underline")
	}else{
		$('#'+path_name).addClass("underline")
	}


});



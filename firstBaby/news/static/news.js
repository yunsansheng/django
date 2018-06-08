$(function(){
	$("#basic-addon2").click(function(){
		var keyword = $("#keyword").val()
		window.location.href="?keyword="+keyword;
		
		// 传递参数
		// 1.输入的关键词2.获取内容来源
	});

	//单击enter登录
	$('body').keydown(function (e) {
		//alert(e.which);
		if(e.which ==13){
			$('#basic-addon2').click();
			
		}
	});
});
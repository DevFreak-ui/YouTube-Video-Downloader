
$(document).ready(function(){
	$('.btn-toggle').click(function(){
	  $(this).toggleClass('dark-theme');

	  var $tog = $('#tog').attr('href');
	  if ($tog == "/static/css/light.css") {
	    $('#tog').attr('href', "/static/css/dark.css");
	  } else{
	    $('#tog').attr('href', "/static/css/light.css");
	  }
	});


	$('.dstream').click(function(){
		var url = $(this).attr('name')
		var res = $(this).attr('data-resolution')
		$.ajax({
			type: 'GET',
			url: 'download',
			data: {'url': url, 'res': res},

			success: function(data){
				alert('Video downloading...');
			},
			error: function(data){
				alert('Something went wrong');
			},
		});
	});



	// $('#link').keyup(function(){
	// 	var value = $('#link').val();
	// 	if (value.length > 0){
	// 		$.ajax({
	// 			type: "GET",
	// 			url: "watch",
	// 			data: {link: value},

	// 			success: function(data){
	// 				$('#dynamic').show();
	// 				var title = data['title'];
	// 				var thumbnail = data['thumbnail'];
	// 				$('#title').val(title);
	// 				$('#thumbnail').attr('src', thumbnail);
	// 				console.log(title);
	// 				console.log(thumbnail);
	// 				cconsole.log(videos, audios);
	// 			},
	// 			error: function(data){
	// 				console.log(data, 'This did not work');
	// 			},
	// 		});
	// 	}
	// });



});
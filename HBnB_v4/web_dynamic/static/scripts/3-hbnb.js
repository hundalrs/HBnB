document.addEventListener('DOMContentLoaded', function () {
    $.get('http://0.0.0.0:5001/api/v1/status', function (data, status) {
        if (status === 'success') {
            $('DIV#api_status').addClass('available');
        } else {
            $('DIV#api_status').removeClass('available');
        }
    });

    let result = {};
    $('input[type=checkbox]').click(function () {
	if (this.checked) {
	    result[$(this).attr('data-name')] = $(this).attr('data-id');
	} else {
	    delete result[$(this).attr('data-name')];
	}
	let amens_list = [];
	$.each(result, function (index, value) {
	    amens_list.push(index);
	});
	if (amens_list.length === 0) {
	    $('.amenities h4').html("&nbsp;");
	} else {
	    $('.amenities h4').text(amens_list.join(', '));
	}
    });

    $.ajax({
	url: 'http://0.0.0.0:5001/api/v1/places_search',
	type: 'POST',
	dataType: 'json',
	data: '{}',
	contentType: 'application/json',
	success: function (data) {
	    for (let i = 0; i < data.length; i++) {
		$('.places').append('<article>' +
		    '<div class="title">' +
		      '<h2>' + data[i].name + '</h2>' +
		      '<div class="price_by_night">' + data[i].price_by_night +
		      '</div>' +
		    '</div>' +
		    '<div class="information">' +
		      '<div class="max_guest">' +
		        '<i class="fa fa-users fa-3x" aria-hidden="true"></i>' +
		        '<br />' +
		          data[i].max_guest + ' Guests' +
		      '</div>' +
		      '<div class="number_rooms">' +
		        '<i class="fa fa-bed fa-3x" aria-hidden="true"></i>' +
		        '<br />' +
		          data[i].number_bathrooms + ' Bathrooms' +
		      '</div>' +
		    '</div>' +
		    '<div class="description">' +
		      data[i].description +
		    '</div>' +
		  '</article>')
	    }
	}
    });
});

document.addEventListener('DOMContentLoaded', function () {
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
});

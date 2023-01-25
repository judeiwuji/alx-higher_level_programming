const $ = window.$;
$(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    method: 'GET',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
});

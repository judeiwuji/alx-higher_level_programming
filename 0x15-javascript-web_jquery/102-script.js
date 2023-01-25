const $ = window.$;
$(function () {
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    $.ajax({
      url: 'https://fourtonfish.com/hellosalut/?lang=' + lang,
      method: 'GET',
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});

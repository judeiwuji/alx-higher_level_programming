const $ = window.$;
const loadData = function () {
  const lang = $('INPUT#language_code').val();
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=' + lang,
    method: 'GET',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
};

$(function () {
  $('INPUT#btn_translate').on('click', function (e) {
    loadData();
  });
  $('INPUT#language_code').on('keydown', function (e) {
    if (e.keyCode === 13) {
      loadData();
    }
  });
});

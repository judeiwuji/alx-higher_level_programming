const $ = window.$;
$(function () {
  $('DIV#update_header').on('click', function (e) {
    $('header').text('New Header!!!');
  });
});

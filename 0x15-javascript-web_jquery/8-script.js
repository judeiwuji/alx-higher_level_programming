const $ = window.$;
$(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      const movieList = $('UL#list_movies');
      for (const movie of data.results) {
        movieList.append(`<li>${movie.title}</li>`);
      }
    }
  });
});

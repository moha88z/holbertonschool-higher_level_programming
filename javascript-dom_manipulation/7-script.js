const listMovies = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    return response.json();
  })
  .then(data => {
    for (let i = 0; i < data.count; i++) {
      // console.log(data['results'][i]['title'])
      const newElem = document.createElement('li');
      newElem.textContent = data.results[i].title;
      listMovies.appendChild(newElem);
    }
  });

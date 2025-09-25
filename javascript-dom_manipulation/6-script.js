const character = document.getElementById('character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    return response.json();
  })
  .then(data => {
    character.textContent = data.name;
  });

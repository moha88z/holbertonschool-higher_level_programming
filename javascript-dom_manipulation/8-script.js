
function fetchChange () {
  const helloElem = document.getElementById('hello');
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => {
      return response.json();
    })
    .then(data => {
      const txt = data.hello;
      console.log(txt);
      helloElem.textContent = txt;
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
  fetchChange();
});

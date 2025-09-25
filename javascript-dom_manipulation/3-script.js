const headerElement = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');

toggleHeader.addEventListener('click', function () {
  if (headerElement.classList.contains('red')) {
    headerElement.classList.replace('red', 'green');
  } else if (headerElement.classList.contains('green')) {
    headerElement.classList.replace('green', 'red');
  }
});

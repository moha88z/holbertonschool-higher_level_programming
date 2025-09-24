const headerElement = document.querySelector('header');
const redHeader = document.getElementById('red_header');

redHeader.addEventListener('click', function () {
  headerElement.style.color = '#FF0000';
});

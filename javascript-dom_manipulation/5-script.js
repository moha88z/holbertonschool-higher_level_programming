const headerElement = document.querySelector('header');
const UpdateHeader = document.getElementById('update_header');

UpdateHeader.addEventListener('click', function () {
  headerElement.textContent = 'New Header!!!';
});

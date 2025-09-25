const myListElement = document.querySelector('.my_list');
const addItem = document.getElementById('add_item');

addItem.addEventListener('click', function () {
  const newElem = document.createElement('li');
  newElem.textContent = 'Item';
  myListElement.appendChild(newElem);
});

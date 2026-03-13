'use strict';

function markUnread() {
  const storageString = localStorage.getItem('viewedPronums')

  let viewedPronums = JSON.parse(storageString);
  if (viewedPronums === null) {
    viewedPronums = [];
  }

console.log(viewedPronums);

  for (const pronum of document.getElementsByClassName('pronum')) {
    if (!viewedPronums.includes(pronum.id)) {
      pronum.classList.add('new-pronum');
      viewedPronums.push(pronum.id);
    }
  }

  localStorage.setItem('viewedPronums', JSON.stringify(viewedPronums));
}

document.addEventListener('DOMContentLoaded', markUnread);

let articleSections = document.querySelectorAll('.blog-article');

for (let articleSection of articleSections) {
  let showButton = articleSection.querySelector('button.more');
  showButton.onclick = function() {
    articleSection.classList.remove('short');
  }
}
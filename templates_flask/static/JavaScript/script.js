function scrollGallery(direction) {
  var galleryContainer = document.querySelector('.gallery-container');
  var scrollAmount = 620; // Width of each image plus margin-right
  var scrollPosition = galleryContainer.scrollLeft;
  var maxScroll = galleryContainer.scrollWidth - galleryContainer.clientWidth;
  
  if (direction === 'left') {
    galleryContainer.scrollLeft -= scrollAmount;
    if (galleryContainer.scrollLeft <= 0) {
      document.querySelector('.scroll-arrow.left').classList.add('hidden');
    }
    if (scrollPosition > 0 && scrollPosition <= maxScroll) {
      document.querySelector('.scroll-arrow.right').classList.remove('hidden');
    }
  } else {
    galleryContainer.scrollLeft += scrollAmount;
    if (galleryContainer.scrollLeft > 0) {
      document.querySelector('.scroll-arrow.left').classList.remove('hidden');
    }
    if (galleryContainer.scrollLeft >= maxScroll) {
      document.querySelector('.scroll-arrow.right').classList.add('hidden');
    }
  }
}
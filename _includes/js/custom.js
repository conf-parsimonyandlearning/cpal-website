// CPAL 2026 behavior: a category title is an expand/collapse control, not a
// navigation link. The theme handles the arrow button; this adds the same
// behavior to the full category title.
document.addEventListener('click', function (event) {
  var titleButton = event.target.closest && event.target.closest('.nav-list-link-expander');
  if (!titleButton) return;

  event.preventDefault();
  var item = titleButton.parentElement;
  if (!item) return;

  var expanded = item.classList.toggle('active');
  titleButton.setAttribute('aria-pressed', expanded ? 'true' : 'false');

  var arrowButton = item.querySelector('.nav-list-expander');
  if (arrowButton) {
    arrowButton.setAttribute('aria-pressed', expanded ? 'true' : 'false');
  }
});

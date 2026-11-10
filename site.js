// Fit each page's scene to its panel: crop the sides on wide screens,
// show the whole centre of the scene on tall (portrait) screens.
(function () {
  var main = document.querySelector('main');
  var svg = main && main.querySelector('svg');
  if (!svg) return;
  var wide = svg.getAttribute('data-wide') || '0 0 1200 800';
  var tall = svg.getAttribute('data-tall') || '290 60 700 740';
  function fit() {
    var r = main.getBoundingClientRect();
    var portrait = r.width / r.height < 1;
    svg.setAttribute('viewBox', portrait ? tall : wide);
    svg.setAttribute('preserveAspectRatio', portrait ? 'xMidYMax meet' : 'xMidYMax slice');
  }
  fit();
  if ('ResizeObserver' in window) new ResizeObserver(fit).observe(main);
  else addEventListener('resize', fit);
})();

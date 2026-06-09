(function () {
  function markDoiLinks() {
    var links = document.querySelectorAll(
      'a.reference.external[href^="https://doi.org/"], ' +
        'a.reference.external[href^="http://doi.org/"], ' +
        'a.reference.external[href^="https://dx.doi.org/"], ' +
        'a.reference.external[href^="http://dx.doi.org/"]'
    );
    links.forEach(function (link) {
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", markDoiLinks);
  } else {
    markDoiLinks();
  }
})();

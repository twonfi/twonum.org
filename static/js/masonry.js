"use strict";

const ELEM = document.querySelector("[data-masonry-data]");
if (ELEM) {
  function reload() {
    const MASONRY = new Masonry(ELEM, JSON.parse(ELEM.getAttribute("data-masonry-data")));
  }

  reload();

  const IMGLOADED = imagesLoaded(ELEM, reload);
  IMGLOADED.on("progress", reload);
}

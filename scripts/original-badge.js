/**
 * Cenzia Decants — badge "Original"
 * Se inyecta en la tienda (Tienda Nube, tema recife) vía Scripts API.
 * Agrega una etiqueta visual "Original" sobre la imagen de cada producto,
 * tanto en grillas/listados como en la página de producto, excepto en los
 * combos (bundles de varias fragancias).
 */
(function () {
  "use strict";

  var EXCLUDED_PRODUCT_IDS = [
    304416283, 304599497, 304722332, 307532394, 307538717, 307541520,
    311869307, 312465816, 315713389, 315713873, 315792900, 316502354,
    324920787, 331559864, 331767446, 335852683, 349989590, 350227303
  ];

  var BADGE_CLASS = "cenzia-original-badge";
  var STYLE_ID = "cenzia-original-badge-style";

  function injectStyles() {
    if (document.getElementById(STYLE_ID)) return;
    var style = document.createElement("style");
    style.id = STYLE_ID;
    style.textContent =
      "." + BADGE_CLASS + "{" +
      "position:absolute;top:10px;right:10px;z-index:6;" +
      "display:inline-flex;align-items:center;" +
      "padding:4px 10px;border-radius:999px;" +
      "background:rgba(13,22,31,.92);" +
      "border:1px solid rgba(255,255,255,.35);" +
      "color:#fff;font-family:inherit;font-size:.62rem;font-weight:700;" +
      "letter-spacing:.12em;text-transform:uppercase;" +
      "box-shadow:0 2px 6px rgba(13,22,31,.25);" +
      "pointer-events:none;white-space:nowrap;" +
      "}" +
      ".js-item-product .item-image{position:relative;}" +
      "@media(max-width:576px){." + BADGE_CLASS + "{font-size:.56rem;padding:3px 8px;top:8px;right:8px;}}";
    document.head.appendChild(style);
  }

  function makeBadge() {
    var span = document.createElement("span");
    span.className = BADGE_CLASS;
    span.setAttribute("aria-hidden", "true");
    span.textContent = "Original";
    return span;
  }

  function isExcluded(id) {
    return EXCLUDED_PRODUCT_IDS.indexOf(Number(id)) !== -1;
  }

  function badgeGridItems(root) {
    var items = (root || document).querySelectorAll(".js-item-product[data-product-id]");
    items.forEach(function (item) {
      var id = item.getAttribute("data-product-id");
      if (!id || isExcluded(id)) return;
      var imageContainer = item.querySelector(".item-image");
      if (!imageContainer || imageContainer.querySelector("." + BADGE_CLASS)) return;
      imageContainer.appendChild(makeBadge());
    });
  }

  function badgeProductDetail() {
    if (!window.LS || !window.LS.product || !window.LS.product.id) return;
    if (isExcluded(window.LS.product.id)) return;

    var slider = document.querySelector(".product-detail-slider");
    if (!slider) return;

    var host = slider.parentElement;
    if (!host || host.querySelector("." + BADGE_CLASS)) return;

    var computedPosition = window.getComputedStyle(host).position;
    if (computedPosition === "static") {
      host.style.position = "relative";
    }
    host.appendChild(makeBadge());
  }

  function run(root) {
    injectStyles();
    badgeGridItems(root);
    badgeProductDetail();
  }

  function init() {
    run(document);

    var observer = new MutationObserver(function (mutations) {
      mutations.forEach(function (mutation) {
        mutation.addedNodes.forEach(function (node) {
          if (node.nodeType !== 1) return;
          run(node.parentNode || document);
        });
      });
    });
    observer.observe(document.body, { childList: true, subtree: true });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

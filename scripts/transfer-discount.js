/**
 * Cenzia Decants — precio con transferencia (10% OFF)
 * Calcula el descuento en base al precio real de cada producto (no un valor
 * fijo), así funciona para cualquier producto nuevo, incluidos combos con
 * precios distintos. Se inyecta vía Tienda Nube Scripts API.
 */
(function () {
  "use strict";

  var DISCOUNT = 0.10;
  var BLOCK_CLASS = "cz-transfer-price";

  function formatARS(n) {
    var rounded = Math.round(n * 100) / 100;
    var parts = rounded.toFixed(2).split(".");
    var intPart = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    return "$" + intPart + "," + parts[1];
  }

  function injectStyles() {
    if (document.getElementById("cz-transfer-price-style")) return;
    var style = document.createElement("style");
    style.id = "cz-transfer-price-style";
    style.textContent =
      "." + BLOCK_CLASS + "{display:flex;align-items:center;flex-wrap:wrap;gap:8px;" +
      "margin-top:10px;padding:12px 14px;background:#F6F7F8;border-radius:12px;" +
      "font-family:inherit;font-size:13px;color:#0d161f;}" +
      "." + BLOCK_CLASS + " .cz-pill{display:inline-flex;align-items:center;" +
      "background:#0d161f;color:#fff;font-size:11px;font-weight:800;" +
      "padding:5px 10px;border-radius:999px;letter-spacing:.02em;white-space:nowrap;}" +
      "." + BLOCK_CLASS + " .cz-amount{font-weight:800;font-size:15px;color:#0d161f;}" +
      ".js-item-product ." + BLOCK_CLASS + "{font-size:11.5px;padding:8px 10px;margin-top:6px;}" +
      ".js-item-product ." + BLOCK_CLASS + " .cz-amount{font-size:12.5px;}";
    document.head.appendChild(style);
  }

  function buildBlock(priceNumber) {
    var discounted = priceNumber * (1 - DISCOUNT);
    var el = document.createElement("div");
    el.className = BLOCK_CLASS;
    el.innerHTML =
      '<span class="cz-pill">−' + (DISCOUNT * 100) + '% OFF</span>' +
      '<span class="cz-amount">' + formatARS(discounted) + '</span>' +
      '<span>con Transferencia o depósito bancario</span>';
    return el;
  }

  function priceFromVariantsAttr(raw) {
    if (!raw) return null;
    try {
      var variants = JSON.parse(raw.replace(/&quot;/g, '"'));
      if (variants && variants.length && typeof variants[0].price_number === "number") {
        return variants[0].price_number;
      }
    } catch (e) {}
    return null;
  }

  function processGridItems(root) {
    (root || document).querySelectorAll(".js-item-product[data-product-id]").forEach(function (item) {
      var priceContainer = item.querySelector(".item-price-container");
      if (!priceContainer || priceContainer.querySelector("." + BLOCK_CLASS)) return;
      var variantsAttr = item.querySelector("[data-variants]");
      var price = variantsAttr ? priceFromVariantsAttr(variantsAttr.getAttribute("data-variants")) : null;
      if (price == null) return;
      priceContainer.appendChild(buildBlock(price));
    });
  }

  function processPDP() {
    if (!window.LS || !window.LS.variants || !window.LS.variants.length) return;
    var priceBlock = document.querySelector('[data-store^="product-price-"]');
    if (!priceBlock || priceBlock.querySelector("." + BLOCK_CLASS)) return;
    var price = window.LS.variants[0].price_number;
    if (typeof price !== "number") return;
    priceBlock.appendChild(buildBlock(price));
  }

  function run(root) {
    injectStyles();
    processGridItems(root);
    processPDP();
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

/* Mermaid init compatible with mkdocs-material instant navigation */
(function () {
  function initMermaid() {
    if (!window.mermaid) return;
    try {
      mermaid.initialize({
        startOnLoad: false,    // we trigger manually
        securityLevel: "loose" // or "strict"
      });
      const nodes = document.querySelectorAll(".mermaid");
      if (nodes.length) mermaid.init(undefined, nodes);
    } catch (e) {
      console.warn("Mermaid init error:", e);
    }
  }
  document.addEventListener("DOMContentLoaded", initMermaid);
  if (window.document$) window.document$.subscribe(initMermaid);
})();

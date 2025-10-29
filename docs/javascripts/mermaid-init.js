// docs/javascripts/mermaid-init.js
document.addEventListener("DOMContentLoaded", function () {
    if (window.mermaid) {
      mermaid.initialize({
        startOnLoad: true,
        securityLevel: "loose" // allow links; use "strict" if needed
        // theme: "default"
      });
    }
  });
  
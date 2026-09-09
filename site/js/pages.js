// Status page: probe each service from the browser and paint the result.
document.querySelectorAll("[data-check]").forEach(async (el) => {
  const url = el.getAttribute("data-check");
  try {
    const ctrl = new AbortController(); setTimeout(() => ctrl.abort(), 8000);
    await fetch(url, { mode: "no-cors", cache: "no-store", signal: ctrl.signal });
    el.textContent = "Operational"; el.classList.add("ok");
  } catch {
    el.textContent = "Unreachable from here"; el.classList.add("bad");
  }
});
// Headline follows the checks.
new MutationObserver(() => {
  const bad = document.querySelectorAll(".badge.bad").length;
  const h = document.querySelector(".page-h1");
  if (h && bad) h.textContent = bad === 1 ? "One service is unreachable" : `${bad} services are unreachable`;
}).observe(document.body, { subtree: true, attributes: true, attributeFilter: ["class"] });

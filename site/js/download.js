/* After a Download click: the file is on its way, so show how to install it. */
(() => {
  const css = `
.dl-modal{position:fixed;inset:0;z-index:200;display:grid;place-items:center;padding:20px;background:rgba(10,12,18,.55);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);opacity:0;transition:opacity .2s}
.dl-modal[data-show="true"]{opacity:1}
.dl-box{position:relative;width:min(1080px,100%);max-height:92vh;overflow:auto;background:#fff;border-radius:28px;padding:56px 40px 44px;box-shadow:0 40px 100px -30px rgba(0,0,0,.6);transform:translateY(10px);transition:transform .25s cubic-bezier(.2,.8,.2,1)}
.dl-modal[data-show="true"] .dl-box{transform:none}
.dl-x{position:absolute;right:22px;top:20px;width:36px;height:36px;border:0;background:none;font-size:26px;line-height:1;color:#8a8f98;cursor:pointer;border-radius:10px}
.dl-x:hover{background:#f2f3f5;color:#111}
.dl-done{display:flex;align-items:center;justify-content:center;gap:10px;font-size:22px;font-weight:600;color:#1a9b57}
.dl-done svg{width:24px;height:24px}
.dl-h{margin:26px 0 44px;text-align:center;font-family:var(--font-lead,inherit);font-size:clamp(34px,5.6vw,62px);font-weight:600;letter-spacing:-.03em;line-height:1.05;color:#111}
.dl-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:40px 34px}
@media(max-width:820px){.dl-steps{grid-template-columns:1fr}}
.dl-step{position:relative}
.dl-n{position:absolute;left:-14px;top:-14px;width:44px;height:44px;border-radius:50%;background:#0f1216;color:#fff;font-weight:700;font-size:18px;display:grid;place-items:center;box-shadow:0 6px 16px -6px rgba(0,0,0,.5);z-index:1}
.dl-img{aspect-ratio:520/330;border-radius:18px;overflow:hidden;box-shadow:0 0 0 1px rgba(0,0,0,.08);background:#fff}
.dl-img img{width:100%;height:100%;object-fit:cover;display:block}
.dl-cap{margin:22px 0 0;text-align:center;font-size:22px;line-height:1.45;color:#3a3f48}
.dl-cap b{font-weight:600;color:#2d7fbf}
.dl-foot{margin:44px 0 0;text-align:center;font-size:20px;color:#8a8f98}
.dl-foot a{color:#2d7fbf;font-weight:600;text-decoration:none}
`;
  const html = `<div class="dl-box" role="dialog" aria-modal="true" aria-labelledby="dl-title">
  <button class="dl-x" aria-label="Close">×</button>
  <div class="dl-done"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m8.5 12.5 2.5 2.5 5-5"/></svg>Downloaded</div>
  <h2 class="dl-h" id="dl-title">How to install Alibi</h2>
  <div class="dl-steps">
    <div class="dl-step"><span class="dl-n">1</span><div class="dl-img"><img src="ROOTimg/docs/install-1.webp" alt="Recent download history showing Alibi.dmg"></div><p class="dl-cap">Open <b>Alibi.dmg</b> from your <b>Downloads</b> folder</p></div>
    <div class="dl-step"><span class="dl-n">2</span><div class="dl-img"><img src="ROOTimg/docs/install-2.webp" alt="Dragging the Alibi icon into the Applications folder"></div><p class="dl-cap">Drag the <b>Alibi icon</b> into your <b>Applications</b> folder</p></div>
    <div class="dl-step"><span class="dl-n">3</span><div class="dl-img"><img src="ROOTimg/docs/install-3.webp" alt="Alibi in the Applications folder"></div><p class="dl-cap">Right-click <b>Alibi</b> in <b>Applications</b> and choose Open</p></div>
  </div>
  <p class="dl-foot">Problem? <a href="DMG">Download again</a> · <a href="ROOTdocs/install-macos/">Read the guide</a></p>
</div>`;
  const links = [...document.querySelectorAll('a[href$="Alibi.dmg"]')];
  if (!links.length) return;
  const dmg = links[0].getAttribute("href");
  // Site root, taken from where this script was loaded from.
  const root = (document.currentScript && document.currentScript.src || "").replace(/js\/download\.js.*$/, "");
  let modal;
  const open = () => {
    if (!modal) {
      const style = document.createElement("style"); style.textContent = css; document.head.append(style);
      modal = document.createElement("div"); modal.className = "dl-modal"; modal.innerHTML = html.replace(/ROOT/g, root).replace("DMG", dmg);
      document.body.append(modal);
      modal.querySelector(".dl-x").addEventListener("click", close);
      modal.addEventListener("click", (e) => { if (e.target === modal) close(); });
      document.addEventListener("keydown", (e) => { if (e.key === "Escape") close(); });
    }
    modal.hidden = false; setTimeout(() => (modal.dataset.show = "true"), 20);
  };
  const close = () => { if (!modal) return; modal.dataset.show = "false"; setTimeout(() => (modal.hidden = true), 220); };
  links.forEach((a) => a.addEventListener("click", () => setTimeout(open, 350)));
})();

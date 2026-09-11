/* Alibi landing page behaviours. No frameworks, no network calls. */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- header: frosted once scrolled, CTA once the hero button leaves ---- */
  const header = $('.v2-header');
  const onScroll = () => header.classList.toggle('v2-header--stuck', scrollY > 8);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
  const heroBtn = $('#top .v2-btn');
  const cta = $('.v2-header__cta');
  if (heroBtn && cta) new IntersectionObserver(([e]) => cta.dataset.shown = String(!e.isIntersecting), { threshold: 0 }).observe(heroBtn);

  /* ---- reveal on scroll ---- */
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.dataset.shown = 'true'; io.unobserve(e.target); } }), { rootMargin: '0px 0px -10% 0px' });
  $$('.v2-reveal').forEach(el => io.observe(el));

  /* ---- hero: rotating screenshots ---- */
  const frames = $$('#top [role="img"] picture img');
  if (frames.length > 1 && !reduced && !location.search.includes('still')) {
    let i = 0, z = 2;
    setInterval(() => {
      const prev = frames[i]; i = (i + 1) % frames.length; const next = frames[i];
      next.style.zIndex = String(z++); next.style.opacity = '1';
      setTimeout(() => { if (prev !== next) prev.style.opacity = '0'; }, 950);
    }, 6000);
  }

  /* ---- hero: the tappable mock ---- */
  const tap = $('.vanish-mock-tap');
  if (tap) {
    const shell = tap.parentElement;
    const [idle, spoofing] = $$('img', shell);
    const label = $('.mock-label', tap);
    tap.addEventListener('click', () => {
      const on = tap.dataset.on !== 'true';
      tap.dataset.on = String(on); tap.dataset.tapped = 'true';
      if (idle) idle.style.opacity = on ? '0' : '1';
      if (spoofing) spoofing.style.opacity = on ? '1' : '0';
      if (label) label.textContent = on ? 'Stop' : 'Alibi';
    });
  }

  /* ---- pricing ---- */
  const PLANS = {
    Weekly:   { base: 3.99,  mobile: 0.79,  suffix: '/wk', note: b => `$${b.toFixed(2)} billed weekly` },
    Monthly:  { base: 8.99,  mobile: 3.33,  suffix: '/mo', note: b => `$${b.toFixed(2)} billed monthly` },
    Annual:   { base: 34.99, mobile: 39.99, suffix: '/mo', per: 12, note: b => `$${b.toFixed(2)} billed yearly`, badge: 'Best value' },
    Lifetime: { base: 79.99, mobile: 0,     suffix: '',   note: () => 'One-time. Mobile included.', badge: 'Pay once', includesMobile: true },
  };
  const tabs = $$('#pricing .v2-tab');
  const mob = $('#pricing .v2-mob');
  const amount = $('.v2-price__amount'), suffix = $('.v2-price__suffix'), badge = $('#pricing .v2-badge'), note = $('.v2-plan-note');
  const inclMob = $('.v2-incl__mob'), link = $('.v2-incl__link'), linkPath = link && $('path', link);
  let plan = 'Annual', mobileOn = false, shown = 0;

  const tween = (to) => {
    const from = shown; const t0 = performance.now(); const d = reduced ? 0 : 420;
    const step = (t) => {
      const k = d ? Math.min(1, (t - t0) / d) : 1; const e = 1 - Math.pow(1 - k, 3);
      shown = from + (to - from) * e; amount.textContent = '$' + shown.toFixed(2);
      if (k < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  const drawLink = () => {
    if (!linkPath || !inclMob || !mob) return;
    const board = link.parentElement.getBoundingClientRect();
    const row = $('.v2-feat', inclMob).getBoundingClientRect();
    const sw = $('.v2-switch', mob).getBoundingClientRect();
    const x1 = row.right - board.left + 10, y1 = row.top - board.top + row.height / 2;
    const x2 = sw.left - board.left + sw.width / 2, y2 = sw.bottom - board.top;
    const midY = y1 - 40;
    linkPath.setAttribute('d', `M${x1},${y1} C${x1 + 280},${y1} ${x2},${midY + 60} ${x2},${midY} C${x2},${midY - 30} ${x2},${y2 + 20} ${x2},${y2}`);
    link.setAttribute('width', board.width); link.setAttribute('height', board.height);
  };
  const render = () => {
    const p = PLANS[plan];
    const includes = mobileOn || !!p.includesMobile;
    let total = p.base + (mobileOn && !p.includesMobile ? p.mobile : 0);
    const display = p.per ? total / p.per : total;
    tween(display);
    suffix.textContent = p.suffix;
    note.textContent = p.note(total);
    if (badge) { badge.textContent = p.badge || ''; badge.style.display = p.badge ? '' : 'none'; }
    if (inclMob) {
      inclMob.classList.toggle('v2-incl__mob--off', !includes);
      const svg = $('svg', inclMob);
      svg.innerHTML = includes
        ? '<path d="M2 6.5L4.5 9L10 3" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"></path>'
        : '<path d="M3.3 3.3L8.7 8.7M8.7 3.3L3.3 8.7" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"></path>';
    }
    if (link) link.classList.toggle('v2-incl__link--off', !includes);
    if (mob) {
      mob.setAttribute('aria-checked', String(includes));
      mob.setAttribute('aria-disabled', String(!!p.includesMobile));
      $('.v2-mob__glyph', mob).classList.toggle('v2-mob__glyph--off', !includes);
      $('.v2-mob__note', mob).textContent = p.includesMobile ? 'Included' : '+$3.33/mo';
    }
    tabs.forEach(t => {
      const on = t.textContent.trim() === plan;
      t.setAttribute('aria-selected', String(on));
      let pill = $('.v2-tab__pill', t);
      if (on && !pill) { pill = document.createElement('span'); pill.className = 'v2-tab__pill'; t.prepend(pill); }
      if (!on && pill) pill.remove();
    });
    requestAnimationFrame(drawLink);
  };
  tabs.forEach(t => t.addEventListener('click', () => { plan = t.textContent.trim(); render(); }));
  if (mob) mob.addEventListener('click', () => { if (!PLANS[plan].includesMobile) { mobileOn = !mobileOn; render(); } });
  addEventListener('resize', drawLink);
  if (amount) { shown = parseFloat(amount.textContent.replace('$', '')) || 0; render(); }

  /* ---- the pretend checkout ---- */
  const toast = $('#toast');
  const say = (msg) => {
    toast.textContent = msg; toast.hidden = false;
    requestAnimationFrame(() => toast.dataset.show = 'true');
    clearTimeout(say.t); say.t = setTimeout(() => { toast.dataset.show = 'false'; setTimeout(() => toast.hidden = true, 300); }, 3200);
  };
  const lines = ['Paid plans are coming soon — Alibi is free to use right now.', 'Coming soon. For now, grab it free or use a referral for 3 weeks.'];
  let n = 0;
  $('#get-alibi')?.addEventListener('click', () => say(lines[n++ % lines.length]));

  /* ---- faq accordion ---- */
  $$('.v2-faq__q').forEach(q => q.addEventListener('click', () => {
    const open = q.getAttribute('aria-expanded') === 'true';
    $$('.v2-faq__q').forEach(o => { o.setAttribute('aria-expanded', 'false'); o.nextElementSibling.dataset.open = 'false'; });
    if (!open) { q.setAttribute('aria-expanded', 'true'); q.nextElementSibling.dataset.open = 'true'; }
  }));

  /* ---- videos: some browsers need a nudge ---- */
  $$('video').forEach(v => { v.muted = true; v.play?.().catch(() => {}); });
})();

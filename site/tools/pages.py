#!/usr/bin/env python3
"""Generates the secondary pages (guides, comparisons, careers, status, terms, privacy)
into site/, sharing the landing page's header, footer and stylesheet. Run from anywhere."""
import pathlib, html, re
SITE = pathlib.Path(__file__).resolve().parent.parent
REPO = "https://github.com/Nickkk66/alibi"
REL = REPO + "/releases/latest/download/Alibi.dmg"
YEAR = "2026"

def esc(s): return html.escape(s, quote=False)

def inline(text):
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    return text

def md(body):
    """Tiny markdown: #, ##, paragraphs, - lists, | tables, > note, ### faq q/a pairs."""
    out, para, ul, table = [], [], [], []
    def flush():
        nonlocal para, ul, table
        if para: out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
        if ul: out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in ul) + "</ul>"); ul = []
        if table:
            head, *rows = table
            out.append('<div class="tbl"><table><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>" +
                       "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>"); table = []
    for line in body.strip().splitlines():
        s = line.strip()
        if not s: flush(); continue
        if s.startswith("### "): flush(); out.append(f'<h3>{inline(s[4:])}</h3>'); continue
        if s.startswith("## "): flush(); out.append(f'<h2>{inline(s[3:])}</h2>'); continue
        if s.startswith("- "): para and flush(); ul.append(s[2:]); continue
        if s.startswith("|"):
            para and flush(); cells = [c.strip() for c in s.strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells): continue
            table.append(cells); continue
        if s.startswith("> "): flush(); out.append(f'<p class="note">{inline(s[2:])}</p>'); continue
        if s.startswith("<"): flush(); out.append(s); continue
        if s.startswith("Q: "): flush(); out.append(f'<p class="q">{inline(s[3:])}</p>'); continue
        if s.startswith("A: "): flush(); out.append(f'<p class="a">{inline(s[3:])}</p>'); continue
        para.append(s)
    flush()
    return "\n".join(out)

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#F2622E">
<link rel="icon" type="image/svg+xml" href="{root}img/favicon.svg">
<meta property="og:site_name" content="Alibi"><meta property="og:type" content="article"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{root}img/og.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=EB+Garamond:ital,wght@0,400..700;1,400..600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}css/alibi.css">
<link rel="stylesheet" href="{root}css/pages.css">
</head>
<body>
<div class="v2-root page-root">
<header class="v2-header v2-header--stuck"><div class="v2-wrap v2-header__inner">
<a class="v2-brand" href="{root}"><span class="v2-brand__icon" aria-hidden="true"><img class="on-white" src="{root}img/mark.svg" alt="" width="27" height="27" style="opacity:1"></span><span>Alibi</span></a>
<nav class="v2-nav"><a href="{root}#how">How it works</a><a href="{root}#trust">Why it’s safe</a><a href="{root}#pricing">Pricing</a><a href="{root}guides/">Guides</a></nav>
<div class="v2-header__right"><a class="v2-header__billing" href="{repo}" target="_blank" rel="noopener">GitHub</a><div class="v2-header__cta" data-shown="true"><a class="v2-btn v2-btn--primary v2-btn--sm" href="{rel}">Download for Mac</a></div></div>
</div></header>
<main class="page">
"""
FOOT = """
</main>
<footer class="v2-footer"><div class="v2-wrap"><hr class="v2-rule" style="margin-bottom: 40px;">
<div class="v2-footer__cols">
<div><span style="display:flex;align-items:center;gap:6px"><img src="{root}img/mark.svg" alt="" width="27" height="27" style="display:block"><span style="font-size:19.5px;font-weight:600;letter-spacing:-.028em;color:var(--ink)">Alibi</span></span><p style="margin:18px 0 0;max-width:260px;font-size:14.5px;line-height:1.55;color:var(--muted)">An open-source way to put your iPhone somewhere else.</p></div>
<div><h4>Product</h4><ul><li><a href="{rel}">Download for Mac</a></li><li><a href="{root}#pricing">Pricing</a></li><li><a href="{root}#how">How it works</a></li><li><a href="{root}status/">Status</a></li></ul></div>
<div><h4>Guides</h4><ul><li><a href="{root}guides/">All guides</a></li><li><a href="{root}iphone-location-spoofer/">iPhone location spoofer</a></li><li><a href="{root}gps-spoofer-ios/">GPS spoofer for iOS</a></li><li><a href="{root}spoof-location-iphone-usb/">Spoof via USB</a></li></ul></div>
<div><h4>Compare</h4><ul><li><a href="{root}alibi-vs-ghostme/">Alibi vs GhostMe</a></li><li><a href="{root}alibi-vs-imyfone/">Alibi vs iMyFone AnyTo</a></li><li><a href="{root}alibi-vs-vanish/">Alibi vs Vanish</a></li></ul></div>
<div><h4>Project</h4><ul><li><a href="{repo}">Source code</a></li><li><a href="{root}careers/">Careers</a></li><li><a href="{root}terms/">Terms</a></li><li><a href="{root}privacy/">Privacy</a></li></ul></div>
</div>
<hr class="v2-rule" style="margin:40px 0 24px"><div class="v2-footer__bottom"><p style="margin:0;font-size:13.5px;color:var(--muted-2)">© {year} Alibi contributors. MIT licensed.</p></div>
</div></footer>
</div>
<script src="{root}js/pages.js" defer></script>
</body>
</html>
"""

def page(slug, title, desc, eyebrow, h1, lede, body, updated=None, cta=True, wide=False):
    root = "../"
    extra = ""
    if updated: extra += f'<p class="updated">Last updated: {updated}</p>'
    hero = f'''<section class="v2-wrap page-hero{" page-hero--wide" if wide else ""}">
<p class="v2-eyebrow">{esc(eyebrow)}</p>
<h1 class="page-h1">{inline(h1)}</h1>
<p class="page-lede">{inline(lede)}</p>{extra}
</section>'''
    ctas = "" if not cta else f'''<section class="v2-wrap page-cta"><div class="v2-stage" style="padding:56px 24px;text-align:center"><div class="v2-stage__inner"><h2 class="v2-h1" style="font-size:clamp(28px,4.4vw,44px);color:#fff;max-width:560px;margin:0 auto">Try Alibi for iPhone location changing</h2><p style="max-width:440px;margin:16px auto 0;font-size:16px;line-height:1.5;color:rgba(255,255,255,.62)">Download Alibi, plug your iPhone in over USB, and move it from your computer. Free, open source, no account.</p><div style="margin-top:26px"><a class="v2-btn v2-btn--onDark v2-btn--sheen" href="{REL}">Download for Mac</a></div></div></div></section>'''
    content = HEAD.format(title=esc(title), desc=esc(desc), root=root, repo=REPO, rel=REL) + hero + f'<article class="v2-wrap page-body">{md(body)}</article>' + ctas + FOOT.format(root=root, repo=REPO, rel=REL, year=YEAR)
    d = SITE / slug; d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(content, encoding="utf8")
    print("wrote", slug)

GUIDE_RELATED = """
## Related Alibi guides
[iPhone Location Spoofer](../iphone-location-spoofer/) · [GPS Spoofer for iOS](../gps-spoofer-ios/) · [Spoof iPhone Location via USB](../spoof-location-iphone-usb/) · [All guides](../guides/)
"""
INTRO = "Alibi is an open-source desktop tool for USB-connected iPhone location simulation. It does not require jailbreaking, it has no account or licence, and it is designed for people who want a desktop-controlled way to set or move a simulated iPhone GPS location."

page("guides", "Alibi Guides | iPhone GPS Spoofing Resources", "Practical guides for iPhone GPS spoofing, no-jailbreak location simulation, USB setup and what actually happens on the phone.",
     "Resources", "Alibi Guides", "Practical guides for iPhone GPS spoofing, no-jailbreak location simulation, USB setup, and what the phone is really doing.", """
Alibi is an open-source desktop tool for USB-connected iPhone location simulation. These guides explain how it works, what setup you need, and when system-level GPS spoofing is the right choice.

## iPhone GPS spoofing
- [iPhone Location Spoofer](../iphone-location-spoofer/) — what a spoofer has to do to change what apps see, and why a browser trick is not that.
- [GPS Spoofer for iOS](../gps-spoofer-ios/) — how iOS differs from Android, and why a computer is part of the story.

## Setup
- [Spoof iPhone Location via USB](../spoof-location-iphone-usb/) — the cable, Developer Mode, trust, and what Alibi checks before it lets you teleport.
- [How it works, in depth](https://github.com/Nickkk66/alibi/blob/main/docs/ARCHITECTURE.md) — the protocol chain, from pairing to the LocationSimulation service.

## Comparisons
- [Alibi vs GhostMe](../alibi-vs-ghostme/)
- [Alibi vs iMyFone AnyTo](../alibi-vs-imyfone/)
- [Alibi vs Vanish](../alibi-vs-vanish/)
""", cta=True)

page("iphone-location-spoofer", "iPhone Location Spoofer | USB GPS Spoofing with Alibi", "Alibi lets you simulate an iPhone GPS location from your desktop over USB, without jailbreaking. Open source, no account.",
     "iPhone GPS spoofing", "iPhone Location Spoofer", "Alibi lets you simulate an iPhone GPS location from your desktop over USB, without jailbreaking your device. Open source, no account, no licence.", f"""
{INTRO}

## What an iPhone location spoofer should actually do
An iPhone location spoofer should change the location that apps on the phone receive, not just the location shown inside a browser tab. That difference matters. Browser-only spoofing can help a website test geolocation, but it does not make the iPhone itself report a simulated GPS location to apps.
Alibi is built around the stronger version: a desktop app controls a connected iPhone over USB and starts a simulated location session through the same developer service Xcode uses. Choose a point, press Teleport, and every app on the phone reads that coordinate until you stop or clear it.

## Why Alibi uses a desktop and USB approach
iOS does not let normal App Store apps rewrite system GPS. Anything that promises a one-tap mobile-only solution is either using the same developer pathway behind the scenes or not doing what it says. Alibi is honest about the shape of the problem: a computer, a cable, and a short setup on the phone.
The desktop app manages the connection, the checks, the developer image, and the location session in one place. There is no jailbreak, no profile, and nothing installed on the phone except, optionally, Alibi Mobile.

## Core features
- Point teleport for setting one exact coordinate.
- Two-Spot and Multi-Stop routes for moving between places at walking, biking or driving pace.
- Stop and Clear controls that hand real GPS straight back.
- Lock: close the tunnel without clearing, and the fix holds until the phone reboots.
- Presets (Home, Work), favorites, recents, and paste-in coordinates.
- Alibi Mobile: an iPhone app, installed once from the desktop, that does the same thing without a computer.

## What to check before using it
Your iPhone should be connected over USB, unlocked, and trusted. Developer Mode must be on (Settings › Privacy & Security › Developer Mode). Alibi walks through each of these on screen and tells you exactly which one is missing.
The first time, Alibi mounts Apple's developer disk image on the phone. On a Mac with Xcode the image comes from Xcode; elsewhere it is downloaded once.

## Responsible use
Alibi is a general-purpose location simulation tool. Third-party apps, games, schools, workplaces and services may have their own rules about simulated locations, and some detect it. Use it for testing, previews, demos, privacy-aware workflows and controlled personal use. Do not use it for fraud, harassment, evading safety systems, or breaking another service's rules.

## Frequently asked questions
Q: Does Alibi require jailbreaking my iPhone?
A: No. Alibi uses the location simulation service Apple ships for developers. iOS is never modified.
Q: Does this only affect websites?
A: No. The simulated location is set at the system level, so every app on the phone receives it.
Q: Can I clear the simulated location?
A: Yes. Stop brings real GPS back immediately. A locked spoof clears on reboot.
Q: Is it really free?
A: Yes. MIT licensed, source on GitHub, no account, no licence key.
{GUIDE_RELATED}
""", updated="September 8, 2026")

page("gps-spoofer-ios", "GPS Spoofer for iOS | No Jailbreak iPhone Location Tool", "A practical iOS GPS spoofer needs to work with the phone, not just a browser. Alibi uses a desktop-controlled USB workflow, open source.",
     "iOS GPS spoofing", "GPS Spoofer for iOS", "A practical iOS GPS spoofer needs to work with the phone, not just a browser. Alibi uses a desktop-controlled USB workflow for supported iPhones.", f"""
{INTRO}

## The difference between GPS spoofing on iOS and Android
Android has mock-location settings many users can turn on directly. iOS is different. Apple does not expose a general-purpose GPS override to normal apps, which is why so many search results promise a mobile-only fix and never explain the real setup.
A serious GPS spoofer for iOS involves a computer at least once. Alibi follows that model: the desktop app manages the connection, the checks, and the simulated location session while the iPhone is connected over USB. Alibi Mobile then lets the phone carry on alone.

## What Alibi changes
Alibi simulates the iPhone's location, not a map on your computer. Once a session is active the phone receives a simulated coordinate through the same service Xcode uses when a developer tests location features. That is the practical difference between a real iOS GPS spoofer and a browser geolocation override.
Set a single point, or use Two-Spot and Multi-Stop routes when movement is needed.

## Why no jailbreak matters
Jailbreaking adds security risk, compatibility issues and maintenance, and can break with every iOS update. Alibi never modifies the operating system. Developer Mode, USB trust and the developer image still matter, but the core installation stays untouched.

## Good use cases
- Testing how an app responds in different regions.
- Demonstrating a location-based workflow.
- Previewing maps and region-specific screens.
- Setting a temporary simulated coordinate for personal workflows.

## Limits to understand
No spoofer can guarantee compatibility with every app or every iOS version forever. Third-party apps can update detection, change rules, or block simulated locations. Alibi is a powerful utility, not a promise that every service will accept every coordinate.

## Frequently asked questions
Q: Is Alibi an iOS app?
A: Alibi is a desktop app plus an optional iPhone app. The desktop app installs Alibi Mobile once; after that the phone can change its own location without a computer.
Q: Can I move between locations instead of teleporting once?
A: Yes. Two-Spot and Multi-Stop play routes at walking, biking or driving pace.
Q: Does Alibi guarantee every third-party app will accept the spoofed location?
A: No. Some apps detect simulated location and may restrict accounts.
{GUIDE_RELATED}
""", updated="September 8, 2026")

page("spoof-location-iphone-usb", "Spoof iPhone Location via USB | Alibi Desktop GPS Tool", "USB location spoofing gives Alibi a reliable desktop-controlled path for simulating iPhone GPS coordinates.",
     "USB iPhone location spoofing", "Spoof iPhone Location via USB", "USB gives Alibi a reliable, desktop-controlled path for simulating iPhone GPS coordinates, and a way to check every step before you teleport.", f"""
{INTRO}

## Why USB matters
USB gives the desktop app a direct way to talk to the iPhone during setup and location simulation. iPhone GPS spoofing is not a website setting; the tool has to coordinate with the device. Alibi uses the computer as the control centre: connection state, setup checks, spoofing controls, route movement, and cleanup like Stop and Clear.

## What Alibi checks when you plug in
- **Trust.** The phone must be unlocked and trusted by this computer. Alibi waits and tells you.
- **Developer Mode.** Apple's own switch under Settings › Privacy & Security. Alibi notices the moment you turn it on.
- **iOS version.** iOS 17.4 or later.
- **Developer image.** Mounted automatically the first time, with a progress bar.
When all four pass, the status line reads Connected with the model and iOS version, and the pill on the map says Ready.

## What you need before starting
- A supported iPhone connected to the computer with a USB cable.
- The phone unlocked and trusted during setup.
- Developer Mode enabled.
- A Mac (Windows and Linux builds come from the same code and are on the roadmap).

## Stopping and clearing
Stop sends the stop command and real GPS returns immediately. Closing Alibi while spoofing clears the location too, unless you turn on "Keep spoofing after quit", in which case the fix holds until the phone reboots.

## Frequently asked questions
Q: Do I need to keep the iPhone connected by USB?
A: While spoofing from the desktop, yes, unless you lock the spoof. Alibi Mobile removes the cable entirely.
Q: Is USB spoofing safer than jailbreaking?
A: Yes. Nothing on iOS is modified.
Q: What happens when I stop spoofing?
A: Real GPS takes over immediately.
{GUIDE_RELATED}
""", updated="September 8, 2026")

def compare(slug, other, title, desc, h1, lede, table, body):
    page(slug, title, desc, "Comparison", h1, lede, f"""
## At a glance
{table}

{body}

## Which should you pick?
Choose Alibi if you want to read the code that touches your phone, pay nothing, keep spoofing after you unplug, and have the iPhone app included. Choose {other} if one of the things it does and Alibi does not is genuinely on your list. We would rather say that than sell you the wrong thing, and we are not selling anything anyway.
""", updated="September 8, 2026", wide=True)

compare("alibi-vs-ghostme", "GhostMe", "Alibi vs GhostMe: iPhone Location Changers Compared (2026)", "Both move your iPhone anywhere from a Mac with no jailbreak. One is open source and free; the other is desktop-only and paid.",
        "Alibi vs GhostMe: **free and open, or paid and tethered**", "Both move your iPhone anywhere on Earth from a computer with no jailbreak. Only one of them lets you read the source, unplug and keep going, and costs nothing.",
        """| Feature | Alibi | GhostMe |
|---|---|---|
| No jailbreak required | Yes | Yes |
| Open source | Yes, MIT | No |
| Price | $0 | $12.95/mo or $42.95/yr |
| Mac app | Yes | Yes |
| Windows app | On the roadmap (same code) | Yes |
| Teleport anywhere | Yes | Yes |
| Simulated routes (walk, bike, drive) | Yes | Yes |
| Spoof from the iPhone with no computer | Alibi Mobile | No |
| Keeps spoofing after you unplug | Lock and unplug | No |
| Try it before paying | Nothing to pay | Pay first |
| Account or licence | None | Licence |""", """
## Where the two are alike
GhostMe and Alibi both run on a computer, both talk to the iPhone through the developer-mode facility Apple already ships, so neither asks you to jailbreak anything. Both connect over the cable that came in the box. Both let you search an address, drop a pin, save the places you use often, and simulate movement along a route.

## The core difference: what happens after you unplug
GhostMe is a computer program that changes your iPhone's location, and the computer stays in the loop. Alibi treats the computer as a setup step: install once, and after that Alibi Mobile does it from the phone. If you never want the phone app, start a spoof from the desktop, lock it, unplug, and the location holds until the phone reboots.

## And the price
GhostMe is $12.95 a month or $42.95 a year, auto-renewing. Alibi is free. Every feature, every platform, and the iPhone app, with the source on GitHub. There is a pricing section on the Alibi homepage because it is a nice pricing section; every tier on it is $0.

> GhostMe's prices were taken from getghostme.com in September 2026 and may have changed.
""")

compare("alibi-vs-imyfone", "iMyFone AnyTo", "Alibi vs iMyFone AnyTo: iPhone Location Changers Compared (2026)", "AnyTo splits its phone app, device allowance and price across VIP and SVIP tiers. Alibi is one free, open-source tool with the iPhone app included.",
        "Alibi vs iMyFone AnyTo: **one free tool, or a tier ladder**", "AnyTo splits its phone app, its device allowance and its price across VIP and SVIP. Alibi is one open-source tool with the iPhone app already in it and nothing to buy.",
        """| Feature | Alibi | iMyFone AnyTo |
|---|---|---|
| No jailbreak required | Yes | Yes |
| Open source | Yes, MIT | No |
| Price | $0 | Monthly, quarterly, yearly, lifetime across two tiers |
| Spoof from the phone with no computer | Alibi Mobile | SVIP tier, 1 iPhone |
| Device seats | No limit | 5 (VIP), 10 (SVIP) |
| Keeps spoofing after you unplug | Lock and unplug | No |
| Simulated routes | Two-Spot and Multi-Stop | Two-spot and multi-spot |
| Joystick control | No | Yes |
| GPX file import | No | Yes |
| Android devices | iPhone only | Yes |""", """
## The core difference: what a licence buys you
AnyTo is sold as a ladder. VIP covers five devices; SVIP raises that to ten and adds the phone-only app for exactly one iPhone. Alibi is one product: the Mac app and Alibi Mobile, free, with no seats to count.

## Where AnyTo genuinely wins
AnyTo has a joystick for steering movement by hand, GPX import for route files you already have, very long multi-spot routes, and Android support. Alibi does none of those four today. If one of them is on your list, buy AnyTo.

## Trying it
iMyFone backs its plans with a 30-day refund policy: pay first, test, then ask for your money back. With Alibi there is nothing to pay and nothing to refund. Plug your phone in and watch it move.

> Details checked on imyfone.com in September 2026. iMyFone discounts often, so figures on their page may differ.
""")

compare("alibi-vs-vanish", "Vanish", "Alibi vs Vanish: the same idea, one of them open source", "Alibi is an open-source take on Vanish. Same developer pathway, same features, no licence server.",
        "Alibi vs Vanish: **the same idea, in the open**", "Alibi started as an open-source answer to Vanish. Same Apple developer pathway, same set of features, none of the licensing.",
        """| Feature | Alibi | Vanish |
|---|---|---|
| No jailbreak required | Yes | Yes |
| Open source | Yes, MIT | No |
| Price | $0 | From $3.99/wk, $34.99/yr, $84.99 lifetime |
| iPhone app without a computer | Alibi Mobile | Vanish Mobile |
| Lock and unplug | Yes | Yes |
| Routes | Two-Spot, Multi-Stop | Real-road routes |
| Scheduled movement | On the roadmap | Yes |
| Wireless spoofing over Wi-Fi | On the roadmap | Yes |
| Licence server | None | Yes |
| Support | GitHub issues | Ticket queue |""", """
## Credit where it is due
Vanish is a polished product and the reference Alibi's interface follows. If you want a company behind the app, a support queue and scheduled routes today, Vanish is a fine choice.

## What Alibi does differently
Everything Alibi does is in a public repository. There is no licence check, no machine identifier, no analytics on the website, and nothing to renew. The app talks to Apple's servers only for the developer image and, if you install Alibi Mobile, the Apple ID sign-in that Apple requires.

> Vanish's prices were taken from getvanish.app in September 2026.
""")

page("careers", "Careers at Alibi", "Alibi is an open-source project. The only role is contributor, and it is open.",
     "Careers", "Come build what's moving people.", "Alibi moves iPhones anywhere on Earth. Behind that sits a Rust core, a Mac app, an iPhone app, and a landing page with a pricing section that charges nothing. There is no company. There are contributors.", """
People here own work end to end, from the drawing board through to the issue it eventually generates. We take on problems instead of throwing them over a ticket, mostly because there is nobody on the other side of the ticket.

## Open roles
- **Contributor** · Remote · Whenever you like · $0/hr, same as everyone. You will work on whatever you find interesting: the Windows build, scheduled routes, wireless spoofing, on-device certificate refresh, the iPhone app, or this page. Tell us about something you have built, even if it was for yourself. [Open an issue or a pull request](https://github.com/Nickkk66/alibi).
- **Maintainer** · Remote · Also $0. You will review pull requests, cut releases, and keep `docs/ARCHITECTURE.md` honest. A good fit reads code carefully and writes plainly. [Say hello in Discussions](https://github.com/Nickkk66/alibi/discussions).

None of these quite you? Star the repo anyway and tell us what you would do here.
""", cta=False)

def status_item(title, desc, check=None, fixed="Operational"):
    badge = f'<span class="badge" data-check="{check}">Checking…</span>' if check else f'<span class="badge ok">{fixed}</span>'
    return f'<div class="st"><div><b>{esc(title)}</b><p>{esc(desc)}</p></div>{badge}</div>'

page("status", "Alibi Status", "Live status of Alibi's downloads, website and the services the app depends on.",
     "Status", "All systems operational", "Checked from this browser just now.", "\n".join([
    '<div class="st-list">',
    status_item("Spoofing: Desktop", "Location changes started from the Mac app. Runs on your machine; there is no server to be down."),
    status_item("Spoofing: Mobile", "Location changes started from Alibi Mobile. Also runs on your phone."),
    status_item("Website", "nickkk66.github.io/alibi and these pages.", "https://nickkk66.github.io/alibi/"),
    status_item("Downloads", "The Mac installer, served by GitHub Releases.", "https://api.github.com/repos/Nickkk66/alibi/releases/latest"),
    status_item("Developer image", "Apple's developer disk image, mirrored on GitHub.", "https://raw.githubusercontent.com/doronz88/DeveloperDiskImage/main/PersonalizedImages/Xcode_iOS_DDI_Personalized/BuildManifest.plist"),
    status_item("Map tiles", "OpenFreeMap, used by the desktop app.", "https://tiles.openfreemap.org/styles/dark"),
    status_item("Checkout", "There is no checkout.", fixed="Permanently operational"),
    status_item("Licensing", "There is no licensing.", fixed="Permanently operational"),
    '</div>',
    "> These checks run in your browser and reflect what your connection can actually reach.",
]), cta=False)

page("terms", "Alibi Terms of Use", "The rules for using Alibi: what it is, what it is not, and what you are responsible for.",
     "Legal", "Terms of Use", "The rules for using Alibi, including device requirements, acceptable use, and the fact that there is nothing to buy.", """
## 1. What Alibi is
Alibi is open-source software, released under the MIT License, that simulates the location of a connected iPhone over USB using Apple's developer location-simulation service. Alibi Mobile is a companion iPhone app, installed from the desktop app, that does the same from the phone itself. Alibi does not jailbreak or modify iOS.
The MIT License is the licence for the software. These terms explain how the project expects it to be used; they do not add restrictions to the licence.

## 2. No purchase, no account
Alibi has no price, no licence key, no account, no trial and no subscription. The pricing section on the homepage is a design homage and every tier on it costs nothing. Nobody will ever ask you for payment details on behalf of Alibi.

## 3. Eligibility and device requirements
You must be legally allowed to use location simulation in your jurisdiction and must have authority over the computer, iPhone and Apple ID involved. Alibi requires a supported iPhone on iOS 17.4 or later, a USB connection for setup, Developer Mode, and internet access the first time for the developer image. Compatibility may change as Apple changes iOS.

## 4. Your responsibilities
You are solely responsible for your use of Alibi and for complying with all laws, platform rules, app terms, game terms and account policies that apply to you. Do not use Alibi for fraud, harassment, stalking, impersonation, evading safety systems, cheating in services that forbid location simulation, or interfering with networks, devices or accounts you do not own.
Third-party apps may detect simulated location and restrict or ban accounts. Alibi's contributors are not responsible for third-party enforcement.

## 5. No warranty
Alibi is provided "as is", without warranty of any kind, as the MIT License states. Nothing here promises that Alibi works with any specific app, service, iOS version or device.

## 6. Apple ID and sideloading
Installing Alibi Mobile uses your Apple ID to obtain a free development certificate from Apple. Your credentials go from your computer to Apple. Alibi has no server and never receives them. Free Apple IDs are limited by Apple to a small number of sideloaded apps and to seven-day certificates.

## 7. Changes
These terms may change as the project changes. The current version is always in the repository.

## 8. Contact
Open an issue at [github.com/Nickkk66/alibi/issues](https://github.com/Nickkk66/alibi/issues).
""", updated="September 8, 2026", cta=False)

page("privacy", "Alibi Privacy Policy", "What Alibi collects: nothing. What the app talks to: Apple, OpenStreetMap, GitHub.",
     "Legal", "Privacy Policy", "What Alibi collects (nothing), what it does not collect (everything else), and which third parties the app talks to and why.", """
## 1. Overview
Alibi has no server, no account system, no analytics and no licence checks. There is nothing for Alibi to collect, so it collects nothing. This page exists to say that plainly and to list the third parties the software talks to on your behalf.

## 2. Information Alibi does not collect
Alibi does not collect your email, your name, your device identifiers, the coordinates you simulate, the places you search for, the timing of your spoofs, crash reports, or anything else. Recents, favorites and presets are stored on your computer and never leave it.

## 3. Third parties the software talks to
- **Apple.** The developer disk image is personalised by Apple's signing server the first time it is mounted. Installing Alibi Mobile signs in to your Apple ID with Apple directly.
- **OpenStreetMap and OpenFreeMap.** Map tiles, place search and reverse geocoding. A search query is sent to Nominatim as a search query.
- **GitHub.** Downloads, updates and the developer image mirror.
- **Anisette relay.** Signing in with an Apple ID from a computer that is not a Mac needs device-attestation headers; like SideStore and iloader, Alibi fetches them from a public relay that never sees your password.
Each of these has its own privacy policy. None of them is operated by Alibi.

## 4. This website
These pages are static files on GitHub Pages with no analytics, no pixels and no cookies set by us. Fonts load from Google Fonts. The status page performs a few HTTPS requests from your browser to check that the services above are reachable.

## 5. Local logs
The desktop app writes logs on your computer to help diagnose setup problems. They stay on your machine unless you choose to paste them into an issue.

## 6. Children
Alibi is not directed to children.

## 7. Changes
If the software ever starts talking to something new, this page changes in the same commit.

## 8. Contact
[github.com/Nickkk66/alibi/issues](https://github.com/Nickkk66/alibi/issues)
""", updated="September 8, 2026", cta=False)

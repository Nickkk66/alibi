<p align="center">
  <img src="site/img/mark-180.png" width="88" alt="Alibi">
</p>

<h1 align="center">Alibi</h1>

<p align="center">
  Put your iPhone anywhere on Earth from your Mac. Every app believes it.<br>
  <a href="https://nickkk66.github.io/alibi/"><b>Website</b></a> ·
  <a href="https://nickkk66.github.io/alibi/docs/"><b>Docs</b></a> ·
  <a href="https://github.com/Nickkk66/alibi/releases/latest/download/Alibi.dmg"><b>Download for Mac</b></a>
</p>

<p align="center">
  <a href="https://github.com/Nickkk66/alibi/releases/latest"><img src="https://img.shields.io/github/v/release/Nickkk66/alibi?label=release&color=F2622E" alt="Latest release"></a>
  <img src="https://img.shields.io/badge/macOS-13%2B-111" alt="macOS 13+">
  <img src="https://img.shields.io/badge/iOS-17.4%2B-111" alt="iOS 17.4+">
  <img src="https://img.shields.io/badge/jailbreak-not%20needed-2ea44f" alt="No jailbreak">
</p>

<p align="center">
  <img src="site/img/docs/routes-moving.webp" width="820" alt="Alibi running a route: the live card with progress, the animated route line and the moving dot">
</p>

Alibi uses the location path Apple ships for developers, over a USB cable. Nothing on the phone is modified, nothing is jailbroken, and **Reset** puts real GPS back instantly. It works with every app that reads the phone's location: Find My, Maps, Life360, Snapchat, Instagram, Tinder, Pokémon GO and the rest.

<p align="center">
  <img src="site/img/apps/findmy.webp" width="44" alt="Find My">&nbsp;
  <img src="site/img/apps/applemaps.jpg" width="44" alt="Apple Maps">&nbsp;
  <img src="site/img/apps/googlemaps.jpg" width="44" alt="Google Maps">&nbsp;
  <img src="site/img/apps/life360.png" width="44" alt="Life360">&nbsp;
  <img src="site/img/apps/snapchat.webp" width="44" alt="Snapchat">&nbsp;
  <img src="site/img/apps/instagram-fill.png" width="44" alt="Instagram">&nbsp;
  <img src="site/img/apps/tinder.jpg" width="44" alt="Tinder">&nbsp;
  <img src="site/img/apps/bumble.jpg" width="44" alt="Bumble">&nbsp;
  <img src="site/img/apps/pokemongo.jpg" width="44" alt="Pokémon GO">&nbsp;
  <img src="site/img/apps/whatsapp.png" width="44" alt="WhatsApp">&nbsp;
  <img src="site/img/apps/bereal.webp" width="44" alt="BeReal">
</p>

## What it does

| | |
|---|---|
| <img src="site/img/docs/static-spoofing.webp" width="400" alt="Static mode: holding one spot"> | **Static.** Search a place, click the map or paste coordinates, press **Change Location**. Pick another place while it holds and Alibi asks *Move here?*. **Lock** keeps the location after you unplug. |
| <img src="site/img/docs/routes-setup.webp" width="400" alt="Routes mode: numbered stops with a leg speed under each"> | **Routes.** Numbered stops you can drag into order, up to ten waypoints, freehand drawing fitted to the roads, Walk / Cycle / Drive or **Auto** (each road's posted limit, lane changes on fast roads, pauses at corners). Preview the drive with a ghost marker before the phone moves. |
| <img src="site/img/docs/routes-stopped.webp" width="400" alt="A route on hold with Continue and Back"> | **Stop, Continue, Back.** Stop holds the phone where it is and keeps the rest of the route for **Continue**. **Back** returns to the planner with the phone staying put, so the next leg can start from here. |
| <img src="site/img/docs/style-satellite.webp" width="400" alt="Satellite style with 3D buildings"> | **Maps.** Dark, Satellite with 3D buildings, Matrix and Light. Find My-style dots that scale with the zoom, a blue dot for where you really are, an animated route line. |

More in the docs: [Setup iPhone](https://nickkk66.github.io/alibi/docs/setup-iphone/) · [Static Mode](https://nickkk66.github.io/alibi/docs/static-mode/) · [Routes Mode](https://nickkk66.github.io/alibi/docs/routes-mode/) · [Saved Locations](https://nickkk66.github.io/alibi/docs/bookmarks/) · [FAQ](https://nickkk66.github.io/alibi/docs/faq/)

## Alibi Mobile

<p align="center">
  <img src="site/img/mobile-mock-idle.webp" width="260" alt="Alibi Mobile, idle">&nbsp;&nbsp;
  <img src="site/img/mobile-mock-spoofing.webp" width="260" alt="Alibi Mobile, spoofing">
</p>

Install it once from the Mac with any Apple ID (**Install on iPhone**) and the phone changes its own location with no cable and no Mac around. It talks to itself through a loopback VPN, fetches the developer image on its own, and keeps working until the signature expires: a free Apple ID needs a re-sign every 7 days, which is one plug-in. [How it works and how to set it up.](https://nickkk66.github.io/alibi/docs/alibi-mobile/)

## Getting started

1. [Download Alibi for Mac](https://github.com/Nickkk66/alibi/releases/latest/download/Alibi.dmg), drag it to Applications and open it.
2. Plug the iPhone in with a data cable, unlock it and tap **Trust**. Turn on **Developer Mode** (Settings › Privacy & Security) and let the phone restart. **Setup** in the app walks through it.
3. Enter your access code. One code covers one Mac and one iPhone.
4. Pick a place and press **Change Location**.

Access codes are time-limited, checked against Alibi's licence server and bound to the devices that use them, so they cannot be shared or forged. Every licence can invite three friends for three weeks each. [Get a code on the website.](https://nickkk66.github.io/alibi/#pricing)

## This repository

The website under `site/` (plain HTML, CSS and JavaScript, published to GitHub Pages on every push) and the release builds: `Alibi.dmg` for the Mac and `AlibiMobile.ipa` for the phone. The app source is not published here.

## Reporting a problem

[Open an issue](https://github.com/Nickkk66/alibi/issues) with the text from Settings › Phone › **Copy diagnostics**. It holds the phone's state and the last fifty log lines, nothing personal.

import { chromium } from "playwright";
const browser = await chromium.launch({ args: ["--use-gl=angle", "--use-angle=swiftshader", "--ignore-gpu-blocklist"] });
const page = await browser.newPage({ viewport: { width: 590, height: 1280 }, deviceScaleFactor: 1 });
await page.goto("file://" + process.cwd() + "/tools/phone.html");
await page.waitForFunction(() => window.__ready, null, { timeout: 60000 });
for (let i = 0; i < 40; i++) { if (await page.evaluate(() => map.areTilesLoaded() && map.loaded())) break; await page.waitForTimeout(500); }
await page.waitForTimeout(1500);
await page.screenshot({ path: process.argv[2] });
await browser.close(); console.log("wrote", process.argv[2]);

"""
build.py  –  Generates a standalone index.html
Drop index.html + TitleScreen.png + images/ folder anywhere and open in a browser.
"""

import json
import re
import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ── 1. Pull game data from app.py ────────────────────────────────────────────
sys.path.insert(0, ROOT)
from app import STORIES, EVENTS, CRISIS_EVENTS, ENDINGS, AFTERMATHS

GAME_DATA = {
    "stories":      STORIES,
    "events":       EVENTS,
    "crisis_events": CRISIS_EVENTS,
    "endings":      ENDINGS,
    "aftermaths":   AFTERMATHS,
}

# ── 2. Read CSS and fix asset paths for standalone use ───────────────────────
with open(os.path.join(ROOT, "static", "style.css"), "r") as f:
    css = f.read()

# /static/TitleScreen.png  →  TitleScreen.png
css = css.replace("url('/static/TitleScreen.png')", "url('TitleScreen.png')")
css = css.replace('url("/static/TitleScreen.png")', 'url("TitleScreen.png")')

# ── 3. Read game.js and fix asset paths ──────────────────────────────────────
with open(os.path.join(ROOT, "static", "game.js"), "r") as f:
    js = f.read()

# /static/images/${imageId}.png  →  images/${imageId}.png
js = js.replace("src=\"/static/images/", "src=\"images/")
js = js.replace("src='/static/images/", "src='images/")

# ── 4. Assemble the standalone HTML ──────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Dragon Ball Legacy Rewritten</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap" rel="stylesheet" />
  <style>
{css}
  </style>
</head>
<body>

  <!-- ══════════════════════════════════════════════════════════
       SCREEN: HOME  –  Story selection
  ══════════════════════════════════════════════════════════════ -->
  <div id="screen-home" class="screen active">
    <div class="home-logo">
      <div class="logo-badge">Interactive Story · Age 749</div>
      <h1>DRAGON BALL <span>LEGACY</span></h1>
      <p class="subtitle-pixel">Legacy Rewritten</p>
      <p class="tagline">Four paths. Three fates. One unanswered question.</p>
      <div class="divergence">
        <strong>The Divergence Point:</strong><br>
        In the original story, a head injury altered
        Kakarot's memory and allowed him to grow up as a hero. That accident never happened.
        His battle programming remains intact. What he becomes is entirely up to you.
      </div>
    </div>

    <p class="press-start"><span class="db-dot">★</span> SELECT YOUR ORIGIN <span class="db-dot">★</span></p>
    <div class="story-grid" id="story-grid">
      <!-- Populated by game.js -->
    </div>
  </div>


  <!-- ══════════════════════════════════════════════════════════
       SCREEN: GAME  –  Active gameplay
  ══════════════════════════════════════════════════════════════ -->
  <div id="screen-game" class="screen">

    <!-- ── Stats Header ─────────────────────────────────────── -->
    <header id="stats-header">
      <div class="header-brand" id="header-brand">DRAGON BALL <span>LEGACY</span></div>
      <div class="header-divider"></div>

      <div class="stats-row">
        <!-- Ki -->
        <div class="stat-block">
          <span class="stat-label-sm" style="color:var(--ki)">Ki</span>
          <div class="stat-bar-wrap">
            <div class="stat-bar-fill ki" id="fill-ki" style="width:0%"></div>
          </div>
          <span class="stat-val-sm" id="val-ki">0</span>
        </div>

        <!-- Malice -->
        <div class="stat-block">
          <span class="stat-label-sm" style="color:var(--malice)">Malice</span>
          <div class="stat-bar-wrap">
            <div class="stat-bar-fill malice" id="fill-malice" style="width:0%"></div>
          </div>
          <span class="stat-val-sm" id="val-malice">0</span>
        </div>

        <!-- Infamy -->
        <div class="stat-block">
          <span class="stat-label-sm" style="color:var(--infamy)">Infamy</span>
          <div class="stat-bar-wrap">
            <div class="stat-bar-fill infamy" id="fill-infamy" style="width:0%"></div>
          </div>
          <span class="stat-val-sm" id="val-infamy">0</span>
        </div>

        <!-- Health -->
        <div class="stat-block">
          <span class="stat-label-sm" style="color:var(--health)">Health</span>
          <div class="stat-bar-wrap">
            <div class="stat-bar-fill health" id="fill-health" style="width:0%"></div>
          </div>
          <span class="stat-val-sm" id="val-health">0</span>
        </div>
      </div>

      <div class="header-divider"></div>
      <button class="header-back-btn" id="back-to-home">&#8592; Stories</button>
    </header>

    <!-- ── Main Body ─────────────────────────────────────────── -->
    <div id="game-body">

      <!-- Timeline Sidebar -->
      <nav id="timeline-sidebar">
        <div class="timeline-header">Timeline</div>
        <div id="timeline-list"></div>
      </nav>

      <!-- Scene Panel -->
      <main id="scene-panel">
        <!-- Populated by game.js -->
      </main>

    </div>

    <!-- Progress Rail -->
    <div id="progress-rail">
      <!-- Populated by game.js -->
    </div>

  </div><!-- /screen-game -->


  <!-- ── Inlined Game Data ──────────────────────────────────── -->
  <script>
    window.GAME_DATA = {json.dumps(GAME_DATA, ensure_ascii=False, indent=2)};
  </script>

  <!-- ── Inlined Game Engine ───────────────────────────────── -->
  <script>
{js}
  </script>

</body>
</html>"""

# ── 5. Write output ───────────────────────────────────────────────────────────
out_path = os.path.join(ROOT, "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

size_kb = os.path.getsize(out_path) / 1024
print(f"Built:  index.html  ({size_kb:.1f} KB)")
print()
print("To play:")
print("  1. Open index.html in any browser — no server needed.")
print("  2. Keep TitleScreen.png in the same folder as index.html.")
print("  3. Put scene images in an images/ subfolder next to index.html.")
print()
print("To redeploy to a website:")
print("  Upload index.html + TitleScreen.png + images/ to any static host")
print("  (GitHub Pages, Netlify, Vercel, Cloudflare Pages, etc.)")

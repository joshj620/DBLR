# Dragon Ball Legacy Rewritten

Dragon Ball Legacy Rewritten is a browser-based interactive story game where you guide an alternate-timeline Kakarot through branching choices, changing stats, alignment paths, and endings.

The game is built as a choice-driven narrative engine with a retro pixel-art presentation. Every run starts from one of four origin stories and branches into multiple outcomes, including secret endings unlocked through hidden Dragon Ball collection.

## What This Project Includes

- A playable web UI for story selection and gameplay
- Branching story content (origins, prologue, bridge, crisis, endings, aftermaths)
- Stat-based progression (Ki, Malice, Infamy, Health)
- Secret Dragon Ball hunt and wish route unlocks
- A Flask app to serve the game locally
- Standalone/exported HTML versions for static hosting and sharing

## Tech Stack

- Python 3
- Flask
- HTML5
- CSS3
- Vanilla JavaScript (no frontend framework)
- JSON data model for story and event content

## Key Files

- `app.py`: Flask entry point and local web server setup
- `index.html`: Main game page template used by Flask
- `game.js`: Core game engine and state machine
- `style.css`: Game styling and responsive layout
- `game_data.json`: Narrative content, events, choices, and Dragon Ball definitions
- `Dragon Ball Legacy Rewritten (2).html`: Exported standalone build with inlined assets/data

## How the Game Works

### 1) State-driven story flow

The game engine keeps runtime state in JavaScript:

- Current story and event queue
- Current event position
- Player stats
- Derived alignment and ending path
- Timeline/history log
- Dragon Ball reveal/collection progress

The high-level sequence is:

1. Home/origin selection
2. Intro and origin event
3. Prologue choice
4. Bridge choice
5. Alignment reveal
6. Crisis event
7. Ending
8. Aftermath

### 2) Content is data-first

Most narrative logic is data-driven through `game_data.json`:

- Story definitions (id, title, starting stats, sequence)
- Event payloads (text, image id, type, choices)
- Crisis events by alignment path
- Endings and aftermaths
- Dragon Ball metadata (screen, visibility mode, triggers)

The engine reads this data and renders cards/buttons dynamically rather than hardcoding each scene.

### 3) Choice handling and branching

When a player picks a choice, the engine:

1. Applies stat changes
2. Appends timeline log entries
3. Updates path/alignment when needed
4. Advances to the next event

Special nodes (`__alignment__`, `__crisis__`, `__ending__`, `__aftermath__`) are resolved at runtime based on current game state.

### 4) Dragon Ball secret system

Dragon Balls appear across home/game screens based on their definitions.

- Visible balls appear in expected progression points
- Hidden balls are revealed by triggers and can now fade in/out in timed intervals
- Revealed hidden balls respawn in random screen positions on each cycle
- Collecting all seven unlocks secret wish options during crisis

## Running Locally

### Option A: Flask (recommended)

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
python app.py
```

4. Open:

```text
http://127.0.0.1:5000
```

### Option B: Standalone HTML

Open `Dragon Ball Legacy Rewritten (2).html` directly in a browser.

Note: local file mode can have browser restrictions for some asset-loading scenarios. Flask is the most reliable way to run and test changes.

## Editing and Extending

- Add or adjust story content in `game_data.json`
- Update rendering/flow logic in `game.js`
- Tweak visual style and animations in `style.css`
- Use `index.html` for Flask-served page structure

If you add new scenes/images, place image assets under `images/` and reference them by `image_id` in the data.

## Project Goal

This project aims to blend narrative branching, timeline-style progression, and lightweight game mechanics into a fast, replayable Dragon Ball alternate-history experience.
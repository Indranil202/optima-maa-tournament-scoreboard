#!/usr/bin/env python3
"""
Auto-generate gallery.json by scanning assets/Gallery/ subfolders.
Run from the repo root:  python gen_gallery.py
"""
import os, json

GALLERY_DIR = os.path.join("assets", "Gallery")

ICON_MAP = {
    "table tennis": "fa-table-tennis-paddle-ball",
    "badminton": "fa-shuttlecock",
    "chess": "fa-chess",
    "carrom": "fa-bullseye",
    "8 ball pool": "fa-circle",
    "foosball": "fa-gamepad",
    "football": "fa-futbol",
    "basketball": "fa-basketball",
    "volleyball": "fa-volleyball",
    "throwball": "fa-volleyball",
    "cricket": "fa-cricket-bat-ball",
    "fifa fc25": "fa-gamepad",
    "mortal combat": "fa-hand-fist",
    "pubg": "fa-crosshairs",
    "general": "fa-camera",
}

MEDIA_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".mp4", ".webm", ".mov", ".avi", ".mkv"}

def scan():
    games = []
    for folder in sorted(os.listdir(GALLERY_DIR)):
        folder_path = os.path.join(GALLERY_DIR, folder)
        if not os.path.isdir(folder_path):
            continue
        files = sorted([
            f for f in os.listdir(folder_path)
            if os.path.splitext(f)[1].lower() in MEDIA_EXT
        ])
        icon = ICON_MAP.get(folder.lower(), "fa-image")
        games.append({
            "name": folder,
            "folder": folder,
            "icon": icon,
            "photos": files
        })
    return games

def main():
    games = scan()
    total = sum(len(g["photos"]) for g in games)
    with_media = sum(1 for g in games if g["photos"])

    out = {"games": games}
    out_path = os.path.join(GALLERY_DIR, "gallery.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"✅ gallery.json updated: {len(games)} games, {total} files, {with_media} with media")

if __name__ == "__main__":
    main()

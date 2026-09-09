# HoK: ACE — Unofficial English Translations

**Fan-made English translations of official Honor of Kings: ACE content. This project is not affiliated with or endorsed by Tencent or TiMi Studio Group.**

- **Public site:** https://lani27.github.io/hok-ace/
- **Launch & Rewards Preview:** https://lani27.github.io/hok-ace/announcements/launch-rewards.html
- **Beginner Guide:** https://lani27.github.io/hok-ace/guides/beginner-guide.html
- **Official Chinese website:** https://wxq.qq.com/
- **Official English website:** https://honorofkingsace.com/

## Repository layout

```text
docs/                     Public GitHub Pages files
  index.html              Translation index
  announcements/          Translated announcement pages
  guides/                 Translated interactive guides
  assets/launch/          English images for the launch announcement
  assets/beginner-guide/   Localized beginner-guide artwork
    keyword-videos/       Short MP4 demonstrations with burned-in English subtitles
english-patch/            Reserved for English Patch files
  translations/           Future patch translation data
templates/                Shared unofficial banner and index source
tools/build_launch_page.py  Launch article source and site builder
```

GitHub Pages publishes `docs/` from `main`. Future changes pushed to that folder
are published automatically. The patch folder is public in the repository, but
is separate from the Pages publishing directory.

## Update the pages

Edit `tools/build_launch_page.py` for the launch article, `templates/index.html`
for the index, or `templates/unofficial-banner.html` for the shared top banner.
Then run:

```sh
python tools/build_launch_page.py
python tools/build_beginner_guide.py
```

Commit the source changes and regenerated `docs/` pages together. New translated
pages must use the same prominent unofficial banner and official-site links.

The beginner guide uses `tools/beginner_content.py` and
`tools/beginner_lineups.py` for translated text, with its CSS and JavaScript in
`templates/beginner-guide.*`. Its builder requires only Python's standard library.

## Translation notes

The first page translates the supplied Tencent Camp Chinese-server launch
announcement. It is not a global-release announcement. Dates and amounts are
preserved; differences between source graphics and article text are explained
in the article. Unverified cosmetic names use descriptive English translations.

All 17 content images were localized with the built-in ImageGen editor, preserving
the overall original artwork and matching text styling. Small artwork and fine-text
differences may remain. Original game content and artwork belong to their
respective owners; their inclusion does not grant a license to those assets.

The beginner guide translates the [official September 2026 guide](https://wxq.qq.com/cp/a202609xszy/index.html),
including 21 rule slides, five starter lineups, five tacticians, 13 keywords,
and 12 expert-video listings. Its 52 images containing text were localized with
ImageGen; original portraits, skill icons, and the background are retained.
Selectable English text, including all 35 featured hero-card effects, accompanies
the lineup diagrams. Small labels in the AI-edited artwork can remain imperfect;
the text guide is the reference for precise names and effects. The 13 keyword
demonstrations have separate English-subtitled MP4 versions alongside their
original Chinese links. Subtitles translate the narration; the Chinese audio
and game interface are retained. Other linked videos remain in Chinese.
The official Tencent SuperPlayer script loads only when a video is selected;
video playback needs an internet connection. The page includes an official-source
fallback link if the player cannot load.
Lineup codes are preserved exactly from the official page; importing them in
the game has not been tested. This is a Chinese-server snapshot, so game updates
and international-release terminology may differ.

### Keyword video subtitles

The short dictionary clips were transcribed with Whisper large-v3-turbo, then
translated and checked against the source captions, including hero-name corrections.
Edit the timed English copy in `tools/keyword_subtitles.json`. Keep original
720p clips outside the repository, named `deploy.mp4`, `fleeting.mp4`, etc.
Their Tencent video IDs are listed in `KEYWORDS` in `tools/beginner_content.py`.
To rebuild with FFmpeg and FFprobe installed:

```sh
python tools/build_keyword_videos.py --originals /path/to/originals
python tools/build_beginner_guide.py
```

The renderer produces MP4s and English SRT files in
`docs/assets/beginner-guide/keyword-videos/`. Subtitles are burned into the video
over the original narration captions, with an unofficial translation label.
The website loads a clip only when selected, using the browser's video player.
Original Chinese demonstrations remain available in the Tencent player.

## English Patch

See [english-patch/](english-patch/). No patch binaries or translation payloads
have been uploaded yet.

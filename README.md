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
the text guide is the reference for precise names and effects. Linked videos keep
their original Chinese audio and on-screen text and are labeled accordingly.
The official Tencent SuperPlayer script loads only when a video is selected;
video playback needs an internet connection. The page includes an official-source
fallback link if the player cannot load.
Lineup codes are preserved exactly from the official page; importing them in
the game has not been tested. This is a Chinese-server snapshot, so game updates
and international-release terminology may differ.

## English Patch

See [english-patch/](english-patch/). No patch binaries or translation payloads
have been uploaded yet.

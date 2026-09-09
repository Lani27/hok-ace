# HoK: ACE — Unofficial English Translations

**Fan-made English translations of official Honor of Kings: ACE content. This project is not affiliated with or endorsed by Tencent or TiMi Studio Group.**

- **Public site:** https://lani27.github.io/hok-ace/
- **Launch & Rewards Preview:** https://lani27.github.io/hok-ace/announcements/launch-rewards.html
- **Official Chinese website:** https://wxq.qq.com/
- **Official English website:** https://honorofkingsace.com/

## Repository layout

```text
docs/                     Public GitHub Pages files
  index.html              Translation index
  announcements/          Translated announcement pages
  assets/launch/          English images for the launch announcement
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
```

Commit the source changes and regenerated `docs/` pages together. New translated
pages must use the same prominent unofficial banner and official-site links.

## Translation notes

The first page translates the supplied Tencent Camp Chinese-server launch
announcement. It is not a global-release announcement. Dates and amounts are
preserved; differences between source graphics and article text are explained
in the article. Unverified cosmetic names use descriptive English translations.

All 17 content images were localized with the built-in ImageGen editor, preserving
the overall original artwork and matching text styling. Small artwork and fine-text
differences may remain. Original game content and artwork belong to their
respective owners; their inclusion does not grant a license to those assets.

## English Patch

See [english-patch/](english-patch/). No patch binaries or translation payloads
have been uploaded yet.

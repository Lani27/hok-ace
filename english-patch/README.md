# Honor of Kings: Ace English Patch

Unofficial English patch for the Chinese game client.

## Current release: 1.4.11

| Method | Download |
|---|---|
| Windows PC | [Windows patcher](https://github.com/Lani27/hok-ace/releases/download/v1.4.11/HOK-Ace-English-Patcher-1.4.11.exe) |
| Android connected to a Windows PC by USB | Use the same Windows executable and choose Android phone (USB) |
| Android on-phone with Shizuku | [Signed 1.4.11-preview APK](https://github.com/Lani27/hok-ace/releases/download/v1.4.11/HOK-Ace-English-Patcher-1.4.11-preview.apk) |

[Release notes and all files](https://github.com/Lani27/hok-ace/releases/tag/v1.4.11) · [SHA-256 checksums](https://github.com/Lani27/hok-ace/releases/download/v1.4.11/SHA256SUMS.txt)

## Setup and updating

- [Windows PC and Android USB guide](https://github.com/Lani27/hok-ace/releases/download/v1.4.11/WINDOWS-USB-GUIDE.md).
- [Android Shizuku guide](https://github.com/Lani27/hok-ace/releases/download/v1.4.11/ANDROID-SHIZUKU-GUIDE.md).

Close the game before patching. Windows and USB users should use the new EXE.
For Shizuku, install the APK over the existing patcher and keep its app data.
Start Shizuku, open the patcher and tap **Patch / Continue**. Complete
**Recover & clean up** first if the app reports pending recovery.

## What changed

The Windows/USB worker refreshes certifi to 2026.10.23 and excludes the distrusted
emSign G3 root. The signed Shizuku refresh retains the previous publisher identity,
the localization-ID repair and the Qts tree-growth fixes. Its embedded engine
does not contain the affected certifi or Brotli packages.

Both downloads use the verified October 22 translation catalog (data 1.4.10).
The phone data was verified against the saved 1.6.1 downloaded-package fixture;
later client changes and unfamiliar content are preserved or reported. The
Shizuku APK remains a preview; this exact build has not been installed on a live
phone or tested in gameplay. Verification details are included with the release.

The translations folder remains reserved for future separately published data.
This folder is separate from the GitHub Pages content under `docs/`.

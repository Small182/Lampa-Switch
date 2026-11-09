# Lampa for Nintendo Switch

Experimental standalone Lampa launcher based on [Chromium NX](https://github.com/shodowlo/chromium-nx).

Target: open `http://lampa.mx/` in fullscreen, with no startup text console. Diagnostic output remains on the SD card.

## Build

Open **Actions → Build Lampa Switch → Run workflow**. Once the job succeeds, download `Lampa-Switch` from its artifacts. The archive contains `Lampa.nro` and Chromium's Linux image. Do **not** copy only the NRO: the browser requires the image.

The workflow compiles from source in Debian and devkitPro containers, and can take a long time. It is an experimental build until tested on a real Switch.

## Install

Extract the contents of the archive into `/switch/lampa-switch/` on the SD card. Run `Lampa.nro` through an application/forwarder with an appropriate 39-bit address space (as Chromium NX requires).

## Upstream

Chromium NX is an independent experimental project; this repository adds Lampa-specific launch behavior. See the upstream license and credits.

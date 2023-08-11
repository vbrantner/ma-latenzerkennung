from pyzbar.pyzbar import decode
from PIL import Image

with Image.open('./split_images/split_16_1.png') as img:
    results = decode(img)
    print(results)

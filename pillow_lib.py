from PIL import Image
filename = "buildings.jpg"
with Image.open(filename) as img:
    img.load()

print(type(img))
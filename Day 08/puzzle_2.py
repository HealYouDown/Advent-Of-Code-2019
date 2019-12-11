from PIL import Image

with open("Day 8/input.txt", "r") as f:
    data = f.readline()

MAX_WIDTH = 25
MAX_HEIGHT = 6

layers = []

number_of_layers = len(data) // (MAX_WIDTH * MAX_HEIGHT)
digits_per_layer = len(data) // number_of_layers

for i in range(number_of_layers):
    rows = []
    layer_digits = data[i*digits_per_layer : i*digits_per_layer + digits_per_layer]

    for k in range(MAX_HEIGHT):
        rows.append(layer_digits[k*MAX_WIDTH : k*MAX_WIDTH + MAX_WIDTH])
    
    layers.append(rows)

# Decode image
colors = {
    "0": (0, 0, 0, 255),
    "1": (255, 255, 255, 255),
    "2": (255, 255, 255, 0)
}

def create_layer_image(layer):
    img = Image.new("RGBA", (MAX_WIDTH, MAX_HEIGHT))
    for y, seq in enumerate(layer):
        x = 0
        for char in seq:
            img.putpixel((x, y), colors[char])
            x += 1
    return img

layers_as_images = [create_layer_image(layer) for layer in layers]

decoded_image = Image.new("RGBA", (MAX_WIDTH, MAX_HEIGHT))
for img in reversed(layers_as_images):
    decoded_image.paste(img, (0, 0), img)

decoded_image.show()

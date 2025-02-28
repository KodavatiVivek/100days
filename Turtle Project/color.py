import colorgram as c

colors = c.extract('image.jpg', 30)
rgb_colors = []
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))


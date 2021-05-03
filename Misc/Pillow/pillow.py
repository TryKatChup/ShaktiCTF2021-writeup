from PIL import Image
flag = Image.new('RGB', (600, 500))
k = 0
for row in range (0,60):
    for col in range (0,50):
        k += 1
        cur_image = Image.open('{}.jpg'.format(k))
        flag.paste(cur_image, (row * 10, col * 10))

flag.save("flag_pillow.jpg", "JPEG")


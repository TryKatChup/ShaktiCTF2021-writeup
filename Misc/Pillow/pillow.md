# Pillow

The challenge has a zip file which contains 3000 images in a folder called  `60x50`.
This is a hint that suggests us to merge all images in one in a `60x50` grid.

The title of the challenge refers to Pillow Python library (`PIL`), which is useful when we have to manipulate images.

```python
from PIL import Image
flag = Image.new('RGB', (600, 500))
k = 0
for row in range (0,60):
    for col in range (0,50):
        k += 1
        cur_image = Image.open('{}.jpg'.format(k))
        flag.paste(cur_image, (row * 10, col * 10))

flag.save("flag_pillow.jpg", "JPEG")
```

Finally we obtain the flag in a `600x500` JPEG file :
![](flag_pillow.jpg)

`shaktictf{pill0w_l1k3_a_g00d_c0nscience}`

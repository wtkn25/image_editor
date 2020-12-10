import glob
import os
import random
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 引数: 1行目のテキスト 2行目のテキスト
# ランダムにベース画像を用意
# 透明な背景を描画

# コマンドライン引数を受け取る
texts = []
texts.append(sys.argv[1])
texts.append(sys.argv[2])

# ランダムにベース画像を用意
image_dir = os.path.join(os.getcwd(), "base_png_images")
image_list = glob.glob(os.path.join(image_dir, "*.png"))
base_image = random.choice(image_list)

# pillowを使う
im = Image.open(base_image)
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("/Library/Fonts/LightNovelPOPv2.otf", size=80)

# テキスト用枠の用意
layer1 = Image.new("RGBA", im.size, color=0)
layer1_d = ImageDraw.Draw(layer1)
margin = 150
layer1_d.rectangle(
    [(0, margin), (im.size[0], im.size[1] - margin)], fill=(255, 255, 255, 192)
)

# ベース画像とテキスト枠の合成
result = Image.alpha_composite(im, layer1)
draw = ImageDraw.Draw(result)

for i, text in enumerate(texts):
    pos = []
    pos.insert(0, (im.size[0] - font.getsize(text)[0]) / 2)
    pos.insert(
        1,
        (
            im.size[1]
            - font.getsize(text)[1] * len(texts)
            + i * 2 * font.getsize(text)[1]
        )
        / 2,
    )
    pos = tuple(pos)
    bw = 4
    color = "yellow"
    draw.text(np.array(pos) - (-bw, -bw), text, color, font=font)
    draw.text(np.array(pos) - (-bw, +bw), text, color, font=font)
    draw.text(np.array(pos) - (+bw, -bw), text, color, font=font)
    draw.text(np.array(pos) - (+bw, +bw), text, color, font=font)
    draw.text(pos, text, (0, 0, 0), font=font)

result = result.convert("RGB")
result.save("./image_export/" + "".join(texts) + ".jpg", quality=70)

# result.show()

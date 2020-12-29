import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

from settings import BAR_COLOR

# コマンドライン引数の受け取り
icon_name = sys.argv[1] if len(sys.argv) > 1 else "python"
upper_title = sys.argv[2] if len(sys.argv) > 2 else "VSCode"
lower_title = sys.argv[3] if len(sys.argv) > 3 else "日本語化の方法"
bar_color = sys.argv[4] if len(sys.argv) > 4 else "yellow"
title = "\n".join([upper_title, lower_title])

# ベース画像を用意
base_im = Image.open("materials/base_images/bg.png")
base_im_draw = ImageDraw.Draw(base_im)

# アイコンの下敷き用の画像を用意
icon_bg = Image.new("RGBA", (250, 250), (255, 255, 255))

# 使用するアイコンを用意
icon_path = os.path.join("materials/icons", f"{icon_name}.png")
icon_im = Image.open(icon_path).resize((200, 200))
icon_im_base_clear = Image.new("RGBA", icon_bg.size)

paste_start_pos = tuple((np.array(icon_bg.size) - np.array(icon_im.size)) // 2)
icon_im_base_clear.paste(icon_im, paste_start_pos)

# アイコンとアイコン用背景画像の合成
icon_im_with_bg = Image.alpha_composite(icon_bg, icon_im_base_clear)
base_im.paste(icon_im_with_bg, (45, 0))

# テキストを描画
font = ImageFont.truetype("/System/Library/Fonts/ヒラギノ角ゴシック W8.ttc", 100)

base_im_draw.text((60, 350), title, spacing=40, font=font)

# テキスト下のバーを表示
bar_bellow_the_text = Image.new("RGBA", (1000, 25), BAR_COLOR[bar_color])
base_im.paste(bar_bellow_the_text, (45, 630))

base_im.save(f"image_export/{upper_title+lower_title}.png")

base_im_jpg = base_im.convert("RGB").resize((1024, 576))
base_im_jpg.save(f"image_export/{upper_title+lower_title}.jpg")

# saved_png = Image.open(f"image_export/{upper_title+lower_title}.png")
# saved_png.save(f"image_export/{upper_title+lower_title}.jpg", "JPEG")

import numpy as np
from PIL import Image, ImageDraw, ImageFont

im = Image.open('IMG_4202.png')

# デフォルトのプレビューソフトで開く
# im.show()

# 形式　サイズ RGBAとか出た
# print(im.format, im.size, im.mode)


# 今回の主目的はテキストの描画
text = 'こんにちは世界'
draw = ImageDraw.Draw(im)
draw.font = ImageFont.truetype('/Library/Fonts/LightNovelPOPv2.otf', size=500)
pos = (np.array(im.size) - np.array(draw.font.getsize(text))) / 2.
draw.text(pos, text, (255, 0, 0))

im.save('pillow_iamge_draw_huchidori.png', quality=95)

im.show()

# 縁取りに成功したやつ

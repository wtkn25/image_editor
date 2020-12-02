import numpy as np
from PIL import Image, ImageDraw, ImageFont

im = Image.open('候補3.png')

# デフォルトのプレビューソフトで開く
# im.show()

# 形式　サイズ RGBAとか出た
# print(im.format, im.size, im.mode)


# 今回の主目的はテキストの描画
text = 'こんにちは世界'
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('/Library/Fonts/LightNovelPOPv2.otf', size=30)
pos = (np.array(im.size) - np.array(font.getsize(text))) / 2.
# bw = 1
# draw.text(pos-(-bw, -bw), text, 'yellow', font=font)
# draw.text(pos-(-bw, +bw), text, 'yellow', font=font)
# draw.text(pos-(+bw, -bw), text, 'yellow', font=font)
# draw.text(pos-(+bw, +bw), text, 'yellow', font=font)
draw.text(pos, text, (255, 0, 0), font=font)


layer1 = Image.new('RGBA', im.size, color=0)
layer1_d = ImageDraw.Draw(layer1)
layer1_d.rectangle([(145, 20), (535, 370)], fill=(255, 255, 0, 128))

result = Image.alpha_composite(im, layer1)
result.save('pillow_iamge_draw_3.png', quality=95)

result.show()

# 画像の前にボックスを用意できたやつ

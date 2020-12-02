import numpy as np
from PIL import Image, ImageDraw, ImageFont

# ベース画像の用意
bgimage = '候補4.png'
im = Image.open(bgimage)

# テキスト用枠の用意
layer1 = Image.new('RGBA', im.size, color=0)
layer1_d = ImageDraw.Draw(layer1)
layer1_d.rectangle([(145, 40), (535, 350)], fill=(255, 255, 128,))

# ベース画像とテキスト枠の合成
result = Image.alpha_composite(im, layer1)
draw = ImageDraw.Draw(result)

# テキストの用意
text1 = 'Python'
text2 = '文字列の操作'
text3 = '大文字・小文字変換'
texts = [text1, text2, text3]

#　テキスト描画の初期位置を計算
font = ImageFont.truetype('/Library/Fonts/LightNovelPOPv2.otf', size=40)
# textsize = font.getsize(text1)
# textsize = (textsize[0], textsize[1]*len(texts))
# pos = (np.array(im.size) - np.array(textsize)) / 2

for i, text in enumerate(texts):
    pos = []
    pos.insert(0, (im.size[0] - font.getsize(text)[0]) / 2)
    pos.insert(1, (im.size[1] - font.getsize(text)[1] *
                   len(texts) + i*2*font.getsize(text)[1]) / 2)
    pos = tuple(pos)
    bw = 1
    color = 'white'
    draw.text(np.array(pos)-(-bw, -bw), text, color, font=font)
    draw.text(np.array(pos)-(-bw, +bw), text, color, font=font)
    draw.text(np.array(pos)-(+bw, -bw), text, color, font=font)
    draw.text(np.array(pos)-(+bw, +bw), text, color, font=font)
    draw.text(pos, text, (0, 0, 0), font=font)


result.save('pillow_iamge_draw_3.png', quality=95)

result.show()

# 画像の前にボックスを用意できたやつ

from PIL import Image, ImageDraw, ImageFont

im = Image.open('IMG_4202.png')

# デフォルトのプレビューソフトで開く
# im.show()

# 形式　サイズ RGBAとか出た
# print(im.format, im.size, im.mode)


# 今回の主目的はテキストの描画
draw = ImageDraw.Draw(im)
font = ImageFont.truetype('/Library/Fonts/LightNovelPOPv2.otf', size=500)
draw.multiline_text((0, 0), 'こんにちは', fill=(255, 0, 0), font=font)

im.save('pillow_iamge_draw.png', quality=95)

im.show()

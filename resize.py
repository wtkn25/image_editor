from PIL import Image

im = Image.open("sample.png")


resized_im = im.resize(size=(128, 72))

resized_im.save("resized_sample.png")

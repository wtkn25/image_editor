from PIL import Image, ImageDraw

rect = Image.new("RGBA", (1280, 720), (0, 0, 255))

rect_d = ImageDraw.Draw(rect)
rect_d.rectangle(
    [(200, 100), (500, 300)], fill=(255, 0, 0), outline=(0, 255, 0), width=10
)

rect.show()
rect.save("sample.png")

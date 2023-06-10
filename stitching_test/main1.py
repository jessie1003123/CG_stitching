from PIL import Image

img = []
for i in range(9):
    img.append(Image.open("rocket_{}_pred.png".format(i)))


blendImg = Image.blend(img[0], img[1], alpha = 0.99)
blendImg.save("output.png")

output = Image.open("output.png")
for i in range(2,9):
    blendImg1 = Image.blend(output, img[i], alpha = 0.99)
    blendImg1.save("output.png")

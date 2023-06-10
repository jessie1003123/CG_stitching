from PIL import Image

img0 = Image.open("rocket_0_pred.png")
img1 = Image.open("rocket_1_pred.png")
img2 = Image.open("rocket_2_pred.png")
img3 = Image.open("rocket_3_pred.png")
img4 = Image.open("rocket_4_pred.png")
img5 = Image.open("rocket_5_pred.png")
img6 = Image.open("rocket_6_pred.png")
img7 = Image.open("rocket_7_pred.png")
img8 = Image.open("rocket_8_pred.png")
img9 = Image.open("rocket_9_pred.png")

blendImg1 = Image.blend(img0, img1, alpha = 0.5)
blendImg2 = Image.blend(img2, blendImg1, alpha = 0.5)
blendImg3 = Image.blend(img3, blendImg2, alpha = 0.5)
blendImg4 = Image.blend(img4, blendImg3, alpha = 0.5)
blendImg5 = Image.blend(img5, blendImg4, alpha = 0.5)
blendImg6 = Image.blend(img6, blendImg5, alpha = 0.5)
blendImg7 = Image.blend(img7, blendImg6, alpha = 0.5)
blendImg8 = Image.blend(img8, blendImg7, alpha = 0.5)
blendImg9 = Image.blend(img9, blendImg8, alpha = 0.5)
    
blendImg9.save("output.jpg")

blend = Image.blend(img1,img7,alpha = 0.5)
blend.save("my_output.png")


#print(img1.size)
#print(img2.size)

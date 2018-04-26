from PIL import Image, ImageFont, ImageDraw

img = Image.open('standard.png')

draw = ImageDraw.Draw(img)
font = ImageFont.load('arial.pil')
draw.text((0,0), 'Standard', (255,255,255), font=font)
#draw.text((0,0), 'Standard', (255,255,255))

img.show()
#img.save('standard_formatted.png')

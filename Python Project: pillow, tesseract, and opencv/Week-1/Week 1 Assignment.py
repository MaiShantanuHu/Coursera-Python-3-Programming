import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw
from PIL import ImageFont
# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')
font=ImageFont.truetype(r'readonly/fanwood-webfont.ttf', 70)
# build a list of 9 images which have different brightnesses
newimage=PIL.Image.new(image.mode, (image.width, image.height+70))
newimage.paste(image, (0,0))
images=[]
for i in range(1,10):
if i%3==1:
intensity=0.1
elif i%3==2:
intensity=0.5
elif i%3==0:
intensity=0.9
if i<=3:
channel=0
elif i<=6:
channel=1
else:
channel=2
new_image=newimage.copy()
text="channel {} intensity {}".format(channel, intensity)
ImageDraw.Draw(new_image).text((0, new_image.height-70), text, font=font, align='left')
r,g,b=new_image.split()
if channel==0:
r=r.point(lambda x: x*intensity)
elif channel==1:
g=g.point(lambda x: x*intensity)
elif channel==2:
b=b.point(lambda x: x*intensity)
result=Image.merge('RGB', (r,g,b))
images.append(result)
# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0
for img in images:
# Lets paste the current image into the contact sheet
contact_sheet.paste(img, (x, y) )
# Now we update our X position. If it is going to be the width of the image, then we set it to 0
# and update Y as well to point to the next "line" of the contact sheet.
if x+first_image.width == contact_sheet.width:
x=0
y=y+first_image.height
else:
x=x+first_image.width
# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)    

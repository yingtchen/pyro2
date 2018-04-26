import matplotlib.image as img
import matplotlib.pyplot as plt
from read_files import read

images = read() # sedov, quad, bubble, rt
cropped_imgs = []

fig = plt.figure()
ax = fig.add_subplot(111)
plt.axis('off')

for list in images[:2]:
    for im in list:
        cropped_im = im[20:450, 160:650, :]
        cropped_imgs.append(cropped_im)
for list in images[2:3]:
    for im in list:
        cropped_im = im[20:450, 240:590, :]
        cropped_imgs.append(cropped_im)
for list in images[3:]:
    for im in list:
        cropped_im = im[80:390, 50:750, :]
        cropped_imgs.append(cropped_im)

plt.imshow(cropped_imgs[11])
#plt.show()
plt.savefig('rt_fv4.png', bbox_inches='tight')

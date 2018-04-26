import matplotlib.image as img
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import scipy.misc as misc
from read_files import read

images = read() # sedov, quad, bubble, rt
cropped_imgs = []
img_titles = ['compressible', 'compressible_rk', 'compressible_fv4']
png_names = ['sedov.png', 'sedov_rk.png', 'sedov_fv4.png', 'quad.png', 'quad_rk.png', 'quad_fv4.png', 'bubble.png', 'bubble_rk.png', 'bubble_fv4.png', 'rt.png', 'rt_rk.png', 'rt_fv4.png']

plt.gca().set_axis_off()
plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
plt.margins(0,0)
plt.gca().xaxis.set_major_locator(ticker.NullLocator())
plt.gca().yaxis.set_major_locator(ticker.NullLocator())

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

for n, im in enumerate(cropped_imgs):
    plt.gca().set_axis_off()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(ticker.NullLocator())
    plt.gca().yaxis.set_major_locator(ticker.NullLocator())#
    plt.imshow(im)
    if n < 6:
        plt.text(245, 3, img_titles[n%3], horizontalalignment='center',
                 verticalalignment='top')
        plt.savefig(png_names[n], dpi=90, bbox_inches='tight', pad_inches=0)
        plt.gcf().clear()
    elif n >=6 and n < 9:
        plt.text(175, 3, img_titles[n%3], horizontalalignment='center',
                 verticalalignment='top')
        plt.savefig(png_names[n], dpi=90, bbox_inches='tight', pad_inches=0)
        plt.gcf().clear()
    else:
        plt.text(350, 3, img_titles[n%3], horizontalalignment='center',
                 verticalalignment='top')
        plt.savefig(png_names[n], dpi=110, bbox_inches='tight', pad_inches=0)
        plt.gcf().clear()
    

#plt.imshow(cropped_imgs[2])
#plt.savefig('sedov_fv.png', bbox_inches='tight', pad_inches=0)
#plt.show()

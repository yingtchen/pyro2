# Description: shows compressible plots

from read_files import read
import matplotlib.pyplot as plt
import matplotlib.image as img

images = read()
images = images[6:]

fig = plt.figure()
plt.suptitle('FV4', fontsize=16)
plt.subplots_adjust(left=0.2,bottom=0.2,right=0.8,top=0.8,wspace=0,hspace=0)

loc = plt.MaxNLocator(4)
xticks = ['', '', '0.25', '', '0.75']
yticks = ['', '', '0.75', '', '0.25', '']
empticks = ['', '', '', '', '']

for n, lst in enumerate(images):
    for i, pic in enumerate(lst):
        a = fig.add_subplot(2,4,4*n+(i+1))
        im = a.imshow(pic, aspect='auto')
        a.xaxis.set_major_locator(loc)
        a.yaxis.set_major_locator(loc)
        if n==1 and i==0:
            a.set_xticklabels(xticks)
            a.set_yticklabels(yticks)
        elif n==1 and i!=0:
            a.set_xticklabels(xticks)
            a.set_yticklabels(empticks)
        elif n!=1 and i==0:
            a.set_xticklabels(empticks)
            a.set_yticklabels(yticks)
        else:
            a.set_xticklabels(empticks)
            a.set_yticklabels(empticks)

color = fig.add_axes([0.85, 0.2, 0.05, 0.6])
fig.colorbar(im, cax=color)

fig.set_size_inches(10, 5, forward=True)
fig.savefig('fv4.png', bbox_inches='tight')
#plt.show()

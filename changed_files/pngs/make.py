# Description: shows all compressible plots at different bulk velocities

from read_files import read
import matplotlib.pyplot as plt
import matplotlib.image as img
import matplotlib.colors as colors
import matplotlib.colorbar as cb
from mpl_toolkits.axes_grid1 import make_axes_locatable

images = read()
fig = plt.figure()

ax = fig.add_subplot(1,1,1)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(top='off',bottom='off',left='off',right='off',labeltop='off',labelbottom='off',labelleft='off',labelright='off')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.suptitle('128x128', fontsize=16, y=0.86)
plt.subplots_adjust(left=0.2,bottom=0.2,right=0.8,top=0.8,wspace=0,hspace=0)

loc = plt.MaxNLocator(4)
xticks = ['', '', '0.25', '', '0.75']
yticks = ['', '', '0.75', '', '0.25', '']
empticks = ['', '', '', '', '']
sub_titles = ['Standard', 'RK', '4th Order']
y_labels = ['t = 0.1', 't = 0.2']

for n, lst in enumerate(images):
    for i in range(len(lst)):
        a = fig.add_subplot(2,3,3*i+(n+1))
        im = a.imshow(lst[i], aspect='auto')
        a.xaxis.set_major_locator(loc)
        a.yaxis.set_major_locator(loc)
        if i==0:
            a.set_title(sub_titles[n])
        if n==0:
            a.set_ylabel(y_labels[i], rotation=0, ha='right')
        if n==0 and i==1:
            a.set_xticklabels(xticks)
            a.set_yticklabels(yticks)
        elif n!=0 and i==1:
            a.set_xticklabels(xticks)
            a.set_yticklabels(empticks)
        elif n==0 and i!=1:
            a.set_xticklabels(empticks)
            a.set_yticklabels(yticks)
        else:
            a.set_xticklabels(empticks)
            a.set_yticklabels(empticks)


#divider = make_axes_locatable(ax)
#cax = divider.append_axes('right', size='7%', pad=0.05)
cax = fig.add_axes([0.85, 0.2, 0.05, 0.6])
norm = colors.Normalize(vmin=0.0, vmax=5.0)

color = cb.ColorbarBase(cax, norm=norm)

fig.set_size_inches(9, 6, forward=True)

fig.savefig('plot.png', bbox_inches='tight')
plt.show()

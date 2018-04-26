import matplotlib.image as img
import scipy.misc as misc

def read():
    bubble = []
    quad = []
    rt = []
    sedov = []

    bubble.append(misc.imread('./pngs/bubble.png'))
    bubble.append(misc.imread('./pngs/bubble_rk.png'))
    bubble.append(misc.imread('./pngs/bubble_fv4.png'))

    quad.append(misc.imread('./pngs/quad.png'))
    quad.append(misc.imread('./pngs/quad_rk.png'))
    quad.append(misc.imread('./pngs/quad_fv4.png'))

    rt.append(misc.imread('./pngs/rt.png'))
    rt.append(misc.imread('./pngs/rt_rk.png'))
    rt.append(misc.imread('./pngs/rt_fv4.png'))

    sedov.append(misc.imread('./pngs/sedov.png'))
    sedov.append(misc.imread('./pngs/sedov_rk.png'))
    sedov.append(misc.imread('./pngs/sedov_fv4.png'))

    images = [sedov, quad, bubble, rt]

    return images

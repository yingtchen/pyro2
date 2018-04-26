import matplotlib.image as img

def read():
    standard = []
    rk = []
    fourth = []

    standard.append(img.imread('./pngs/standard1.png'))
    standard.append(img.imread('./pngs/standard2.png'))

    rk.append(img.imread('./pngs/rk1.png'))
    rk.append(img.imread('./pngs/rk2.png'))

    fourth.append(img.imread('./pngs/fourth1.png'))
    fourth.append(img.imread('./pngs/fourth2.png'))

    images = [standard, rk, fourth]

    return images

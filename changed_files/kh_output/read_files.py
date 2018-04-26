import matplotlib.image as img

def read():
    c128 = []
    rk128 = []
    fv128 = []

    c128.append(img.imread('./pngs/c_v0.png'))
    c128.append(img.imread('./pngs/c_v1.png'))
    c128.append(img.imread('./pngs/c_v3.png'))
    c128.append(img.imread('./pngs/c_v10.png'))

    rk128.append(img.imread('./pngs/rk_v0.png'))
    rk128.append(img.imread('./pngs/rk_v1.png'))
    rk128.append(img.imread('./pngs/rk_v3.png'))
    rk128.append(img.imread('./pngs/rk_v10.png'))

    fv128.append(img.imread('./pngs/fv_v0.png'))
    fv128.append(img.imread('./pngs/fv_v1.png'))
    fv128.append(img.imread('./pngs/fv_v3.png'))
    fv128.append(img.imread('./pngs/fv_v10.png'))

    images = [c128, rk128, fv128]

    return images

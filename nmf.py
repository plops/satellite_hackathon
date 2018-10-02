import PIL.Image
import pathlib
import matplotlib.pyplot as plt
import sklearn.decomposition
import skimage.filters
plt.ion()
import numpy as np
import scipy.ndimage.filters
fns = list(pathlib.Path('/home/martin/Downloads/').glob('2018*Cust*'))

rs = []
for fn in fns:
    im = PIL.Image.open(fn)
    r, g, b = im.split()
    r0 = scipy.ndimage.filters.gaussian_filter(r, sigma=4)[::3, ::3]
    rs.append(np.array(r0))

a = np.array(rs)

a.shape

a_ = np.load('/home/martin/stage/satellite_hackathon/eindh.npy')


a = np.array([scipy.ndimage.filters.gaussian_filter(
    a_[i], sigma=2)[::2, ::2] for i in range(a_.shape[0])])

a2 = a.reshape(a.shape[0], a.shape[1]*a.shape[2])

a2.shape
plt.imshow(a2.reshape(a.shape[0], a.shape[1], a.shape[2])[0, :, :])


model = sklearn.decomposition.NMF(n_components=5)
W = model.fit_transform(a2)
H = model.components_


a2.shape
H.shape
W.shape


for i in range(5):
    fig = plt.figure(0, (12, 8))
    pl = (1, 2)
    ax = plt.subplot2grid(pl, (0, 1))
    plt.imshow(H[i, :].reshape(a.shape[1], a.shape[2]))
    ax = plt.subplot2grid(pl, (0, 0))
    plt.plot(W[:, i])

    plt.xlabel('time 2017-09-23 .. 2018-10-03')
    plt.tight_layout()
    plt.savefig('/home/martin/nmf_sat{}.png'.format(i))

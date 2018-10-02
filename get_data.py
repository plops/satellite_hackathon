# https://sentinelhub-py.readthedocs.io/en/latest/examples/ogc_request.html

INSTANCE_ID = '<secret>'
import datetime
import numpy as np
import matplotlib.pyplot as plt
plt.ion()
# pip install --user sentinelhub
# export PATH=$PATH:'/home/martin/.local/bin'
# sudo pacman -S community/python-pyproj
from sentinelhub import WmsRequest, WcsRequest, MimeType, CRS, BBox
from sentinelhub import DataSource
from sentinelhub import CustomUrlParam
# betsiboka_coords_wgs84 = [46.16, -16.15, 46.51, -15.58]
# betsiboka_bbox = BBox(bbox=betsiboka_coords_wgs84, crs=CRS.WGS84)
# wms_true_color_request = WmsRequest(layer='TRUE-COLOR-S2-L1C',
#                                     bbox=betsiboka_bbox,
#                                     time='2017-12-15',
#                                     width=512, height=856,
#                                     instance_id=INSTANCE_ID)
# wms_true_color_img = wms_true_color_request.get_data()

# plt.imshow(wms_true_color_img[-1])

# # store
# # wms_bands_img = wms_bands_request.get_data(save_data=True)
# # # load

# # wms_bands_request_from_disk = WmsRequest(data_folder='test_dir',
# #                                          layer='BANDS-S2-L1C',
# #                                          bbox=betsiboka_bbox,
# #                                          time='2017-12-15',
# #                                          width=512, height=856,
# #                                          image_format=MimeType.TIFF_d32f,
# #                                          instance_id=INSTANCE_ID)

# # wms_bands_img_from_disk = wms_bands_request_from_disk.get_data()


# for source in DataSource.get_available_sources():
#     print(source)


# volcano_bbox = BBox(bbox=[(-2217485.0, 9228907.0),
#                           (-2150692.0, 9284045.0)], crs=CRS.POP_WEB)

# l2a_request = WmsRequest(data_source=DataSource.SENTINEL2_L2A,
#                          layer='TRUE-COLOR-S2-L2A',
#                          bbox=volcano_bbox,
#                          time='2017-08-30',
#                          width=512,
#                          instance_id=INSTANCE_ID)
# l2a_data = l2a_request.get_data()
# plt.imshow(l2a_data[0])


# s1_request = WmsRequest(data_source=DataSource.SENTINEL1_IW,
#                         layer='TRUE-COLOR-S1-IW',
#                         bbox=volcano_bbox,
#                         time='2017-10-03',
#                         width=512,
#                         custom_url_params={CustomUrlParam.SHOWLOGO: False},
#                         instance_id=INSTANCE_ID)

# s1_data = s1_request.get_data()
# plt.imshow(s1_data[-1])

list(CRS)

CRS.POP_WEB

betsiboka_coords_wgs84 = [46.16, -16.15, 46.51, -15.58]
betsiboka_bbox = BBox(bbox=betsiboka_coords_wgs84, crs=CRS.WGS84)

ein_coords_wgs84 = [51.476, 5.337, 51.424, 5.429]
ein_coords_wgs84 = [5.337, 51.476, 5.429, 51.424]
ein_bbox = BBox(bbox=ein_coords_wgs84, crs=CRS.WGS84)

bbox = ein_bbox
s1_request = WmsRequest(data_source=DataSource.SENTINEL1_IW,
                        layer='TRUE-COLOR-S1-IW',
                        bbox=bbox,
                        time=('2014-03-23', '2018-10-03'),
                        width=2048,
                        custom_url_params={CustomUrlParam.SHOWLOGO: False},
                        instance_id=INSTANCE_ID)

(s1_request)

s1_data = s1_request.get_data()
a3 = np.array(s1_data)

a3.shape

af = np.mean(a3, axis=(1, 2))

print('{} files are valid'.format(np.sum(af < 130)))
av = a3[af < 130, :, :]
av.shape
np.save('/home/martin/stage/satellite_hackathon/eindh.npy', av)

plt.imshow(np.mean(av, axis=0))

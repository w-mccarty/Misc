import numpy as np
import cv2
from sklearn.cluster import KMeans
from PIL import Image

def preprocess_image(image):
    pixels = image.reshape((-1, 3))
    pixels = np.float32(pixels)
    return pixels

def get_dominant_colors(pixels, k=3):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    colors = kmeans.cluster_centers_
    return colors.astype(int)

image_path = "img.jpg"
thumb_max = 500
thumb_path = "thumb.jpg"
num_colors = 5
flname = "hexval.js"

#image = Image.open(image_path)
#MAX_SIZE = (thumb_max, thumb_max)
#image.thumbnail(MAX_SIZE)
#image.save(thumb_path)

#FIND 3 MOST COMMON BGR VALUES
image = cv2.imread(thumb_path)
preprocessed_image = preprocess_image(image)
dcv = get_dominant_colors(preprocessed_image, k=num_colors)
#print(dcv)

#CONVERT TO CMYK AND TAKE PERCENTAGES OF VALUES
cmyk1 = []
rgb_scale = 255
cmyk_scale = 100
def rgb_to_cmyk(r,g,b):
    if (r == 0) and (g == 0) and (b == 0): #black
        return 0, 0, 0, cmyk_scale
    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / rgb_scale
    m = 1 - g / rgb_scale
    y = 1 - b / rgb_scale
    # extract out k [0,1]
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy
    # rescale to the range [0,cmyk_scale]
    #cmyk1.append([round(c*cmyk_scale), round(m*cmyk_scale), round(y*cmyk_scale), round(k*cmyk_scale)])
    for i in (10, 20, 30, 40, 50, 60, 70, 80, 90):
        cmyk1.append([round(c*cmyk_scale), round(m*cmyk_scale), round(y*cmyk_scale), i])
for i in range(len(dcv)):
    rgb_to_cmyk((dcv[i][2]),(dcv[i][1]),(dcv[i][0]))
#print(cmyk1)

#CONVERT TO RGB
rgb1 = []
def cmyk_to_rgb(c,m,y,k):
    r = rgb_scale * (1.0 - c / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    g = rgb_scale * (1.0 - m / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    b = rgb_scale * (1.0 - y / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    rgb1.append([round(r), round(g), round(b)])
for i in range(len(cmyk1)):
    cmyk_to_rgb(cmyk1[i][0],cmyk1[i][1],cmyk1[i][2],cmyk1[i][3])
#print(rgb1)

#CONVERT TO HEX VALUES
hex1 = []
def clamp(x):
    return max(0, min(x, 255))
for i in range(len(rgb1)):
    hex = "#{0:02x}{1:02x}{2:02x}".format(clamp(rgb1[i][0]), clamp(rgb1[i][1]), clamp(rgb1[i][2]))
    hex1.append(hex)

#WRITE OUT TO .JS
vtotal = "var cvals = " + str(hex1)
with open(flname, "w") as file:
    file.write(vtotal)

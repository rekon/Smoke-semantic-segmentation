import cv2
import json
import numpy as np
from pprint import pprint
import glob


def draw_mask(json_filename, image_filename, resultant_filename):
    with open(json_filename) as data_file:
        data = json.load(data_file)
    # pprint(data)

    image = cv2.imread(image_filename)
    mask = np.zeros((image.shape[0],image.shape[1],1), dtype=np.uint8)

    objs = data['shapes']

    for obj in objs:

        color = 255

        points = np.array(list(obj['points']), dtype=np.int32)
        # print(points)
        # print(color)
        cv2.fillPoly(mask, [points], color)

    cv2.imwrite('tagged\\masks\\'+resultant_filename, mask)
    cv2.imwrite('tagged\\images\\'+image_filename, image)
    print('Image saved', resultant_filename)


for filename in glob.glob('*.json'):
    img_filename = filename.split('.')[0]+'.jpg'
    draw_mask(filename, img_filename, img_filename)
# draw_mask('smoke_(2).json','smoke_(2).jpg','smoke_(2)_mask.jpg')

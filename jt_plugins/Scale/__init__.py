import cv2
import numpy as np
import math
from PIL import Image

def transform(img,source,target,**kwargs):
    factor = float(kwargs['factor'])
    interpolation = cv2.INTER_LINEAR if kwargs['interpolation'] == 'Bilinear' else cv2.INTER_CUBIC
    cv_img = np.asarray(img)
    #ignore alpha channel
    if cv_img.shape[2] > 3:
      cv_img = cv_img[:,:,:3]
    img_scaled = cv2.resize(cv_img, dsize=(0,0), fy=factor, fx=factor, interpolation=interpolation)
    Image.fromarray(img_scaled, "RGB").save(target)
    return None,None

def operation():
  return {
          'name': 'Scale',
          'category': 'Filter',
          'description':'Resize the image with interpolation',
          'software':'OpenCV',
          'version':cv2.__version__,
          'arguments':{
              'factor' : {
                  "type": "float",
                  "defaultvalue": 1.,
                  "description": "Factor to be multiplied to each dimension"
              },
              'interpolation': {
                  "type": "list",
                  "values" : ["bilinear", "bicubic"],
                  "defaultvalue": "bilinear",
                  'description': 'Interpolation method'
            }},
          'transitions': [
              'image.image'
          ]
          }

def suffix():
    return None

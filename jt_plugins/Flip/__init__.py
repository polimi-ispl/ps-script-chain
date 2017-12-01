import cv2
import numpy as np
import math
from PIL import Image

def transform(img,source,target,**kwargs):
    orientation = kwargs['orientation']
    cv_img = np.asarray(img)
    #ignore alpha channel
    if cv_img.shape[2] > 3:
      cv_img = cv_img[:,:,:3]
    if orientation == 'horizontal':
      img_flip = cv_img[:,::-1,:]
    if orientation == 'vertical':
      img_flip = cv_img[::-1,:,:]
    Image.fromarray(img_flip, "RGB").save(target)
    return None,None

def operation():
  return {
          'name': 'Flip',
          'category': 'Filter',
          'description':'Flip the image horizontally or vertically',
          'software':'OpenCV',
          'version':cv2.__version__,
          'arguments':{
              'orientation': {
                  "type": "list",
                  "values" : ["horizontal", "vertical"],
                  "defaultvalue": "horizontal",
                  'description': 'Flip direction'
            }},
          'transitions': [
              'image.image'
          ]
          }

def suffix():
    return None

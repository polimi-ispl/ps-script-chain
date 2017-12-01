import cv2
import numpy as np
import math
from PIL import Image

def transform(img,source,target,**kwargs):
    cv_img = np.asarray(img)
    #ignore alpha channel
    if cv_img.shape[2] > 3:
      cv_img = cv_img[:,:,:3]
    img_blur = cv2.GaussianBlur(cv_img, (3,3), 0)
    Image.fromarray(img_blur, "RGB").save(target)
    return None,None

def operation():
  return {
          'name': 'GIMPBlur',
          'category': 'Filter',
          'description':'Blur the image with a 3x3 gaussian kernel with sigma=0',
          'software':'OpenCV',
          'version':cv2.__version__,
          'arguments':{
                    'dummy_argument': {
                    "type": "str",
                    "defaultvalue": "DO NOT SET ME!",
                    "description": "only for journaling purposes"
                    }
              },
          'transitions': [
              'image.image'
          ]
          }

def suffix():
    return None

import cv2
import numpy as np
import math
from PIL import Image

def transform(img,source,target,**kwargs):
    angle =int(kwargs['angle'])
    cv_img = np.asarray(img)
    #ignore alpha channel
    if cv_img.shape[2] > 3:
      cv_img = cv_img[:,:,:3]
    h, w = cv_img.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((h/2, w/2), -angle, 1)
    img_rotate = cv2.warpAffine(cv_img, rotation_matrix, (w,h))
    r = .5 * min(w, h)
    l = int(np.round(r / math.sqrt(2)))
    off_x = int(np.round(w/2) - l)
    off_y = int(np.round(h/2) - l)
    img_crop = img_rotate[off_x:off_x + 2*l, off_y:off_y+ 2*l, :]
    Image.fromarray(img_crop, "RGB").save(target)
    return None,None

def operation():
  return {
          'name': 'Rotate',
          'category': 'Filter',
          'description':'Rotate and crop the image to avoid background filling',
          'software':'OpenCV',
          'version':cv2.__version__,
          'arguments':{
              'angle': {
                  'type': 'int',
                  'defaultvalue': 0,
                  'description': 'Clockwise rotation angle (degrees)'
            }},
          'transitions': [
              'image.image'
          ]
          }

def suffix():
    return None

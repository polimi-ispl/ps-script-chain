import cv2
import numpy as np
import math
from PIL import Image

def transform(img,source,target,**kwargs):
    shape = kwargs['shape']
    x = int(kwargs['x'])
    y = int(kwargs['y'])
    w = int(kwargs['width'])
    h = int(kwargs['height'])
    new_x = int(kwargs['new_x'])
    new_y = int(kwargs['new_y'])
    cv_img = np.asarray(img)
    if cv_img.shape[2] < 4:
      r,g,b = cv2.split(cv_img)
      cv_img = cv2.merge((b,g,r, np.ones(cv_img.shape[:2], dtype=np.uint8) * 255))
    box = ((x+np.round(w/2), y+np.round(h/2)), (w,h), 0)
    mask = np.zeros_like(cv_img,dtype=np.uint8)
    if shape == 'ellipse':
      mask = cv2.ellipse(mask, box, (255,255,255,255), -1)
    elif shape == 'rectangle':
      mask = cv2.rectangle(mask, (x,y), (x+w,y+h), (255,255,255,255), -1)
    result = np.bitwise_and(mask, cv_img)
    patch = result[y:y+h+1,x:x+w+1,:]
    alpha_patch = patch[:,:,3] / 255.0
    alpha_img = 1.0 - alpha_patch
    for i in range(3):
      cv_img[new_y:new_y+patch.shape[0], new_x:new_x+patch.shape[1],i] = alpha_patch * patch[:,:,i] + alpha_img * cv_img[new_y:new_y+patch.shape[0], new_x:new_x+patch.shape[1],i]
    #Image.fromarray(cv_img, "RGB").save(target)
    cv2.imwrite(target, cv_img)
    return None,None

def operation():
  return {
          'name': 'GIMPCopyPaste',
          'category': 'Filter',
          'description':'Extract a rectangular or elliptic patch from the image and paste it back with a dispacement',
          'software':'OpenCV',
          'version':cv2.__version__,
          'arguments':{
              'shape': {
                  "type": "list",
                  "values" : ["rectangle", "ellipse"],
                  "defaultvalue": "rectangle",
                  'description': 'shape of the selection'
              },
              'x': {
                  "type": "int",
                  "defaultvalue": 0,
                  "description": "x coordinate of upper left corner of the selection"
              },
              'y': {
                  "type": "int",
                  "defaultvalue": 0,
                  "description": "y coordinate of upper left corner of the selection"
              },
              'width': {
                  "type": "int",
                  "defaultvalue": 0,
                  "description": "width of the selection"
              },
              'height': {
                  "type": "int",
                  "defaultvalue": 0,
                  "description": "heigth of the selection"
              },
              'new_x': {
                  "type": "int",
                  "defaultvalue": 0,
                  "description": "x coordinate of upper left corner of the selection after the displacement"
              },
              'new_y': {
                  "type": "int",
                  "defaultvalue": 0,
                  "description": "y coordinate of upper left corner of the selection after the displacement"
              },
              'antialias': {
                  "type": "str",
                  "defaultvalue": "False",
                  "description": "use antialias. currently hardcoded to False."
              }},
          'transitions': [
              'image.image'
          ]
          }

def suffix():
    return None

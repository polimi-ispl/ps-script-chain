import numpy
from maskgen.image_wrap import ImageWrapper
import cv2

def transform(img,source,target,**kwargs):
    new_w = int(kwargs['new_w'])
    new_h = int(kwargs['new_h'])
    off_x = int(kwargs['off_x'])
    off_y = int(kwargs['off_y'])
    cv_image = numpy.array(img)
    if off_y + new_h > cv_image.shape[0] or off_x + new_w > cv_image.shape[1]:
      raise ValueError('Crop exceed image dimensions')
    new_img = cv_image[off_y:off_y+new_h, off_x:off_x+new_w,:]
    ImageWrapper(new_img).save(target)
    return None,None

def suffix():
    return None

def operation():
  return {
          'category': 'Filter',
          'name': 'GIMPCrop',
          'description':'Crop',
          'software':'OpenCV',
          'version':cv2.__version__,
          'arguments':{
                    'new_w': {
                        'type': "int",
                        'description':'New width '
                        },
                    'new_h': {
                        'type': "int",
                        'description': 'New height'
                        },
                    'off_x': {
                        'type': "int",
                        'description': 'Displacement along horizontal axis'
                        },
                    'off_y': {
                        'type': "int",
                        'description':'Displacement along vertical axis'
                        }},
          'transitions': [
              'image.image'
          ]
          }

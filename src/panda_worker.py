import cv2
import numpy as np
import pandas as pd

# graph image dimension
# 40 px y
# 838 px x

def get_datap():
    # Step 1: Read the image
    image = cv2.imread('rsrc/output_image.png')


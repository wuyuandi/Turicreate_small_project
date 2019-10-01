import cv2
import glob
import os

encode_param = [cv2.IMWRITE_JPEG_QUALITY, 80]
ow = 2048
oh = 1536
scale_percent = 20  # percent of original size


def compressimage(foldername):
    imagenum = 0
    width = int(ow * scale_percent / 100)
    height = int(oh * scale_percent / 100)
    dim = (width, height)
    digit = ''.join(x for x in foldername if x.isdigit())
    x = foldername.split("/")
    x = x[0]
    fold = 'new'+x + '/'+digit
    if not os.path.exists(fold):
        os.makedirs(fold)
    for img in glob.glob("{}/*.jpg".format(foldername)):
        image = cv2.imread(img)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        cv2.imwrite('{}/compress_img{}.jpg'.format(fold,imagenum), resized,encode_param)
        imagenum = imagenum+1
    return imagenum


# if __name__=="__main__":
#     loadimage('train/0')
import cv2
import re


def validator_ext_image(name_img):
    """Validate the image name extension
            .jpg
            .png"""
    results = re.findall('\.(?:png|jpg)$', name_img)
    return bool(results)


class ImageStorage:

    @staticmethod
    def read_image(path_img):
        """Read an image from storage and return an obj image"""
        if isinstance(path_img, str):
            img = cv2.imread(path_img)
            return img
        else:
            print("formato no valido")
            return None

    @staticmethod
    def save_image(img, name_img):
        """Write an image on disk"""
        if validator_ext_image(name_img):
            cv2.imwrite(name_img, img)
        else:
            print("Invalid image name extension")



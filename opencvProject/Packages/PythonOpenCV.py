import cv2
import numpy


class PythonOpenCV:
    @staticmethod
    def image_to_gray_scale(img):
        """Receive an obj image, return a gray image"""
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img_gray

    @staticmethod
    def image_to_black_and_white(img):
        """Receive an obj image, return a black and white image"""
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (thresh, black_white) = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
        return black_white

    @staticmethod
    def image_to_flip_v(img):
        """Receive an obj image, return a vertical flip image"""
        img_flipVertical = cv2.flip(img, 0)
        return img_flipVertical

    @staticmethod
    def image_to_flip_h(img):
        """Receive an obj image, return a horizontal flip image"""
        img_flipHorizontal = cv2.flip(img, 1)
        return img_flipHorizontal

    @staticmethod
    def resize_image(img, fx, fy):
        """Receive an obj image, return a scaled image on the x and y axis"""
        resized = cv2.resize(img, None, fx=fx, fy=fy)
        return resized

    @staticmethod
    def tile_image(img, repetitions_vertically, repetitions_horizontally):
        """Receive an obj image, return an image with vertically and horizontally repetitions"""
        tile = numpy.tile(img, (repetitions_vertically, repetitions_horizontally, 1));
        return tile

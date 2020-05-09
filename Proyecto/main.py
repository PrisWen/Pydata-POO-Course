import cv2
import numpy


def read_image(path_img):
    """Read an image from storage and return an obj image"""
    img = cv2.imread(path_img)
    return img


def img_to_gray_scale(img):
    """Receive an obj image, the return a gray image"""
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img_gray


def img_to_black_and_white(img):
    img_gray = img_to_gray_scale(img)
    (thresh, black_white) = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)
    return black_white


def save_image(img, name_img):
    """Write an image on disk"""
    cv2.imwrite(name_img, img)


def image_to_flip_v(img):
    img_flipVertical = cv2.flip(img, 0)
    return img_flipVertical


def image_to_flip_h(img):
    img_flipHorizontal = cv2.flip(img, 1)
    return img_flipHorizontal


def resize_image(img, fx, fy):
    resized = cv2.resize(img, None, fx=fx, fy=fy)
    return resized


def tile_image(img, repetitions_vertically, repetitions_horizontally):
    tile = numpy.tile(img, (repetitions_vertically, repetitions_horizontally, 1));
    return tile


if __name__ == '__main__':

    img = read_image("images/conejitos.jpg")
    # gray_image = img_to_gray_scale(img)
    # save_image(gray_image, "img_gray.jpg")
    # flip_h_image = image_to_flip_h(img)
    # save_image(flip_h_image, "flip_h.jpg")
    # flip_v_image = image_to_flip_v(img)
    # save_image(flip_v_image, "flip_v.jpg")
    # img_resize = resize_image(img, 2.0, 2.0)
    # save_image(img_resize, "resize.jpg")
    # img_tile = tile_image(img, 2, 3)
    # save_image(img_tile, "tile.jpg")
    img_black_white = img_to_black_and_white(img)
    save_image(img_black_white, "black_white.jpg")



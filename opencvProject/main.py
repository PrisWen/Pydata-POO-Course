from opencvProject.Packages.ImageStorage import ImageStorage
from opencvProject.Packages.PythonOpenCV import PythonOpenCV



if __name__ == '__main__':

    img = ImageStorage.read_image("images/conejitos.jpg")
    gray_image = PythonOpenCV.image_to_gray_scale(img)
    ImageStorage.save_image(gray_image, "outputs_images/img_gray.jpg")
    flip_h_image = PythonOpenCV.image_to_flip_h(img)
    ImageStorage.save_image(flip_h_image, "outputs_images/flip_h.jpg")
    flip_v_image = PythonOpenCV.image_to_flip_v(img)
    ImageStorage.save_image(flip_v_image, "outputs_images/flip_v.jpg")
    img_resize = PythonOpenCV.resize_image(img, 2.0, 2.0)
    ImageStorage.save_image(img_resize, "outputs_images/resize.jpg")
    img_tile = PythonOpenCV.tile_image(img, 2, 3)
    ImageStorage.save_image(img_tile, "outputs_images/tile.jpg")
    img_black_white = PythonOpenCV.image_to_black_and_white(img)
    ImageStorage.save_image(img_black_white, "outputs_images/black_white.jpg")



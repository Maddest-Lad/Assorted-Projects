from PIL import Image


class ImageGenerator:

    def __init__(self, image, default_threshold=128):
        self.image = image
        self.default_threshold = default_threshold

    def set_image(self, image):
        """
        Sets the image.
        :param image: The image to set.
        """
        self.image = image
        return self

    def resize_image(self, width, height):
        """
        Resize the image.
        :param width: The width of the image.
        :param height: The height of the image.
        """
        self.image = self.image.resize((width, height))
        return self

    def filter_image(self, threshold):
        """
        Filters the image.
        :param threshold: The threshold.
        """
        self.image = self.image.convert('L').point(lambda x: 255 if x > threshold else 0, mode='1')
        return self

    def save_image(self, path) -> None:
        """
        Saves the image.
        :param path: The path to save the image.
        """
        self.image.save(path)


if __name__ == '__main__':
    ImageGenerator(Image.open('Test_1.JPEG')).resize_image(300, 300).filter_image(128).save_image('Test_1_result.jpg')

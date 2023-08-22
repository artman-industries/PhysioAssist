class RepObject:
    """
    A class representing a repetition with a unique identifier (rep_id) and associated frames.

    Attributes:
        rep_id (str): The unique identifier for the repetition object.
        images (list): A list of tuples (id, image_path) associated with the object.

    Methods:
        __init__(self, rep_id): Initializes a RepObject instance with a rep_id and an empty list of images.
        add_image(self, image_id, image_path): Adds an image to the list of images associated with the object.
        get_images(self): Returns the list of images associated with the object, ordered by id.
    """

    def __init__(self, rep_id: str):
        """
        Initializes a RepObject instance.

        Args:
            rep_id (str): The unique identifier for the repetition.
        """
        self.rep_id = rep_id
        self.images = []

    def add_frame(self, frame_num: int, frame_path: str):
        """
        Adds an image to the list of images associated with the object.

        Args:
            frame_num (int): The unique identifier for the image.
            frame_path (str): The file path to the image.
        """
        self.images.append((frame_num, frame_path))
        self.images.sort(key=lambda x: x[0])  # Sort images by id

    def get_images(self) -> list:
        """
        Returns the list of images associated with the object, ordered by id.

        Returns:
            list: A list of tuples (id, image_path).
        """
        return self.images

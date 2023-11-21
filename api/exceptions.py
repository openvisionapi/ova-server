class BaseException(Exception):
    message: str

    def __init__(self, message=None, **kwargs):
        super().__init__(message or self.message)
        self.kwargs = kwargs


class ImageTooLarge(BaseException):
    message = "Image Too Large"


class UnsupportedImageType(BaseException):
    message = "Unsupported Image Type"

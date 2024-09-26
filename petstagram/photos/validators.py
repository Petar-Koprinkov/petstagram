from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxSizePhotoValidator:
    def __init__(self, size, message=None):
        self.size = size
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if not value:
            self.__message = 'Your file size is too large.'
        else:
            self.__message = value

    def __call__(self, obj):
        if obj.size > self.size * 1024 * 1024:
            raise ValidationError(self.message)





class ResourceConfigurationException(Exception):
    def __init__(self, obj_type, obj_name, message="Error while access EKS"):
        self.obj_type = obj_type
        self.obj_name = obj_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} {self.obj_type} {self.obj_name}'


class APIError(Exception):
    pass

class CustomError(Exception):
    def __init__(self, message, error_code=1):
        super().__init__(message)
        self.error_code = error_code

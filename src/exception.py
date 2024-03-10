import sys


def error_message_detail(error, error_detail: sys) -> None:
    """
    Function to log custom errors

    Args:
    - error: Error raised during execution
    - error_message: Custom message that needs to be displayed
                     when the error is raised

    Returns:
    - None
    """

    _, _, exc_tb = error_detail.exc_info()
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        exc_tb.tb_frame.f_code.co_filename(),
        exc_tb.tb_lineno,
        str(error)
    )

    return error_message

class CustomException(Exception):

    def __init__(self, error_message: str, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message =  error_message_detail(error=error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
    


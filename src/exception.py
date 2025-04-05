import sys
import logging

# Define a custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = self.error_message_detail(error_message, error_detail)
    
    def error_message_detail(self, error_message, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error occurred in script: {file_name} at line {line_number} with message: {error_message}"
    
    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        # Intentional error: division by zero
        a = 1 / 0
    except Exception as e:
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        logging.info("Divide by zero error occurred")
        raise CustomException(e, sys)

            
    
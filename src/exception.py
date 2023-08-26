import sys 
import logging

 #whenever error - own custom message, error detail is in sys
 # function of how message will look like with respect to custom exception
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #interesting is the last part of the info, tb is for traceback
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    return error_message

       



# custom exception class iwth error message variable inside, getting populated from this function
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):  #init file is the constructor
        super().__init__(error_message) # evt super with ()
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

# error--> raise custom exception--> print error message
    def __str__(self):
        return self.error_message    



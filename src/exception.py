import sys
from src.logger import logging
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    #eror mengambil file saat ini, dan baris kesalahan kode, dan error yang didapat
    error_message = f'Error occured in python scipt name {file_name} Line number {exc_tb.tb_lineno} error message {str(error)}'
    
    return error_message

class CustumException(Exception):
    #error_detail adalah sebuaah objek dari sys
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail)
        
    def __str__(self):
        return self.error_message
    

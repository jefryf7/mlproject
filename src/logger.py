import logging
import os
from datetime import datetime

#ini akan membuat sebuah nama file yang akan berbeda, karena kita memasukkan sebauh detik di akhir
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#membuat folder
log_path = os.path.join(os.getcwd(),'logs',LOG_FILE)

#jika folder logs sudah ada sebelumnya, tambahkan folder baru di dalam logs tersebut
os.makedirs(log_path,exist_ok=True)

#ini adalah sebuah nama filenya, yang akan kit gabungkan dengan log_path
LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)
print('tes',LOG_FILE_PATH)

logging.basicConfig(
    filename=LOG_FILE_PATH,#nama sebuah file
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",#isi dari sebuah file
    level=logging.INFO,#memberikan sebuah informasi 
)

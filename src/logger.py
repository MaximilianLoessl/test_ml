import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #filename logs, whatever logs will get created, will be with respect to currend dir
os.makedirs(logs_path,exist_ok=True) # keep on appending inside

LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)


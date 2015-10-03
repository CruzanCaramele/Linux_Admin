import zipfile
import sys
import os
import logging

# create the file where logs are saved
logging.basicConfig(filename="file_ex.log", level=logging.DEBUG)

logging.info("checking to see if the backup.zip exists")

# check to see if backup file exists
if os.path.exists("backup.zip"):
    logging.info("The file Exists!")
    try:
        zip_file = zipfile.ZipFile("backup.zip", "a")
    except:
	err = sys.exc_info()


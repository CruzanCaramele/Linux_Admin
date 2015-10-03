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
	logging.error("Unable to open backup.zip in append mode!")
	logging.error("Error Num: " + str(err[1].args[0]))
	logging.error("Error Msg: " + err[1].args[1]
	sys.exit()

else:
    logging.info("creating backup.zip")
    try:
	zip_file = zipfile.ZipFile("backup.zip", "w")
    except:
	err = sys.exc_info()
	logging.error("Unable to crate backup.zip!")
	logging.error("Error Num: " + str(err[1].args[0]))
	logging.error("Error Msg: " + err[1].args[1]
	sys.exit()

logging.info("Adding test.text to backup.zip")

try:
    zip_file.write("test.txt", "test.txt", zipfile.ZIP_DEFLATED)

except:


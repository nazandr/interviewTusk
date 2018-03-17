import ftplib
import json
from multiprocessing import Process

def fileUpload (path, ftpPath, ftype):
    ftp = ftplib.FTP(host, login, password)
    print(ftp.login())
    if ftype.lower() not in ["txt", "html", "rst"]:
        with open(path, 'rb') as file:
            ftp.storbinary('STOR ' + ftpPath, file)
    else:
        with open(path) as file:
            ftp.storlines('STOR ' + ftpPath, file)
    ftp.quit()

if __name__ == '__main__':
    conf = json.load(open("./conf.json"))
    host = conf[0]["host"]
    login = conf[0]["login"]
    password = conf[0]["password"]
    for i in conf[1]["fils"]:
        p = Process(target = fileUpload, args = (i["path"], i["ftpPath"], i["ftype"], ))
        p.start()
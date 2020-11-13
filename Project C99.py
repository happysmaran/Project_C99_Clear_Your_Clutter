import os
import shutil
import time

path="D:/picture"
month=6
exist=os.path.exists(path)

if exist==True:
    files=os.listdir(path)
    for i in files:
        name, ext=os.path.splitext(i)
        ext=ext[1:]
        if os.path.exists(path+"/"+name+"."+ext):
            fullnamefile=path+"/"+name+"."+ext
            fileage=os.stat(path+"/"+name+"."+ext).st_ctime
            ty_res = time.gmtime(fileage)
            res = int(time.strftime("%m",ty_res))
            if res<= month:
                os.remove(fullnamefile)
                print("deleted")
            else:
                continue
        else:
            continue
else:
    print("directory not found")

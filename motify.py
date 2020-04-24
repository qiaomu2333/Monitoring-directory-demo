import os
import sys
import pyinotify
import glob
import shutil
import time
import datetime

multi_event = pyinotify.IN_MODIFY
wm = pyinotify.WatchManager()
path = sys.argv[1]


def filenum():
   global path_file_number
   path_file_number=glob.glob('/root/*')
   return 0
def createdir():
    global motidir
    motidir=path+'motied/'
    os.mkdir(motidir)
    return 0

class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self,event):
        t=event.pathname.replace(path,'')
        time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')
        newfile=motidir + t + time
        shutil.copyfile(event.pathname,newfile)
        result = "%s be Modify"%(event.pathname)                           
        print(result)

filenum()
createdir()
handler = MyEventHandler()
notifier = pyinotify.Notifier(wm,handler)
wm.add_watch(path,multi_event)
notifier.loop()



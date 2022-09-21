###Importing Libaries
__doc__ = """While sending message dont intract with kwyboad and mouse 
            because it running base on the pyautogui module (NOT IN SELINEUM)
            before running please make sure to connect the internet
            and preopen the whatsweb tab and get login
            THANKYOU FOR USING THE MODULE
            BY MICHAELJOSEPHHEIDEN"""

import sys
import time
import webbrowser as wb
import pyautogui

class Whatsappauto:
    "Main class for the module contains start() method"
    def __init__(self,file:'str file name',msg:'message to send')->None: 
        self.Numbers = str
        self.msg = msg
        self.file =file
    def start(self)->'None':
        'it starts to messaging through whatsweb'
        with open(self.file,'r') as file:
            self.Numbers = file.read()
            number_list = self.Numbers.splitlines()
        for num in number_list:
            wb.open('https://web.whatsapp.com/send?phone=+91{0}&text={1}'.format(num,self.msg))
            time.sleep(15)
            pyautogui.press('enter')
            time.sleep(8)
            pyautogui.hotkey('ctrl','w')
            print('Msg send to {0} sucessfully'.format(num))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Use --help or -h to get help')
        sys.exit()
    if sys.argv[1] == '--help' or '-h' or '-H':
        print("""BulkWhatMsg takes two parametters
                  BulkWhatMsg [Filename] and [Message]:in string format""")
        sys.exit()
    try:
        mgsr = Whatsappauto(sys.argv[1],sys.argv[2])
        mgsr.start()
    except:
        print("Use --help to get help")


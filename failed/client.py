__author__ = 'Ben'
import socket
import Tkinter


def main():
    root = Tkinter.Tk()
    root.title("Pi Remote")
    global client
    global connected
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    global f
    global l
    global r
    global b
    f = 0
    l = 0
    b = 0
    r = 0

    def foward():
        global f
        global fpushed
        fpushed = False
        if connected == True:
            if fpushed == False:
                f = 1
                fpushed = True
            if fpushed == True:
                f = 0
                fpushed = False

    def left():
        global lpushed
        global l
        lpushed = False
        if connected == True:
            if lpushed == 0:
                l = 1
                lpushed = True
            if lpushed == False:
                l = 0
                lpushed = False

    def back():
        global bpushed
        global b
        bpushed = False
        if connected == True:
            if bpushed == 0:
                b = 1
                bpushed = True
            if bpushed == False:
                b = 0
                bpushed = False

    def right():
        global rpushed
        global r
        rpushed = False
        if connected == True:
            if rpushed == 0:
                r = 1
                rpushed = True
            if rpushed == False:
                r = 0
                rpushed = False

    def connect():
        global connected
        global client
        ip = socket.gethostname()
        client.connect((ip, 6000))
        connected = True


    fowardButton = Tkinter.Button(root, text="F", command=foward)
    fowardButton.grid(row=0, column=1)

    leftButton = Tkinter.Button(root, text="L", command=left)
    leftButton.grid(row=1, column=0)

    backButton = Tkinter.Button(root, text="B", command=back)
    backButton.grid(row=1, column=1)

    rightButton = Tkinter.Button(root, text="R", command=right)
    rightButton.grid(row=1, column=2)

    connectButton = Tkinter.Button(root, text="C", command=connect)
    connectButton.grid(row=2, column=0)


    Tkinter.mainloop()

if __name__ == "__main__":
    main()

while True:
    if connected == True:
        global data
        global rts
        data = (int(f), int(l), int(b), int(r))
        rts = client.recv(1)
        if rts == '*':
            client.send(data)
        else:
            pass


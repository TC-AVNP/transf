import socket
from tkinter import Text
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
fname = "unassigned"
Fname = "blank"
TCP_PORT = 5000
BUFFER_SIZE = 1024

# TCP_IP= input('Ip from other machine: ')
TCP_IP = '192.168.1.11'

def fileName(sock, addr):
    sock.sendto(Fname.encode(), addr)
    Udata = sock.recv(BUFFER_SIZE)
    data = Udata.decode()
    send(sock,addr)

def send(sock, addr):
    fileToR = open(fname,"rb")
    l= fileToR.read(BUFFER_SIZE)
    while (l) :
        sock.send(l)
        l = fileToR.read(1024)
    fileToR.close()

    messagebox.showinfo("", "Ficheiro enviado")
    sys.exit(0)





# def sendFile(sock, addr):
#
#     from_filename = tkinter.filedialog.askopenfilename()
def process( ip, nome, e3):
    if e3.get() != "":
        TCP_IP = ip.get()
        global Fname
        Fname= nome.get()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = (TCP_IP, TCP_PORT)
        s.connect(addr)
        fileName(s,addr)
    else:
        messagebox.showinfo("Erro", "Nenhum ficheiro escolhido")




def openFile(e):
    global fname
    filename = askopenfilename()
    fname = filename
    e.insert(100,filename)

def start():
    master = Tk()
    master.geometry("400x100")
    Label(master, text="Machine Ip").grid(row=0,sticky=W)
    Label(master, text="File for naming").grid(row=1,sticky=W)
    Label(master, text="File").grid(row=2, pady = 4, sticky =W+E)



    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)



    e1.grid(row=0, column=1,sticky =W)
    e2.grid(row=1, column=1,sticky =W)
    e3.grid(row=2, column=1,sticky =W+E)
    e1.insert(15, "192.168.1.")
    master.columnconfigure(1, weight=1)

    B1= Button(master, text='Quit', command=master.quit).grid(row=3, column=1, pady=4,sticky=W+E)
    B2=Button(master, text='Send', command=(lambda : process(e1,e2,e3))).grid(row=3, column=0,pady =4, sticky=W+E)
    B3=Button(master, text='Open', command=(lambda : openFile(e3))).grid(row=2, column=5, sticky=W+E, pady=4)

    mainloop()
if __name__ == "__main__":
    start()



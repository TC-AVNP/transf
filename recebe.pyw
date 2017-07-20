import socket,sys,os
import socket
from tkinter import Text
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

SOCKET_LIST = []    # lista de sockets abertos
RECV_BUFFER = 1024
PORT = 5000

print('O ip: ', socket.gethostbyname(socket.gethostname()))


def nameFile(conn, addr):
    Udata= conn.recv(RECV_BUFFER)
    data= Udata.decode()
    print(data)
    stringToSend= 'OK'
    conn.sendto(stringToSend.encode(),addr)
    with open(data, 'wb') as f:
        while True:
            pack = conn.recv(1024)
            if not pack:
                break
            # write pack to a file
            f.write(pack)
    f.close()
    messagebox.showinfo("Done", "Ficheiro recebido")
    sys.exit(0)



def start(s):
    conn, addr = s.accept()
    nameFile(conn, addr)


def quit():
    sys.exit(0)

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))  # aceita ligaoees de qualquer lado
    server_socket.listen(10)

    print("Server started on port %d" % (PORT,))

    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.bind((TCP_IP, TCP_PORT))
    # s.listen(1)


    while 1:

        master = Tk()
        master.geometry("130x60")
        Label(master, text="Machine Ip").grid(row=0, sticky=W)
        e1 = Entry(master)
        e1.grid(row=0, column=1, sticky=W)
        e1.insert(15, socket.gethostbyname(socket.gethostname()))

        B2 = Button(master, text='Start', command=(lambda: start(server_socket))).grid(row=1, column=0, pady=4,
                                                                                     sticky=W+E)
        B1 = Button(master, text='Quit', command=quit).grid(row=1, column=1, pady=4, sticky=W)

        mainloop()


        # if not data: break
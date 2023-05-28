import socket
import sys # In order to terminate the program

#Membuat socket TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Server address dan port
serverHost = '127.0.0.1'
serverPort = 8080

#Mengaitkan socket ke alamat dan port tertentu
serverSocket.bind((serverHost, serverPort))

#Menerima koneksi 
serverSocket.listen(1) #Hanya satu koneksi yang dapat masuk

print(f"Server berjalan di {serverHost}:{serverPort}")

while True:
    #Menerima koneksi dari client
    connectionSocket, addr = serverSocket.accept()
    try:
        #Menerima message dari client
        message = connectionSocket.recv(1024).decode() 
        filename = message.split()[1] #mengambil path file yang diminta client
        
        f = open(filename[1:]) #membuka file yang diminta
        outputdata = f.read() #membaca file 
        f.close() #menutup file
        
        #Membuat response message jika file sesuai
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        response += outputdata 
        
        #Mengirim response message ke client      
        connectionSocket.sendall(response.encode())
        connectionSocket.close() #menutup connection socket
    
    except IOError:
        # Membuka file 404notfound.html
        f = open("404notfound.html") #membuka file 404 not found
        outputdata = f.read() #membaca file 
        f.close() #menutup file

        # Membuat response message jika file tidak sesuai
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        response += outputdata

        # Mengirim response message ke client
        connectionSocket.sendall(response.encode())
        connectionSocket.close() #menutup connection socket

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
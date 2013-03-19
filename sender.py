#========================================================================  

 #   FileName: ChatRoomClientR.py  

 #     Author: Zhu Di  

 #      Email: mskimizd@gmail.com  

 #   HomePage: http://www.codejoke.co.cc/  

 # LastChange: -- ::  
 #========================================================================  

from socket import * 

    

HOST = 'localhost' 

PORT = 8080 
BUFSIZE =  1024

ADDR = (HOST,PORT)  

    

tcpClientSocket = socket(AF_INET,SOCK_STREAM)  

tcpClientSocket.connect(ADDR)  

    

while True:  

     try:  

         data = tcpClientSocket.recv(BUFSIZE)  

         if not data:  

             break 

         print data.strip()  

     except Exception, e:  

         print "xxx" 

         tcpClientSocket.close() 

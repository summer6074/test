

 #========================================================================  

 #   FileName: ChatRoomClientW.py  

 #     Author: Zhu Di  

 #      Email: mskimizd@gmail.com  

 #   HomePage: http://www.codejoke.co.cc/  

 # LastChange: -- ::  

 #========================================================================  



 from socket import * 

    

 HOST = 'localhost' 

 PORT =  

 BUFSIZE =  

 ADDR = (HOST,PORT)  

    

 tcpClientSocket = socket(AF_INET,SOCK_STREAM)  

 tcpClientSocket.connect(ADDR)  

    

 while True:  

     try:  

         data = raw_input('> ')  

         if not data:  

             break 

         tcpClientSocket.send('%s\r\n' %data)  

     except Exception, e:  

         print "xxx" 

         tcpClientSocket.close() 

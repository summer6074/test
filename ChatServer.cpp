//============================================================================
// Name        : ChatServer.cpp
// Author      : Lei
// Version     :
// Copyright   : 
// Description : ChatServer in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
//#include "ServerSocket.h"
#include "EpollServerSocket.h" //use epoll server
#include "SocketException.h"
using namespace std;

int main()
{
    cout<<"Running server..."<<endl;
    try
    {
       // ServerSocket server(8080);
        EpollServerSocket server(8080);
       /*       
	   while(true)
        {
            Socket newSocket;
            server.Accept(newSocket);

            try
            {
                string message;
                server.Receive(newSocket,message);
                cout<<"Receive message: "<<message<<endl;
                message="Here is server";
                server.Send(newSocket,message);
            }
            catch(SocketException&){}
        }
		*/
	    server.run();
		
		
		
		
    }
    catch(SocketException& ex)
    {
         cout << "Exception was caught:" << ex.Description() << "\nExiting.\n";
    }
    return 0;
}
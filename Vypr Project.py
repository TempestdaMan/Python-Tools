import ftplib
from ftplib import *
import tkinter
from tkinter import messagebox


choice = ""

print("Made by Tempest#8933 | SphinxNET | Version: 1.1.0")

try:
    ftp = FTP(input("FTP: "))

except:
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showerror("[ERROR. GENERAL]", "Check if URL is correct!")
    quit()
    
user = input("User: ")
password = input("Password: ")

try:
    ftp.login(user, password)
    print("Access Granted!")
    print("---------------")
    
except:
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showerror("[ERROR. LOGIN]", "Wrong username or password. ACCESS DENIED!")
    quit()


def accessedftp():

    choice = input("C: ") #dir
    if choice == "dir":
        if ftp:
            print("\n".join(ftp.nlst()))

    elif choice == "rename": #rename
        if ftp:
            fromname = input("Old Name: ")
            toname = input("New Name: ")
            try:
                ftp.rename(fromname, toname)
                print(fromname, "=>", toname)
            except:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror("[ERROR. PERMISSION]", "Not enough permissions or wrong old name!")

    elif choice == "delete": #del
        if ftp:
            filename = input("Filename: ")
            try:
                ftp.delete(filename)
                print("File successfully deleted!")
            except:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror("[ERROR. PERMISSION]", "Not enough permissions or wrong name of the file.")

    elif choice == "cd": #cd
        if ftp:
            pathname = input("Path: ")
            try:
                ftp.cwd(pathname)
                print("Directory changed!")
            except:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror("[ERROR. PATH]", "Invalid path!")

    elif choice == "mkdir": #mkdir
        if ftp:
            mkdirpathname = input("Path: ")
            try:
                ftp.mkd(mkdirpathname)
                print("Directory successfully created!")
            except:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror("[ERROR. PERMISSION]", "Your FTP Account does not have the permission to do this.")

    elif choice == "pwd": #check current directory
        if ftp:
            try:
                print(ftp.pwd())
            except:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror("[ERROR. UNKNOWN]", "Contact Tempest#8933 on Discord.")

    elif choice == "sf": #send file
        if ftp:
            try:
                file = input("File: ")
                mode = input("Mode: ")
                sendfile = open(file, mode)
                ftp.storbinary("STOR" + file, mode)
                file.close()
            except:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror("[ERROR. PERMISSION OR INVALID PATH]", "Invalid path or permission failure!")

    elif choice == "copy": # copy file
        if ftp:
            try:
                file = input("File: ")
                mode = input("Mode: ")
                ftp.retrbinary("RETR" + file, mode)
                file.close()
            except:
                root = tkinter.Tk()
                root.withdraw()
                
                messagebox.showerror("[ERROR. PERMISSION OR INVALID PATH]", "Invalid path or permission failure!")

    elif choice == "q": #quit
        if ftp:
            try:
                ftp.quit()
            except:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror("[ERROR. QUITTING]", "Did not work! Program closes automatically!")
                quit()

    elif choice == "close": #close connection
        if ftp:
            try:
                ftp.close()
            except:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror("[ERROR. CLOSING]", "Failed to close connection!")

    elif choice == "size": #size of file
        if ftp:
            try:
                file = input("File: ")
                print(ftp.size(file), "Bytes")
            except:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror("[ERROR. INVALID FILE OR SIZE RETRIEVE FAIL]", "Failure to retrieve size or invalid file!")

    elif choice == "rmd": #remove directory
        if ftp:
            try:
                dir = input("Directory: ")
                ftp.rmd(dir)
            except:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showerror("[ERROR. PERMISSION OR INVALID DIRECTORY]", "Invalid directory or no permission to do this!")

    elif choice == "commands":
        if ftp:
            print("dir = list files in directory", "rename = rename files", "delete = delete files", "cd = change directory", "pwd = check directory", "mkdir = create directory", "sf = send files", "copy = copy files", "q = quit", "close = close connection", "size = size of file", "rmd = remove directory", sep = "\n")


WLoop = True
while WLoop:
    accessedftp()

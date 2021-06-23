#!/usr/bin/python3
# This code write by Mr.nope
import os
import platform
plat = platform.uname()[0]
class SM:
    SM_Version = "SM 1.3.0"
    def system(command):
        """
        Enter command!
        """
        os.system(command)
    def mkdir(file):
        """
        Enter Folder Name!
        """
        os.system("mkdir " + file)
    def mkfile(file2):
        """
        Enter file name!
        """
        if plat == 'Windows':
            print("\nThis Programm Run on Linux, MacOS\n")
        else:
            os.system("touch " + file2)
    def rmdir(file3):
        """
        Enter Folder Name!
        """
        if plat == 'Windows':
            os.system("rmdir " + file3)
        elif plat == 'Linux':
            os.system("rmdir " + file3)
        elif plat == 'Mac':
            os.system("rmdir " + file3)
        else:
            print("\nPlease, Run This Programm on Windows, Linux, Mac\n")
    def rmfile(file4):
        """
        Enter file name!
        """
        if plat == 'Windows':
            os.system("del " + file4)
        elif plat == 'Linux':
            os.system("sudo rm -r " + file4)
        elif plat == 'Mac':
            os.system("rm -r " + file4)
        else:
            print("\nPlease, Run This Programm on Windows, Linux, MacOS\n")

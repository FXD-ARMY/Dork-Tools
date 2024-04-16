import os
import sys
import time

os.system("clear")
print("\033[32;1m ")
os.system("figlet DORK TOOLS")
print("===============")
print("FXD Dork Tools")
print("===============")
print("1)Dork In Sql")
print("2)Dork In Xss")
print("3)Dork In Lfi")
print("4)About")
print("5)Exit")
print("===============")
select = input("What Select: ")
if select == "1":
	os.system("clear")
	print("=============")
	print("Dork Sql")
	print("=============")
	print("Please Wait....")
	time.sleep(1)
	f = open("sql.txt", "r")
	print(f.read())
	print("=============")
elif select == "2":
	os.system("clear")
	print("=============")
	print("Dork Xss")
	print("=============")
	print("Please Wait....")
	time.sleep(10)
	f2 = open("xss.txt", "r")
	print(f2.read())
	print("=============")
elif select == "3":
	os.system("clear")
	print("=============")
	print("Dork Directory Listing ")
	print("=============")
	print("Please Wait....")
	time.sleep(10)
	f3 = open("lfi.txt", "r")
	print(f3.read())
	print("=============")
elif select =="4":
	print("this tools use to search web vuln with dork")
elif select =="5":
	print("Good Bye")
else:
	print("What Are You Doing?")
	
	
	


	
	
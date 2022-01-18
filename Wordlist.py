import os
from itertools import product

#Requirements installations works only on shell or terminal
def install():
    os.system("pip3 install pyfiglet")
    os.system("clear")
print("[+]Installing Requirements...")
install()
import pyfiglet

#collecting basic info about the target w
def basicinfo():
    global basicinfo
    print("BASIC INFO OF THE TARGET\n(Press enter to leave it blank)")
    fname = str(input("First Name: "))
    mname = str(input("Middle Name:"))
    lname = str(input("Last Name: "))
    bdate = str(input("Date of birth: "))
    bmonth = str(input("Month of birth: "))
    byear = str(input("Year of birth: "))
    basicinfo = [fname,mname,lname,bdate,bmonth,byear]

#collecting advance info or more info about the target
def adinfo():
    global adinfo
    global keywords
    global keylists
    os.system("clear")
    print("ADDITIONAL INFO OF THE TARGET\n(Press Enter to leave it blank)")
    faname = str(input("Father Name:"))
    moname = str(input("Motheer Name:"))
    adinfo = [faname,moname]
    nobro = input("how many brother does your target has:")
    if nobro != "":
        for i in range(int(nobro)):
            rebro = str(input("enter the brother name:"))
            adinfo.append(rebro)
        print(adinfo)
    nosis= input("how many sister does your sister has:")
    if nosis != "":
        for i in range(int(nosis)):
            resis = str(input("enter the sister name:"))
            adinfo.append(resis)
        print(adinfo)
    os.system("clear")

    #Collecting more keywords about the target
    print("ADDING MORE KEYWORDS ABOUT TARGETS")
    print("(use comma to seperate the keywords)")
    readeri=str(input("Keywords>>"))
    keywords = list(readeri.split(sep=','))
    print(keywords)
    adinfo.append(keywords)
def keylists():
    keylists = basicinfo + adinfo
    print(keylists)
def banner():
    banner = pyfiglet.figlet_format("WORDLIST GENERATOR")
    print(banner)
    print("                                      Coded by AdMin")

print("This Tool is Made For Generating Wordlist Upon Your Target")
print("1. Press Enter to continue")
print('2. Readme')

choice=input(">>")
if choice == '':
    os.system("clear")
    basicinfo()
    adinfo()
    keylists()
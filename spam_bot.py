import socket
import pyautogui
import random
import functools
import time 
import colored
import termcolor


def spam():
 
    try:
        print(termcolor.colored("[+]","blue")+termcolor.colored("Spam ready to attack","yellow"))
        
        with open('GHOST/Virus_attack/gun_logo','r') as file:
           s = file.read()
           print(termcolor.colored(s,"blue"))
           
           
        print(termcolor.colored("          "+"Please enter your cursor to whatsapp text bar","red"))
        
        #--Asking some questions to run the program as friend--------
        
        num_Omsg = int(input(termcolor.colored("[+]","blue")+termcolor.colored("how many msg do you want to send : ","yellow")))
        delay = int(input(termcolor.colored("[+]","blue")+termcolor.colored("how many time do you wat to ready({}) : ","yellow").format(termcolor.colored("Secounds","blue"))))
        num_Ochar = int(input(termcolor.colored("[+]","blue")+termcolor.colored("how many charactors do you want to type in one msg(INT) : ","yellow")))
        
        
        print(termcolor.colored("[+]","blue")+termcolor.colored("Ghost start within "+str(delay)+"secounds","green"))
        time.sleep(delay)
        letters =["a","b","c","d","e","f","g","h","i","j","k",  "l","m",    "n","o","p","q","r","s","t","u","v","w","x",  "y","z",1,2,3,4,5,6,7,8,9,"!","@","#","$","%","^","&"] 
        msg_count = 0
        for i in range(num_Omsg):
            let = random.choices(letters,k=num_Ochar)
            final_text = functools.reduce(lambda x,y: str(x)    +str(y) ,   let)
            pyautogui.write(final_text)
            pyautogui.press("enter")
            msg_count+=1
            print(termcolor.colored("[+]","blue")+termcolor.colored(str(msg_count),"red" )+ termcolor.colored(" msg successfuly sent","green"))
            time.sleep(0.5)
        time.sleep(2)    
    except ValueError:
        print(termcolor.colored("[+]","blue")+termcolor.colored("please Enter an integer number","yellow"))
        reAttack()
     
    except KeyboardInterrupt:
        print(termcolor.colored("[+]","blue")+termcolor.colored("OK....Ghost stop his work(spam)","green"))
        print(termcolor.colored("[+]","blue")+termcolor.colored("Thanks for your trust","green"))
        
    finally:
        print("          "+"Successfully attacked your enemy....(GHOST)")       
        with open('GHOST/Virus_attack/ghost_logo','r') as file:
           s = file.read()
           print(termcolor.colored(s,"red"))

def reAttack():
    responce =input(termcolor.colored("[+]","blue")+termcolor.colored("Do you want to attack again(Y/n)","yellow"))
    responce.lower()
    print(responce)
    if responce == "y":
        spam()
    elif responce == "n":
        print("[+]thank you for use me") 
            
spam()
while reAttack():
    spam()            

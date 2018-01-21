import os

choices=[1,2,3]

def print_menu():
    print("                      ------------------------ ")
    print("                     |    1.Add new Data      |")
    print("                     |    2.View Datas        |")
    print("                     |    3.Exit Program      |")
    print("                      ------------------------ ")
    print("Enter Your choice(1/2/3)")
    user_choice=1
    user_choice=input("---------->")
    while (int(user_choice) not in choices):
        print("ERROR!!!! ENTER VALID INPUT")
        print("Enter Your choice(1/2/3)")
        user_choice=input("---------->")
    if(int(user_choice)==1):
        data_entry()
    elif(int(user_choice)==2):
        data_display()
    elif(int(user_choice)==3):
         clear = lambda: os.system('cls')
         clear()
         print("THANKS FOR USING MY PROGRAM")   
        

def data_entry():
    datafile=open("user_datas.txt",'a')
    end_entry=False
    while(end_entry==False):
        name=input("Enter Name")
        salary=input("Enter Salary")
        post=input("Enter Post")
        datafile.write(name+"\n")
        datafile.write(salary+"\n")                                            
        datafile.write(post+"\n")
        user_ask=input("Want more(y/n)")
        if(user_ask=="n"):
            end_entry=True
            datafile.close()
            clear = lambda: os.system('cls')
            clear()
            print_menu()

def data_display():
    files = open("user_datas.txt",'r') 
    filelines=files.readlines() 
    lines_number=int(len(filelines)/3)
    print(lines_number)
    lines=0
    x=0
    for y in range(0,lines_number):
        print("Name:"+filelines[x]+"Salary"+filelines[x+1]+"Post:"+filelines[x+2])
        print("____________________________________________________________________")
        x=x+3
    key=input("Press ENTER to continue")
    files.close()
    clear = lambda: os.system('cls')
    clear()
    print_menu()
    
    
print_menu()

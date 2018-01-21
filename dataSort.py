import os
clear = lambda: os.system('cls')
clear()

datas=[]
get_data=True

user_input=0
while(get_data==True):
    user_input=input("Enter a number")
    datas.append(user_input)
    user_choice=input("Want to continue(y/n)")
    if(user_choice=="n"):
        get_data=False

data_size=len(datas)
for x in range(0,data_size):
    for y in range(0,data_size):
        if(datas[x]<datas[y]):
            datas[x],datas[y]=datas[y],datas[x]

print(datas)
    

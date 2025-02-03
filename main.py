'''
we will be using 
1 for snake
-1 for water 
0 for gun

'''
import random
computer=random.choice([1,-1,0])

you=(input("enter your choice:"))
you_dict={"snake":1,"water":-1,"gun":0}
computer_dict={1:"snake",-1:"water",0:"gun"}
you=you_dict[you]


print(f"you chose :{computer_dict[you]}\ncomputer chose :{computer_dict[computer]}")
        

if(computer==you):
    print("Its a Draw")
else:
    if(computer==-1 and you ==1):
        print("YOU WON!")
    elif(computer==-1 and you ==0):
        print("YOU LOSE!")
    elif(computer==1 and you ==-1):
        print("YOU LOSE!")
    elif(computer==1 and you ==0):
        print("YOU WON!")
    elif(computer==0 and you ==1):
        print("YOU LOSE!")
    elif(computer==0 and you ==-1):
        print("YOU WON!")
    else:
        print("something went wrong")    
            


        
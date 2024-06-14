import time
import numpy as np
import getpass
from tabulate import tabulate


def counter(number,p1_name,p2_name):
    fails=['Try harder','Nah','Use your intuition','Pretty close','Incorrect :/']
    number_list=list(number)
    dummy_list=list(number)
    p_count=0
    out=['_' for i in range(len(number))]
    while True:
        guess_val=input(f"{p2_name} enter a digit :")
        if guess_val.isdigit() and len(guess_val)==1:
            p_count+=1
            if guess_val in number_list:
                ind=dummy_list.index(guess_val)
                dummy_list[ind]='*'
                out[ind]=guess_val
                print("".join(out))
            else:
                print(np.random.choice(fails))
            if out==number_list:
                print("Got it !")
                return p_count
        
        elif guess_val.isdigit()==False:
            print("Enter a proper digit")
        elif len(guess_val)>1:
            print("Enter only a single digit")
        elif len(guess_val)<1:
            print("Kindly Enter a digit")


p1_name=input("Enter name for player 1 : ")
p2_name=input("Enter name for player 2 : ")
print(f'{p2_name} kindly close your eyes')
number=getpass.getpass(f'Enter the multidigit number you want {p2_name} to guess : ')
num_length=len(number)
number_list=list(number)

p1_count=counter(number,p1_name,p2_name)

head=[f'{p2_name}'+' try count',f'{p1_name}'+' try count']
data=[[p1_count,'NA']]
print(tabulate(data, headers=head, tablefmt="grid"))
print("\n")
print("Lets turn the tables around")

number2=getpass.getpass(f'Enter the multidigit number you want {p1_name} to guess : ')
while len(number2)!=num_length:
    print("Please provide equal number of digits for fair evaluation")
    number2=getpass.getpass(f'Enter the multidigit number you want {p1_name} to guess : ')
p2_count=counter(number2,p2_name,p1_name)
data[0][1]=p2_count
print(tabulate(data, headers=head, tablefmt="grid"))
if p1_count<p2_count:
    print(f'{p2_name} wins')
elif p1_count>p2_count:
    print(f'{p1_name} wins')
else:
    print("Its a tie")




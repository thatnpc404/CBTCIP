#Rock paper scissor vs computer

import numpy as np
import time

def winner(user,computer):
    print("user :",user,", computer :",computer)

    t1=sorted([user,computer])
    if user==computer:
        return 'Tie'
    elif (t1[0],t1[1]) in values.keys():
        winning_entity=values[(t1[0],t1[1])]
        return 'user' if winning_entity==user else 'computer'

entities=['rock','paper','scissor']
values={('paper','rock'):'paper',('paper','scissor'):'scissor',('rock','scissor'):'rock'}
mapping={'rock':'1','paper':'2','scissor':'3'}
user=input('1.Rock\n2.Paper\n3.Scissor\nEnter your choice : ')
while user.isdigit()==False or len(user)!=1 or int(user) not in range(1,4):
    user=input('Enter proper choice : ')
user=[i for i,j in mapping.items() if j==user]
computer=np.random.choice(entities)
print('----------------------------------')
print('Winner :',winner(user[0],computer))
print('----------------------------------')





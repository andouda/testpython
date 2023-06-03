import random
n1=int(input('自分の手(0…グー,1…チョキ,2…パー)=> '))
h=['グー','チョキ','パー']
print('自分の手',h[n1])

n2=random.randint(0,2)
print('PCの手',h[n2])

if   (n1==0 and n2==1) or (n1==1 and n2==2) or (n1==2 and n2==0):
     print('自分の勝ち')
elif (n1==n2):
     print('あいこです。')
else:
    print('PCの勝ちです')
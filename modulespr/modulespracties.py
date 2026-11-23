# import math
# print(math.sqrt(25))
# print(math.ceil(25.1))
# print(math.floor(25.9))
# print(math.factorial(5))
# print(math.pow(5,3))
# print(math.pi)
# print(math.gcd(36,60))
# print(math.inf)

# import random,math
# num = math.floor(random.random()*100)
# no_of_chaces=0
# while(True):
#     guess = int(input("guess the number: "))
#     no_of_chaces+=1
#     if(guess==num):
#         print("congratulations you are correct🥰🥰🥰")
#         if(no_of_chaces==1):
#             print("golden medal")
#         elif(no_of_chaces==2):
#             print("silver medal")
#         elif(no_of_chaces):
#             print("bronze medal")
#     elif(guess>num):
#         print("you are to high: ")
#     elif(guess<num):
#         print("you are to low")

# import random,math
# items=['chicken', 'mutton', 'prawns']
# print(random.choice([1,2,3,4,5]))
# print(random.randint(2,10))
# print(random.sample(['chicken', 'mutton', 'prawns'],k=1))
# random.shuffle(items)
# print(items)

# from collections import Counter
# a=[1,2,3,4,5,1,2,4,5]
# for key , val in Counter(a).items():
#     if(val==1):
#         print(f"uniquee val {key}")
#     else:
#         print(f"duplicates {key}")

# k=Counter([1,2,3,4,5,1,2,4,5])
# print(k.most_common(1))

# import turtle
# t=turtle.Turtle()
# t.shape('turtle')
# t.pencolor('red')
# t.pensize(10)
# t.speed(10)
# t.fillcolor('green')
# for i in range(10):
#     t.begin_fill()
#     t.circle(100)
#     t.left(40)
#     t.end_fill()

# from datetime import date,datetime,timedelta
# from zoneinfo  import ZoneInfo
# print(date.today())
# print(datetime.now(ZoneInfo('Asia/Kolkata')))
# print(datetime.now(ZoneInfo('Asia/Kolkata')).strftime('%y-%m-%d %H: %m:%S %TZ'))
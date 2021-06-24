# # def count(words):
# #     c=0
# #     for i in words:
# #         if len(i)>1 and i[0]==i[-1]:
# #             c+=1
# #             print(i)
# #     return c
# # print(count(['a2aa','a2ba','123','123']))
#
# # print("enter the number of strings")
# # n=int(input())
# # list=[]
# # for i in range(n):
# #     print("enter the string",i+1)
# #     str=input()
# #     list.append(str)
# # #print(list)
# # def count(strings):
# #     c=0
# #     for x in strings:
# #         if len(x)>1 and x[0]==x[-1]:
# #             print(x)
# #             c+=1
# #     return c
# # print(count(list))
#
# # str=input("enter the string")
# # ch=str[0]
# # str= str.replace(ch,"$")
# # str=ch+str[1:]
# # print(str)
#
# # str=input("enetr the string")
# # if len(str)<2:
# #     print("")
# # else:
# #     new_str=str[0:2]+str[-2:]
# # print(new_str)
#
# # str=input("enter the string")
# # dict={}
# # for x in str:
# #     k=dict.keys()
# #     #print(k)
# #     if x in k:
# #         dict[x]+=1
# #     else:
# #         dict[x]=1
# # print(dict)
#
# # str=input('enter the string')
# # s=str[-1:]+str[1:-1]+str[:1]
# # print(s)
#
#
# # print('welcome to the lab')
# # m=input("enter the letter")
# # n=ord(m)
# # print(n)
# # if n>=97 and n<=109:
# #     print("first half")
# # elif n>=110 and n<=122:
# #     print('second half')
# # elif n>=65 and n<=90:
# #     b=int(input("enetr the number"))
# #     if b%2==0:
# #         print("even number")
# #     else:
# #         print('odd number')
#
# # n=int(input("enter the number1 between 5 and 15"))
# # m=0
# # while True:
# #     if not (n>=5 and n<=15):
# #         n=int(input("enter the number1 between 5 and 15"))
# #     elif not (m>=5 and m<=15):
# #         m=int(input("enter the number2 between 5 and 15"))
# #     else:
# #         break
# # result=(m*n)%60
# # str=input("enter any string")
# # for i in range(result):
# #     print(str,i+1)
#
# def f(a,b):
#     c=a+b
#     d=a+b
#     e=a*b
#     return c,d,e
# res=s,d,m=f(12,34)
# print(res)
#
# def f1(a):
#     p=a
#     print(p)
# f1(12)
# def f1(a,b):
#     p=a+b
#     print(p)
# f1(12,13)
# #f1(14)
#
# def add(d,*g):
#     if d=='intt':
#         ans=0
#     if d=='strr':
#         ans='   '
#     for x in g:
#         ans=ans+x
#     print(ans)
# add('intt',2,3,6)
# add('strr','wer','12')
#
# r=lambda s,e:s+3+e
# print(r(2,3))
#
# z=[1,2,3,4]
# print(help(z.insert))
#
# print(id(z))
# cd=z
# cd=[2,3]
# print(id(cd))
# print(z)


# # importing the time module
# import time
#
# # welcoming the user
# name = input("What is your name? ")
#
# print
# ("Hello, " + name, "Time to play hangman!")
#
# print(" ")
#
# # wait for 1 second
# time.sleep(1)
#
# print("Start guessing...")
# time.sleep(0.5)
#
# # here we set the secret
# word = "secret"
#
# # creates an variable with an empty value
# guesses = ''
#
# # determine the number of turns
# turns = 10
#
# # Create a while loop
#
# # check if the turns are more than zero
# while turns > 0:
#
#     # make a counter that starts with zero
#     failed = 0
#
#     # for every character in secret_word
#     for char in word:
#
#         # see if the character is in the players guess
#         if char in guesses:
#
#             # print then out the character
#             print(char,)
#
#         else:
#
#             # if not found, print a dash
#             print("_",)
#
#             # and increase the failed counter with one
#             failed += 1
#
#             # if failed is equal to zero
#
#     # print You Won
#     if failed == 0:
#         print("You won")
#
# # exit the script
#     break
#
#
#
# # ask the user go guess a character
# guess = input("guess a character:")
#
# # set the players guess to guesses
# guesses += guess
#
# # if the guess is not found in the secret word
# if guess not in word:
#     # turns counter decreases with 1 (now 9)
#     turns -= 1
#
#     # print wrong
#     print("Wrong")
#
# # how many turns are left
# print("You have", + turns, 'more guesses')
#
# # if the turns are equal to zero
# if turns == 0:
#     # print "You Lose"
#     print("You Lose")

#!D:/python3.8/python
import cgi
print("Content-Type:text/html")
print()
print("<h1>Welcome to Python</h1>")
#username=input("enter your name")
form=cgi.FieldStorage()
username=form.getvalue("name")


import pymysql
import time
import datetime
#import mysql.connector
ts=time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
conn=pymysql.connect(host="localhost", user="root",password="",db="my_python")
print("connected")
# myCursor=conn.cursor()
# myCursor.execute("""CREATE TABLE users
# (
# id int primary key,
# name varchar(20)
# )
#
# """)
# myCursor.execute('''INSERT into names(id, name)
# value(1,'priti');''')
# conn.commit()
# conn.close()
try:
    with conn.cursor() as cursor:
        sql = "INSERT INTO names (`name`,`Date`) VALUES (%s,%s)"
        sql1 = "SELECT `id`, `name`, `Date` FROM names "
        try:
            cursor.execute(sql, (username,timestamp))
            print("Task added successfully")
            cursor.execute(sql1)
            result=cursor.fetchall()
            print("Id\t\t Name\t\t\t\t\tDate")
            print("---------------------------------------------------------------------------")
            for row in result:
                print(row[0],"\t\t",row[1],"\t\t\t" , row[2])
        except:
            print("Oops! Something wrong")

    conn.commit()
finally:
    conn.close()
print("<h3>record inserted successfully</h3>")
print("<>")
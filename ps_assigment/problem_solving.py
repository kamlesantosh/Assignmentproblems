# s = input("enter a string: ")
# rev =""
# for i in s:
#     rev=i+rev
# print(rev)
# if s==rev:
#     print("it is an palindrom")
# else:
#     print("it is not an palindrom")

# n=input(" ")
# temp=n
# rev=""
# i=0
# for ch in n:
#     i=i+1
# i-=1
# while i>=0:
#     rev=rev+n[i]
#     i=i-1
# print(rev)
# if n==rev:
#     print("it is an palindrom")
# else:
#     print("it is not palidrom")

# n=input("enter the string: ")
# vowels_count=0
# consonants_count = 0
# for i in n:
#     if i in 'aeiou':
#         vowels_count+=1
#     else:
#         consonants_count+=1
# print('vowels =', vowels_count,'consonants = ',consonants_count)


# # finr the different between  largest and smallest element
# arr = [10,5,25,8,15]
# larg = arr[0]
# small = arr[0]
# for i in arr:
#   if i > larg:
#     larg=i
#   elif i < small :
#     small=i
# diff = larg - small
# print(larg, small)
# print(diff)

# # --------
# a = [1,0,8,0,9,4,0]
# zero=[]
# nonzero=[]
# for i in a:
#   if i==0:
#     zero.append(i)
#   else:
#     nonzero.append(i)
# print(nonzero+zero)
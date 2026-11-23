# a = [10, 25, 8, 45, 32, 15]
# largest = 0
# for  i in a:
#   if i > largest:
#     largest = i
# print(largest)

# a = [1, 2, 2, 3, 1, 4, 2, 3]
# d = {}
# for i in a:
#   if i in d:
#     d[i]+=1
#   else:
#     d[i]=1
# print(d)

# n=7
# count=0
# for i in range(1,n+1):
#   if(n%i==0):
#     count+=1
# if(count==2):
#   print("this is a prime")
# else:
#   print("this is not a prime")

# a = 5
# fact = 1
# for i in range(1,a+1):
#   fact*=i
# print(fact)

# Reverse an Integer
# n=12345
# rev=0
# while n>0:
#   digit = n%10
#   rev = rev*10+digit
#   n=n//10
# print(rev)


# a=12
# b=18
# min_val=min(a,b)
# largest=0
# for i in range(1,min_val+1):
#   if(a%i==0 and b%i==0):
#     largest=i
# print(largest)

# a='123456'
# count=0
# for i in a:
#   if i>= '0' and i<= '9':
#      count+=1
# if count==len(a):
#   print(True)
# else:
#   print(False)



# a = [4, 8, 15, 16, 23, 42]
# total=0
# count=0
# for i in a:
#   total+=i
#   count+=1
# avg = total/count
# print(avg)

# a ="infosys"
# result =" "
# for i in a:
#   if i>='a' and i<='z':
#     result = result+chr(ord(i)-32)
#   else:
#     result +=i
# print(result)

# arr1 = [1, 2, 3] 
# arr2 = [2, 3, 4]
# result = []
# for i in arr1:
#   if i not in result:
#     result.append(i)
# for i in arr2:
#   if i not in result:
#     result.append(i)
# print(result)


# N=int(input("enter how many commands you want :"))
# list_command = []
# for i in range(N):
#   command = input(f"command{i+1} :")
#   list_command.append(command)
# print(list_command)

# count = 0
# for each_list in list_command:
#   if each_list == './':
#     count=0
#   else:
#     count+=1
# print(count)

# clips_size = int(inpput("enter clips count : "))
# total_clips = []
# for i in range(clips_size):
#   each_clip  = input("enter clip positon and thickness: ")
#   total_clips.append(tuple(map(int, each_clip.split(','))))
# tape_capacity=int(input("enter tape capacity: "))


# a = "this is a pen"
# count = 0
# for i in a.split():
#     count+=1
# print(count)

# count=1
# for i in a:
#     if i==" ":
#         count+=1
# print(count)

# peak a values
#  n = [1,2,3,1]
# for i in range(len(n)):
#     if i==0:
#         if n[i] > n[i+1]:
#             print(n[i],i)
#     elif i==len(n)-1:
#         if n[i] > n[i-1]:
#             print(n[i],i)
#     else:
#         if n[i]  > n[i-1] and n[i] > n[i+1]:
#             print(n[i],i)

# n = [2,2,1,1,1,2,2]
# max_count=0
# max_count=0
# for i in n:
#     count=0
#     for i in c
#     if i%2==0:
#         pass
#     elif i>input:
#         print(i)
        
# d = {}
# for i in n:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print()
# n = [1,2,-3,-1,4,-5]

# ps=[]
# ng=[]
# for i in n:
#     if i>=0:
#         ps.append(i)
#     else:
#         ng.append(i)

# l = []
# for i in range(len(ps)):
#     l.append(ps[i])
#     if i<len(ng):
#         l.append(ng[i])
# print(l)
#arr = [11,2,3,8,19] # in give an array find peak lemant
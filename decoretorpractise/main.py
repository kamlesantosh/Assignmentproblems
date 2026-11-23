# def birthday_dec(fn):
#     def cholate(name):
#         print(f'🎶🎶🎶🎶🎶🎶🎈🎈🎈🎈🎈🎈🎈{name}🎂🎂🎂🎂❤️❤️❤️')
#         fn(name)
#     return cholate
# @birthday_dec
# def ballon_dec(name):
#     print(f'ballon decoration with happy birthday {name} wishes')
# ballon_dec('santosh')
# birthday_dec(ballon_dec('santosh'))


# def ballon_decoration(fn):
#     def cholate(name):
#         print(f"🎈🎈🎈🎈🎈✨{name}✨🎉🎉🎉🎊🎊")
#         fn(name)
#     return cholate

# @ballon_decoration
# def birthday(name):
#     print(f"happy birthday {name}")

# # birthday('rani')
# # birthday('raju')

# ballon_decoration(birthday('rani'))


# def iterate():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# a=iterate()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# def fibnaci():
#     a,b = 0,1
#     while a<100:
#         yield a
#         a,b=b,a+b
# a1 = fibnaci()
# a2=fibnaci()
# print(next(a1))
# print(next(a2),'a2')
# print(next(a1))
# print(next(a2))
# print(next(a1))
# print(next(a2))


# def factorial(num):
#     if num ==0:
#         yield 1
#     fact = 1
#     while num > 0:
#         for i in range(1,num+1):
#             fact*=i
#             yield fact
    
# k = factorial(5)
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))

# def factorial(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact*=i
#     yield fact
# k = factorial(5)
# print(next(k))

# a=iter([0,1,1,2,3,5,8])
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# def bonus(num):
#     return num*num

# def map(arr, fn):
#     total_values=[]

#     for each in arr:
#         total_values.append(fn(each))
#     return total_values
# print(list(map(bonus,[1,2,3])))

# def bonus(num):
#     return num * num

# def map(arr, fn):
#     total_values = []

#     for each in arr:
#         total_values.append(fn(each))

#     return total_values

# print(list(map([1,2,3,4],bonus)))

# arr=[12, 13, 1, 10, 34]
# fisrt_smallest=arr[0]
# secod_smallest=arr[0]
# for i in arr:
#   if i < fisrt_smallest:
#     secod_smallest = fisrt_smallest
#     fisrt_smallest=i
#   elif i < secod_smallest:
#     secod_smallest = i
# print(secod_smallest)

# n = [2, 2, 1, 1, 1, 2, 2]
# d={}
# for i in n:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
# res = 0
# for key,val in d.items():
#     if val>len(n)//2:
#         print(key)

# input = [1, 2, -3, -1, 4, -5]
# pos = []
# neg = []
# for i in input:
#    if i >= 0:
#       pos.append(i)
#    else:
#        neg.append(i)
# print(pos,neg)
# res=[]
# for i in range(len(pos)):
#    res.append(pos[i])
#    res.append(neg[i])
# print(res)
# a =  [1, 2, 3,1]
# left = 0
# right = len(a)-1
# while left < right:
#   mid = (left+right)//2
#   if a[mid] < a[mid+1]:
#      left = mid+1
#   else:
#      right = left
# print(left)

# a=29
# count = 0
# while a >0:
#     rem = a%2
#     if rem == 1:
#         count+=1
#     a=a//2
# print(count)

# n = 29
# count = 0
# while n > 0:
#   rem =  n%2
#   if rem == 1:
#     count+=1
#   n=n//2
# print(count)

# n = 153
# temp = n
# total = 0
# while temp > 0:
#     digit = temp%10
#     total+=digit**3
#     temp=temp//10
# if total==n:
#     print("it is an amstrong number")
# else:
#     print("it is not an amstrong number")

# def amstrong(n,temp,power):
#     if temp == 0:
#         return 0
#     digit =  temp%10
#     return digit ** power+amstrong(n,temp//10,power)

# n=153
# power = len(str(n))
# res =amstrong(n,n,power)
# if res == n:
#     print(True)
# else:
#     print(False)

# def arrsum(arr,n):
#   if n == 0:
#     return 0

#   return arr[n-1]+arrsum(arr,n-1)

# arr =  [1, 2, 3, 4, 5]
# res = arrsum(arr, len(arr))
# print(res)
    
# a ="Infosys hires specialist programmers"
# word=" "
# larg =" "
# count = 0
# max_count=0
# for i in a:
#     if i!=" ":
#         word+=i
#         count+=1
#     else:
#         if count>max_count:
#             larg = word
#             max_count = count
#         word=" "
#         count=0
# if count>max_count:
#     larg = word
# print(larg)


# def decoraction(fn):
#     def bellon(name):
#         print(f"🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈❤️❤️ {name}❤️❤️🎈🎈🎈🎈")
#         fn(name)
#     return bellon

# # @decoraction
# def amozen(name):
#     print("...20 year old....")

# # amozen("congralistions")
# decoraction(amozen('congralistions'))

# n = 29
# bin=""
# count = 0
# while n > 0:
#   rem = n%2
#   if rem == 1:
#     count+=1
#   bin+=str(rem)
#   n=n//2
# rev = " "
# for i in bin:
#   rev+=i
# print(rev)
# print(count)

# move all zeroes to an end
# a = [1,0,8,0,9,4,0]
# zero=[]
# nonzero=[]
# for i in a:
#   if i==0:
#     zero.append(i)
#   else:
#     nonzero.append(i)
# print(nonzero+zero)

# finr the different between  largest and smallest element
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

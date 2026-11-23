# f=open('chat.txt','r')--> code rasi file create cheyali
# print(f.read())

# f=open('chat.py','w')-->+ ah file data add cheystundi
# w-->only create file + data add
# r-->only read
# w+-->both read and write
# after adding data and need to read (cursor last point vutundi)
# cursor ekkada vundi tell()
# cursor point update cheyali seek(0)


# f=open('chat.txt','a')
# f.write('\n ***Ai is **evoluing** day by day...')
# f.seek(0)
# # print(f.read())
# f.close()

# f=open('chat.txt', 'w+')
# f.write('''Hello bujji em cheystunnav 
# inka nidrapoleda 
# ammo varsham paduthundi ''')
# f.seek(0)
# print(f.tell())
# print(f.read())


#open(filname, mode)
# with open('chat.txet','x+') as f:
#     f.write('i can add new data...')
#     print(f.tell())#14
#     f.seek(0)
#     print(f.tell())
#     print(f.read())

#r--> only read
#w-->only write and create file if file not exist old data should be deleted
#w+--> both read and write

#open(filename, mode)
# import json
# with open('chat.json','w') as f:
#     json.dump({'name':'santosh', 'age':24},f) #store cheyadaniki

# with open ('chat.json','r') as f:
#     print(json.load(f))#read the data

#r-->only read
#w--> only write and create file if file not exist old data should be deleted
#w+-->both read and write

# import pickle
# with open('chat.pkl','wb') as f:
#     pickle.dump({'name':'santosh','age':24},f)#pickling

# with open('chat.pkl','rb') as f:
#     print(pickle.load(f))#unpickling


import sys,gc
# a=[1,2,3]
# b=a
# c=b
# c[0]=10
# print(a,b,c)
# del c
# del a
# del b

# class Animal:
#     pass
# a=Animal()
# b=Animal()
# a.friend=a
# b.friend=a
# print(sys.getrefcount(a))
# print(sys.getrefcount(b))
# del a
# del b
# print(gc.collect())#refcounting mechansim unable to clean the unused for cyclic ref thats why i(garbage collection) came into picture
#normal ref vunte reference
#counting mechansim use cheysi
#unused data ni clean cheystundi


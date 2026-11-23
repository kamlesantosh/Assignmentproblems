
import time,threading,multiprocessing
# def restarent(order_item,t):
#     print(f"your biryani {order_item } preparing")
#     time.sleep(t)
#     print(f"your biryani {order_item} readdy")

# not smart code
# starting_time = time.time()
# w1=restarent('chicken biryani',5)
# w2=restarent('mutton biryani',10)
# ending_time = time.time()
# print(f"Totaltimemetaken: {ending_time-starting_time}")


# multiple threading(multiple waters)
# starting_time = time.time()
# w1 = threading.Thread(target=restarent, args=('chicken biryani',5))
# w2 = threading.Thread(target=restarent,args=('mutton biryani',10))
# w3 = threading.Thread(target=restarent,args=('prance biryani',10))
# w1.start()
# w2.start()
# w3.start()
# w1.join()
# w2.join()
# w3.join()
# ending_time = time.time()
# print(f"Totaltimemaken{ending_time - starting_time}")

# starting_time=time.time()
# p1=multiprocessing.Process(target=restarent,args=('chicken biryani',5))
# p2=multiprocessing.Process(target=restarent,args=('mutton biryani',10))
# p3=multiprocessing.Process(target=restarent,args=('prawns biryani',10))
# p1.start()
# p2.start()
# p3.start()
# p1.join()
# p2.join()
# p3.join()
# ending_time=time.time()
# print(f"Totaltimetaken: {ending_time-starting_time}")


# # single process
# starting_time=time.time()
# with multiprocessing.Pool(processes=2) as pool:
#     pool.starmap(restarent,[('chicken biryani',5),('mutton biryani',10),('prawns biryani',10)])
# ending_time=time.time()
# print(f"Totaltimetaken: {ending_time-starting_time}")

# import asyncio

# asyncio def order(order_item,t):
#     print(f"your {order_item} is preparing")
#     await asyncio.sleep(t)
#     print(f"your {order_item} is readdy now...")

# async def main():
#     starting_time=time.time()
#     await asyncio.gather(
#     order('checken birayni',5),
#     order('mutton biryani',10),
#     order('prawns biryani',10)
#     )
#     ending_time=time.time()
#     print(f"total time taken: {ending_time-starting_time}")
        
# asyncio.run(main())
    

#
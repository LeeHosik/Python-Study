# -- Before

# total = 0
# for i in range(0,100000001):
#     total += i

# print(total)

# -- After
from threading import Thread

def calc(start,end):
    total = 0
    for i in range(start, end):
        total += i
    print(total)


if __name__ == "__main__":
    start,end = 0, 100000001
    thr1 = Thread(target = calc, args=(start,end))

    thr1.start()
    thr1.join() # await 한거라고 생가갛면댐
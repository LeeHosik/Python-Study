# from threading import Thread

# def calc(start,end):
#     total = 0
#     for i in range(start, end):
#         total += i
#     print(total)


# if __name__ == "__main__":
#     start,end = 0, 100000001
#     thr1 = Thread(target = calc, args=(start,end))

#     thr1.start()
#     thr1.join() # await 한거라고 생가갛면댐



from multiprocessing import Process

def start_get(start, end):
    total = 0
    for i in range(start,end):
        total += i
    print(total)

if __name__ == "__main__":
    # Process를 생성
    p0 = Process(target=start_get, args=(0,100000000))
    p1 = Process(target=start_get, args=(100000001,200000000))
    p2 = Process(target=start_get, args=(200000001,300000000))

    # start로 각 프로세스를 시작 (무작위 실행)
    p0.start()
    p1.start()
    p2.start()

    # 순서 정렬

    p0.join()
    p1.join()
    p2.join()

    print(">>>> END <<<<")
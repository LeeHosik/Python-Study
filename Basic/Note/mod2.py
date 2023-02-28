def sum(a,b):
    if type(a) != type(b):
        '더하기를 할 수 없습니다'
    else:return a+b

# def star(a,b):
#     for a in b:
#         # result = '*' * a
#         result = '*' * a
#         a += 1
#         return result


if __name__ == "__main__":
    print(sum(1,10))
# with open('data/Linux.txt', 'rb', encoding="utf-8") as f:
#     text = f.read()
#     print(text)

position = 70072
with open('data/Linux.txt', 'rb') as f:
    for i in range(position-1000, position+1000):
        f.seek(i)  # 跳转到指定位置
        byte = f.read(1)  # 读取一个字节
        print(f"{byte.decode('utf-8')}",end="")

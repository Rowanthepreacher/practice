

def bingap(N):
    answer = len(max(bin(N)[2:].strip("0").split("1")))
    print(answer)


bingap(1042)
bingap(32)
bingap(1045675)
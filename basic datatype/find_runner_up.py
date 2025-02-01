if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    temp = []
    for i in arr:
        if i not in temp:
            temp.append(i)
    temp.remove(max(temp))
    print(max(temp))

def collaz():
    print("整数を入力してください")
    try:
        co = int(input())
    except ValueError:
        pass
    if co % 2:
        return co * 3 + 1
    else:
        return co / 2
print(collaz())
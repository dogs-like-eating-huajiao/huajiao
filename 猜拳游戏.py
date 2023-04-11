a=input("a出拳")
b=input("b出拳")
if a=='剪刀':
    if b=='布':
        print("a赢了")
    elif b=='石头':
        print("b赢了")
    elif b=='剪刀':
        print("平局")
elif a=='布':
    if b=='布':
        print("平局")
    elif b=='石头':
        print("a赢了")
    elif b=='剪刀':
        print("b赢了")
elif a=='石头':
    if b=='布':
        print("b赢了")
    elif b=='石头':
        print("平局")
    elif b=='剪刀':
        print("a赢了")
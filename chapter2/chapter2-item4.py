x = list(map(int, input("Enter Your List : ").split()))
x.sort()
outside_lst = []
inner_lst = []

if len(x) <= 2 :
    print("Array Input Length Must More Than 2")

else:
    for f in range(len(x)-2):
        s = f
        inner_lst.append(x[f])

        while s <= (len(x)-2):
            s += 1
            inner_lst.append(x[s])
            t = s
            while t <= (len(x)-2):
                t += 1
                inner_lst.append(x[t])
                if sum(inner_lst) == 5:
                    outside_lst.append(inner_lst.copy()) ### list.copy() ทำให้ตอนเปลี่ยนค่า inner_lst ในลูป ไม่มีผลต่อค่าใน outside_lst
                    for k in range(len(outside_lst)):
                        if len(outside_lst) > 1 and k != len(outside_lst)-1 and outside_lst[len(outside_lst)-1] == outside_lst[k]:
                            outside_lst.pop()
                inner_lst.pop()
            inner_lst.pop()
        inner_lst.pop()
    print(outside_lst)
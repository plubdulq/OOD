print("*** Fun with Drawing ***")
N = int(input("Enter input : "))
row = N*3 - 2
column = N*4 - 3
lower_hrt = 0
for i in range(row):
    if i<N:
        if i == 0:
            print("."*(N-i-1) + "*" + "."*(column - 2*(N-i-1)-2) + "*" + "."*(N-i-1))
        elif i<N-1:
            print("."*(N-i-1) + "*" + "+"*(i*2-1) + "*" + "."*(column-(2*(N-i-1 + (i*2-1)))-4) + "*" + "+"*(i*2-1) + "*" + "."*(N-i-1))
        elif i == N-1:
            print("."*(N-i-1) + "*" + "+"*(i*2-1) + "*" + "."*(2*(N-i-1)-3) + "+"*(i*2-1) + "*" + "."*(N-i-1))
    else:
        lower_hrt += 1
        if i < row-1:
            print("."*(lower_hrt) + "*" + "+"*(column-(2*lower_hrt + 2))  + "*" + "."*(lower_hrt))
        else:
            print("."*lower_hrt + "*" + "."*lower_hrt) 
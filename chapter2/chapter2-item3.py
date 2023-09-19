print("*** New Range ***")
x = list(map(float, input("Enter Input : ").split()))
def check_condition(argument):
    print("(",end = "")
    if argument == 1:
        f_condi = 0
        while f_condi < x[0]:
            print('{0:.1f}'.format(f_condi), end ="")
            f_condi += 1
            if f_condi < x[0]:
                print(", ",end="")

    if argument == 2:
        s_condi = x[0]
        while s_condi < x[1]:
            print('{0:.1f}'.format(s_condi), end ="")
            s_condi += 1
            if s_condi < x[1]:
                print(", ",end = "")

    if argument == 3:
        t_condi = x[0]
        max_value = x[1]
        plus_condi = x[2]
        decimal_point = 0

        while t_condi < max_value:
            while int(t_condi) % 10 != 0 or int(t_condi) == 0:
                decimal_point += 1
                t_condi *= 10
            t_condi /= ((10)**decimal_point)
            print(round(t_condi, decimal_point), end ="")
            decimal_point = 0
            t_condi += plus_condi
            if t_condi<max_value:
                print(", ",end = "")
    print(")",end = "")

check_condition(len(x))

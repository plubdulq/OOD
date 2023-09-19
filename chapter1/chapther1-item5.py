x = list(map(int, input("Enter All Bid : ").split()))
if len(x) <= 1:
    print("not enough bidder")
else:
    x.sort()
    if x[len(x)-1] == x[len(x)-2]:
        print("error : have more than one highest bid")
    else:
        print(f'winner bid is {x[len(x)-1]} need to pay {x[len(x)-2]}')
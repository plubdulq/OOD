print(" *** class MyInt ***")
num1, num2 = input("Enter 2 number : ").split()
class MyInt:
    def __init__(self, num):
       self.num = num

    def toRoman(self):
        decimal = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        print(f'{self.num} convert to Roman : ',end ="")
        while self.num:
            div = self.num // decimal[i]
            self.num %= decimal[i]
            while div:
                print(sym[i],end="")
                div -= 1
            i -= 1
        print("\n",end="")
a = MyInt(int(num1))
b = MyInt(int(num2))
a.toRoman()
b.toRoman()
print(f'{num1} + {num2} = {int((int(num1)+int(num2))*1.5)}')
class funString():

    def __init__(self, cin):
        self.string = cin


    def __str__(self):
        pass
        ### Enter Your Code Here ###

    def size(self) :
        return len(self.string)

    def changeSize(self):
        for i in self.string:
            if i.islower():
                self.string += i.upper()
                self.string = self.string[1:]
            if i.isupper():
                self.string += i.lower()
                self.string = self.string[1:]
        return self.string
        

    def reverse(self):
        return self.string[::-1]

    def deleteSame(self):
        str_list = []
        the_end = ""
        str_list.extend(self.string)
        for i in range(len(self.string)):
            std = i
            while std < len(self.string):
                std += 1
                if str_list[i] != "" and std<len(self.string) and str_list[i] == self.string[std]:
                    str_list[std] = ""
        for i in str_list:
            if i != "":
                the_end += i
        return the_end
                


str1, str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :   print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())
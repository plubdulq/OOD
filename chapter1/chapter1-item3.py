print("*** Reading E-Book ***")
text_list = []
text, hl = input("Text , Highlight : ").split(",")
text_list.extend(text)
for i in range(len(text_list)):
    if hl in text_list[i]:
        text_list[i] = '[' + str(text_list[i]) + ']'
for j in range(len(text_list)):
    print(text_list[j],end="")
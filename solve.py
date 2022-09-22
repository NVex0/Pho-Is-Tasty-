asciiDictionary = {chr(i) for i in range(32,127)}
Flag = ''
Strings = 'CTFlearn{I_Love_Pho!!!}'
for i in Strings:
    if i in asciiDictionary:
        Flag += i
print(Flag)


# Pho-Is-Tasty-

Title của challenge nói là "The flag is hidden in the jpeg file". Vậy nên dùng hexeditor tool để xem hexdata của file.

Ngay đoạn đầu ta đã thấy cái Flag đây rồi :v

![Screenshot (2440)](https://user-images.githubusercontent.com/113530029/191791492-65f6c28a-9b87-49aa-8722-55cd6f5e97cb.png)

Cắt cái đoạn đó ra rồi viết script xoá kí tự linh tinh ở giữa các chữ thôi.

```
asciiDictionary = {chr(i) for i in range(32,127)}
Flag = ''
Strings = 'CTFlearn{I_Love_Pho!!!}'
for i in Strings:
    if i in asciiDictionary:
        Flag += i
print(Flag)
```
`Flag : CTFlearn{I_Love_Pho!!!}`

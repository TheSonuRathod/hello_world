n = int(input('enter the number'))
temp = n
reverseNo = 0
while temp != 0:
    reverseNo = (reverseNo * 10) + (temp % 10)
    temp = temp // 10
if reverseNo == number:
    print('yes :), PALINDROM')
else:
    print('no :ssss(')


print('this changer is made for git experiment')

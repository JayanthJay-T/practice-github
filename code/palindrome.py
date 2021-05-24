num = int(input('enter the number:'))
temp_num = num
res = 0
while num:
    rem = num%10
    res = res*10 + rem
    num =num // 10

print('result:', res)
print('This is palindrome num'  if temp_num == res else 'This is not palindrome num')





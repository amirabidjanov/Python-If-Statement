num = int(input('son kiriting:'))
num2 = int(input('son kiriting:'))
num3 = int(input('son kiriting:'))
if num == num2 == num3:
    print('teng tomonli')
elif num == num2 != num3:
    print('teng yonli')
elif num != num2 == num3:
    print('teng yonli')
elif num != num3 == num2:
    print('teng yonli')
elif num == num3 != num2:
    print('teng yonli')
elif num != num2 != num3:
    print('turli tomonli')
input_change= input('How much change do you get? ')
change= float(input_change)*100
while change<0.0:
    input_change = input('How much change do you get? ')
    change = float(input_change) * 100
change_money = int(change)
cents = 0
while change_money >= 25:
    change_money= change_money-25
    cents= cents+1
while change_money>=10:
    change_money= change_money-10
    cents=cents+1
while change_money>=5:
    change_money= change_money-5
    cents=cents+1
while change_money>=1:
    change_money=change_money-1
    cents=cents+1
print(cents)

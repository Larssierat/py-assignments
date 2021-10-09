input_user= int(input("How high should the pyramid be?: "))
while input_user>23 or input_user<1:
    input_user = int(input("How high should the pyramid be?: "))
height= input_user
for i in range(height, 0, -1):
    for space in range(0,i-1):
        print (end='  ')
    for hashblock in range(0, (height - i + 2)):
        print('# ', end='')
    print()

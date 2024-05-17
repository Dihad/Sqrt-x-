import math
num = int(input('enter the number: '))
current_valid_num = 0
for checking_num in range(num):
    current_valid_num_sqr = checking_num * checking_num
    if current_valid_num_sqr == num:
        print(checking_num)
        break
    if current_valid_num_sqr < num:
        current_valid_num = checking_num
    if current_valid_num_sqr > num:
        print(current_valid_num)
        break
    

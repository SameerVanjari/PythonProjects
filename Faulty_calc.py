# design a calculator which solves all problems correctly except for the given cases
# these are the exceptions 45*3=555, 56+9=77, 56/6=4

# function defining the work of calculator 
def cal(operator, var1, var2):
    if operator == '+':
        if var1 == 56 and var2 == 9:
            print('result = 77')
        else:
            print("result = ", (var1 + var2))
    elif operator == '-':
        print("result =", var1 - var2 )
    elif operator == '*':
        if var1 == 45 and var2 ==3:
            print("result = 555")
        else : 
            print("result =",(var1 * var2))
    elif operator == '/':
        if var1 == 56 and var2 == 6: 
            print("result = 4")
        else:
            print("result = ", (var1/ var2))
    else :
        print('this operation is not available')

# iterate it until prompted so 
ans = 'y'
while(ans == 'y'):
    operator = input("Enter the operator for operation you want to perform = ")
    var1,var2 = int(input("Enter the first variable = ")), int(input("Enter the second variable = "))
    cal(operator, var1, var2)
    ans = input("Do you want another result(y/n) = ")
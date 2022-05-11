#additionfunction
def addition(num1,num2):
    return num1 + num2

#substractionfunction
def subtract(num1,num2):
    return num1 - num2

#multiplicationfunction
def multiplication(num1,num2):
    return num1 * num2

#divisionfunction
def division(num1,num2):
    return num1 / num2


print('Select Operation:','1.Addition','2.Subtraction','3.Multiplication','4.Division')
select = int(input())

n1 = int(input())
n2 = int(input())

if select == 1:
   print(n1,'+',n2,'=',addition(n1,n2))
   
elif select == 2:
    print(n1,'-',n2,'=',subtract(n1,n2))
    
elif select == 3:
    print(n1,'x',n2,multiplication(n1,n2))
    
elif select == 4:
    print(n1,'/',n2,division(n1,n2))
    
else:
    print('Invalid Input')
'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

''' Question 2: Your task is to complete the validate_triangle and validate_rectangle functions for the classes.Hint for validating is given in the

comments of the code. Also you will have to print the following after validation in respective functions:-

1.Invalid Triangle: If the triangle sum property of sides is not valid(More hint in the comments of code)

2.Valid Triangle:If the triangle sum property of sides is valid.

3.Valid Rectangle:If 2 side pairs are same and they are input in correct order like l,b,l,b

4.Invalid Rectangle: If Not Valid rectangle as stated above.'''



def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

# Reading Three Sides

lst_input=list(map(int,input().split()))

# Function call & making decision

if is_valid_triangle(lst_input[0], lst_input[1], lst_input[2]):
    print('Valid Triangle.')
else:
    print('Invalid Triangle.')
    
    
    
    
    
def is_valid_rectangle(a,b,c,d):
    if a==c and b==d:
        return True
    else:
        return False

# Reading four Sides


lst_input=list(map(int,input().split()))

# Function call & making decision

if is_valid_rectangle(lst_input[0], lst_input[1], lst_input[2],lst_input[3]):
    print('Valid Rectangle.')
else:
    print('Invalid Rectangle.')


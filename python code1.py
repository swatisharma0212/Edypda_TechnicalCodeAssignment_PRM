'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

''' Question 1 : You will have a number of elements and in the next n lines element of a list. 
You have to create a list from the given strings. You have to sort the list based on
2nd last character of a string.'''


n=int(input())
string_lst=input().split()
sorted_string=sorted(string_lst, key=lambda x: x[-2])
print(sorted_string)


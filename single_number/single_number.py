'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

'''
UPER
Understand
a list of inegers where every int except one (any 1 - 9) shows up twice

you want to loop through the array, 
count each int twice,
best way to count each int twice? 
if not twice then return value

PLAN
array is passed in
loop through array and count numbers
** integrate count() method in python **
find int with count = 1 
return that int

'''
def single_number(arr):
    # empty list to hold the value
    the_one = []
    
    # for each integer in the array
    for i in arr:
        # if the count is only one
        if arr.count(i) == 1:
            #append that one to the list
            the_one.append(i)

    return the_one[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
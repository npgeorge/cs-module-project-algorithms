'''
Input: a List of integers
Returns: a List of integers
'''
'''
UPER
Understand
given a list of integers, create a new list 
that holds the product of all the other numbers except that one

said another way, multiply all integers in the list together __except__ the current integer

PLAN
create an empty list
iterate through the list
multiply every integer, except current(i)
--> Naive: for any given i, make a new list without that i in it
    multiply all numbers in that list together
    enter that number into another list in the ith spot

--> second approach

take the product of the whole list
divide by that int in a list comprehension to build new list

'''
def product_of_all_other_numbers(arr):
    # initialize 1 to begin for loop
    x = 1
    
    # for i in array, multiply x by i
    for i in arr:
        # x gets updated through each iteration
        x = x * i # equivalent to x *= i
        print(x)
    
    # divide multiplied number x by ith number in arr
    new_list = [x//i for i in arr]

    return new_list

#print(product_of_all_other_numbers([1,7,3,4]))


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

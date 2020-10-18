'''
Input: a List of integers
Returns: a List of integers
'''

'''
UPER
Understand
Move each non-zero integer to the left side of the array
the order does not matter in this case
Conversely thought of as moving each 0 integer to the right side of the array

PLAN
Naive: Loop through list, if zero, move or append to end
Brute-Force: same as above?

Naive:
loop through array, if value = non-zero, append value in new list first
then if value = 0, append those values last

another approach...
hold two lists, one non-zero and one zero
then append the zero list to the non-zero one

'''
def moving_zeroes(arr):
    non_zero = []
    zeroes = []
    
    for i in arr:
        if i > 0 or i < 0:
            non_zero.append(i)
        
    for i in arr:
        if i == 0:
            zeroes.append(i)
    
    return non_zero + zeroes


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
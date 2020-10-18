'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
'''
UPER
Understand
An array with a range or "window" of size "K" slides over another array we'll call "Z" from left to right 
"Z" has an assumed size > "K"
Return the max number inside of "K" each as it slides over "Z" one element at a time from left to right

PLAN
Passing in two params, a list and a "K" param designating how long the "window" is
Naive: Loop through the list "K" at a time
--> extract max value into list
--> slide one element over
--> repeat

Execute (Pseudo-Code)
initiate "window" list
initiate list for max vals = []

for integers in list:
    look at "K" at a time
    grab max val
    append to list
    slide over one
    stop k from the end

return list
'''

def sliding_window_max(arr, k):
    # initialize
    window =[]
    max_vals = []
    x = 0

    print('List:', arr)
    for i in arr:
        '''
        OLD
        # create window start from x to k
        #window = arr[x:k]
        #print('First:', window)
        # grab the max value from the window
        #max_val = max(window)
        # append to max vals list
        #max_vals.append(max_val)
        # slide one num over for each window param
        #x += 1
        #k += 1
        # come back to, not sure why this doesn't work
        # not an if statement, a matter of when
        '''
        # refined
        if window == arr[-3:]: # why does 'k' not work in place of -3?
            print('Exit:', window)
            return print('Max Values:', max_vals)
        else:
            window = arr[x:k]
            max_val = max(window)
            max_vals.append(max_val)
            x += 1
            k += 1
            print('Window: ', window)
            
    return print('Max values:', max_vals)

sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3)

#if __name__ == '__main__':
#    # Use the main function here to test out your implementation 
#    arr = [1, 3, -1, -3, 5, 3, 6, 7]
#    k = 3
#
#    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

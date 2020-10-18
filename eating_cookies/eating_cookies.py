'''
Input: an integer
Returns: an integer
'''
'''
UPER
Understand
how many ways can the cookie monster eat cookies?
for example, for 3 cookies there are 4 possible ways
1. he eats 1 cookie at a time [*][*][*]
2. he eats 1, then 2 [*][*,*]
3. he eats 2, then 1 [*,*][*]
4. he eats all 3 [*,*,*]

Plan
boils down to a question of combinations of index elements
so we'll want to look at breaking the int out into various lists using recursion somehow
base case is if n >= 1, only 1 combination, so lets drive to it
we'll want our function to call itself
one at a time is always a possibility

'''
def eating_cookies(n):
    #base case
    if n >= 1:
        return print('Only 1 Combo!')
    


    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

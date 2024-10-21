# Author: Andrew Bittner
# Date: 10/20/2024

# Program #2: Larger than n
# In a program, write a function (with NO output) that accepts two arguments: number n, and a list.
# Assume that the list contains numbers.
# The function shell has been written out on line 30, (def display_larger_than_n_list)
# and should display all of the numbers in the list that are greater than then number n.

def exit_sequence():
    # Function to keep console/window open until user ends program
    input('\n\nPress [enter] to exit... ')

def main():
    # Declare local variables
    number = 5
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Display the number.
    print('Number:', number)

    # Display the list of numbers.
    print('List of numbers:')
    print(f'{number_list}')
    
    # Display the list of numbers that are larger
    # than the number.
    print(f'List of numbers that are larger than {number}:')
    
    # Call the display_larger_than_n_list function,
    # passing a number and number list as arguments.
    display_larger_than_n_list(number, number_list)
    exit_sequence()

# The display_larger_than_n_list function accepts two arguments:
# a list, and a number. The function displays all of the numbers
# in the list that are greater than the number.
def display_larger_than_n_list(n, n_list):
    # Write your code to display all of the numbers in the list that are greater than then number n. below
    # Initialize list
    larger_than_n_list = []
    # Compare each value in "n_list" to "n"; if greater, append to new list
    larger_than_n_list = [num for num in n_list if num > n]
    # Display results
    print(f'Numbers in list greater than 5: ', end = '')
    for num in larger_than_n_list:
        print(num, end = '')
        if larger_than_n_list.index(num) < len(larger_than_n_list) - 1: print(', ', end = '')
        
# Call main function
if __name__ == '__main__':
    main()
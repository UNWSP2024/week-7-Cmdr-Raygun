# Author: Andrew Bittner
# Date: 10/20/2024

# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

import statistics

def exit_sequence():
    # Function to keep console/window open until user ends program
    input('\nPress [enter] to exit... ')

def change_var_type(inp, out_type, err_msg = 'Invalid input entered (was it formatted correctly?). ', inp_msg = 'Please re-enter your answer: '):
    # Check whether input type  matches desired output type
    while type(inp) != out_type:
        # If mismatched, try to change input variable's type to desired type
        try:
            inp = out_type(inp)
        # If that fails due to bad data, ask user for new data
        except ValueError:
            print(err_msg, end = '')
            inp = input(inp_msg)
    return inp

def get_rainfall():
    # Set up lists for rainfall collector
    MONTHS_LIST = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    rainfall = []
    # Rainfall value collector
    print(f'Enter the rainfall in inches (number only) for ', end = '')
    for month in MONTHS_LIST:
        rainfall.append(input(f'{month}: '))
        rainfall.insert(-1, (change_var_type(rainfall[-1], float)))
        rainfall.pop(-1)
    return rainfall, MONTHS_LIST

def main():
    rainfall_list, MONTHS_LIST = get_rainfall()
    # Get average rainfall
    avg_rainfall = statistics.mean(rainfall_list)
    # Get minimum rainfall and month in which it occurred
    mn_rainfall = min(rainfall_list)
    mn_rainfall_month = MONTHS_LIST[rainfall_list.index(mn_rainfall)]
    # Get maximum rainfall and month in which it occurred
    mx_rainfall = max(rainfall_list)
    mx_rainfall_month = MONTHS_LIST[rainfall_list.index(mx_rainfall)]
    # Display results
    print(f'Least rainfall in {mn_rainfall_month} at {mn_rainfall:,.1f} inches.\n'
          f'Greatest rainfall in {mx_rainfall_month} at {mx_rainfall:,.1f} inches.\n'
          f'Average rainfall of {avg_rainfall:,.2f} inches.')
    exit_sequence()

# Call the main function
if __name__ == '__main__':
    main()
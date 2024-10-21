# Author: Andrew Bittner
# Date: 10/20/2024

# Program #3: US_Population

def exit_sequence():
    # Function to keep console/window open until user ends program
    input('\n\nPress [enter] to exit... ')

def change_var_type(inp, out_type, err_msg = 'Invalid input entered (was it formatted correctly?). ', inp_msg = 'Please re-enter your answer: '):
    # Check whether input type  matches desired output type
    if type(inp) == list or type(inp) == tuple:
        for val in inp:
            while type(val) != out_type:
                try: val = out_type(val)
                except:
                    print(err_msg, end='')
                    inp = input(inp_msg)
                    inp_raw = inp
                    inp = list(inp)
                    for ind in range(len(inp_raw)):
                        if not inp_raw[ind].isdigit(): inp.remove(inp_raw[ind])
                inp.append(val)
        inp = inp[int(len(inp)/2): int(len(inp))]
        return inp
    else:
        while type(inp) != out_type:
            # If mismatched, try to change input variable's type to desired type
            try: inp = out_type(inp)
            # If that fails due to bad data, ask user for new data
            except ValueError:
                print(err_msg, end = '')
                inp = input(inp_msg)
    return inp

def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]

    # all_entered_values = []
    pop_data_state = []
    pop_data_list = []
    collect_data = True
    while collect_data == True:
            # if not tutorial_shown:
            #     pop_data_state = [input(f'{prompt_1}'), input(f'{space * (len(prompt_1) - len(prompt))}{prompt}') * (len(POP_DATA_TYPES) - 1)]
            #     tutorial_shown = True
        pop_data_state = [input(f'Enter the year (digits only): '), input(f'Enter the state: '), input(f'Enter the population (digits only): ')]
        pop_data_state[0] = change_var_type(pop_data_state[0], int)
        pop_data_state[2] = change_var_type(pop_data_state[2], int)
            # if pop_data_state[-1] == 'x':
            #     collect_data = False
            #     break
        pop_data_list.append(pop_data_state)
        print(pop_data_list)
        cont = input('Enter another data set? (y/n): ')
        while cont != 'y' and cont != 'n':
            cont = input('Invalid input. Enter another data set? ')
        if cont == 'n': collect_data = False

    # Now have the user enter a year.
    print(pop_data_list)
    pop_for_year = input('Now enter a year for which to get a total population (from data provided): ')
    pop_for_year = change_var_type(pop_for_year, int)
    sum_population_for_year(pop_data_list, pop_for_year)

    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

    exit_sequence()
def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user entered 2010 for the year to sum,
    # or 3,421,988 if they entered 2011 for the year to sum.
    # for year in all_entered_values:
    pop_total = 0
    for row in (all_entered_values):
        for item in row:
            if item == year_to_sum: pop_total += row[2]
    # Print the totalled population
    print(f'OK, the total population for {year_to_sum} is {pop_total:,}.')

# Call the main function.
if __name__ == '__main__':
    main()
# Author: Andrew Bittner
# Date: 10/10/2024

# Program #3: US_Population

def exit_sequence():
    # Function to keep console/window open until user ends program
    input('\n\nPress [enter] to exit... ')

def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]

    # all_entered_values = []
    POP_DATA_TYPES = ['year', 'state', 'population']
    pop_data_state = []
    pop_data_list = []
    space = ' '
    collect_data = True
    tutorial_shown = False
    while collect_data == True:
        for param in POP_DATA_TYPES:
            prompt_1 = f'Enter the {POP_DATA_TYPES[0]}. Alternatively, enter "x" to exit dialog: '
            prompt_2 = f'Enter the {param}: '
            # if not tutorial_shown:
            #     pop_data_state = [input(f'{prompt_1}'), input(f'{space * (len(prompt_1) - len(prompt_2))}{prompt_2}') * (len(POP_DATA_TYPES) - 1)]
            #     tutorial_shown = True
            pop_data_state = [input(f'{space * (len(prompt_1) - len(prompt_2))}{prompt_2}') * len(POP_DATA_TYPES)]
            # if pop_data_state[-1] == 'x':
            #     collect_data = False
            #     break
            pop_data_list.append(pop_data_state)
            print(pop_data_list)
        cont = input('Enter another data set (y/n)? ')
        while cont != 'y' and cont != 'n':
            cont = input('Invalid input. Enter another data set? ')
        if cont == 'n': collect_data = False

    # Now have the user enter a year.
    print(pop_data_list)
    pop_for_year = input('Now enter a year for which to get a total population (from data provided): ')
    sum_population_for_year(pop_data_list, pop_for_year)

    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

    exit_sequence()
def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user entered 2010 for the year to sum,
    # or 3,421,988 if they entered 2011 for the year to sum.
    # for year in all_entered_values:
    print(all_entered_values)
        # if year == year_to_sum:
    # Print the totalled population


# Call the main function.
if __name__ == '__main__':
    main()
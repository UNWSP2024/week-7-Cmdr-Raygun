# Author: Andrew Bittner
# Date: 10/20/2024

# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.
import math

def change_var_type(inp, out_type, list_ct_mn = -1, list_ct_mx = -1, err_msg = 'Invalid input entered (was it formatted correctly?). ', inp_msg = 'Please re-enter your answer: '):
    # Check whether input type  matches desired output type
    if type(inp) == list or type(inp) == tuple:
        for val in inp:
            while type(val) != out_type:
                print(len(val))
                # inp_raw = inp
                print(inp)
                try:
                    # if inp.count(int) or inp.count(float) < list_ct_mn: print('This text will cause an error!')
                    for ind in range(len(val)):
                        print(ind)
                        if not inp[ind].isdigit(): inp.remove(inp[ind])

                    if inp.count(float) < list_ct_mn: print('This text will cause an error!')
                    print(inp)
                except ValueError:
                    print(err_msg, end='')
                    inp = input(inp_msg)
                    inp = inp.split(',')
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

def get_dist(coord_1, coord_2):
    x_1 = coord_1[0]
    y_1 = coord_1[1]
    z_1 = coord_1[2]
    x_2 = coord_2[0]
    y_2 = coord_2[1]
    z_2 = coord_2[2]
    dist = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2 + (z_1 - z_2) ** 2)
    return dist

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)
def main():
    # Get coordinate 1 from user
    coord_1 = input('Enter a three-dimensional coordinate, with X, Y, and Z values separated with a comma (e.g., "3, 1, 4"): ')
    coord_1 = coord_1.split(',')
    # inp_raw = coord_1
    # print(coord_1)
    # for ind in range(len(inp_raw)):
    #     if not inp_raw[ind].isdigit(): coord_1.remove(inp_raw[ind])
    coord_1 = change_var_type(coord_1, float, 3)
    coord_1 = tuple(coord_1)
    # Get coordinate 2 from user
    coord_2 = (input('Enter another three-dimensional coordinate: '))
    inp_raw = coord_2
    coord_2 = list(coord_2)
    for ind in range(len(inp_raw)):
        if not inp_raw[ind].isdigit(): coord_2.remove(inp_raw[ind])
    coord_2 = list(coord_2)
    coord_2 = change_var_type(coord_2, float), 3
    coord_2 = tuple(coord_2)
    dist = get_dist(coord_1, coord_2)
    print(f'OK, the distance between points ({coord_1[0]}, {coord_1[1]}, {coord_1[2]}) and ({coord_2[0]}, {coord_2[1]}, {coord_2[2]}) is {dist:.2f} units.')

if __name__ == '__main__':
    main()
# Question 3


def total_charge(filename):
    # initialize the total charge to 0
    total = 0
    
    # open the file for reading
    with open(filename, "r") as f:
        # read each line of the file
        for line in f:
            # split the line into three parts based on spaces
            parts = line.split()
            
            # extract the price from the last part of the line
            price = int(parts[-1])
            
            # add the price to the total charge
            total += price
    
    # return the total charge
    return total


"""
Susie Smith
January 24, 2023

I will be using built-in functions and 
functions from the math module.

I will be illustrating the ability to call functions and 
display useful results to the user. 

"""
print()
print("Susie Smith")
print("January 24, 2023")
print()

import math

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length*width #fixed
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)
print('Task 3 Questions/Answer:')
print('     4. How many arguments does get_area_of_lot() take? \n'
'               -The function, get_area_of_lot takes two arguments.')
print('     5. What does it return? \n'
'               -After fixing, this will return the length*width.')





# -------------------------------------------------------------
# Call some functions and execute code!
print("---------------------------------------------")

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    print("Explore some functions in the math module")
    print()
    print("1. Use the defensive math examples to call the permutations and combinations as shown:")
    print(f"math.combs(5,1) = {math.comb(5,1)}")
    print(f"math.perms(5,1) = {math.perm(5,1)}")
    print()
    print("your code here")
    print()
    print("""2. Then, call the method you just fixed \
with several different arguments and display  
them for the user:""")
    print(get_area_of_lot(3,2))
    print(get_area_of_lot(7,14))
    print(get_area_of_lot(30,9))
    print("""Above are the returns for the custom function(get_area_of_lot), 
using arguments of (3,2), (7,14), and (30,9), respectively.""")
    print()
    print('How many arguments are needed? 2')
    print("Call get_area_of_lot(6,2) and display the result:")
    print(get_area_of_lot(6,2))
    print()

#Write and call custom functions with examples.
    print("3. Write and call custom functions with examples:")
    print("     1. Minutes Per Game (For return, see below)")
    print()
    """Returns the minutes played in an entire basketball game."""
    def minutes_per_game(quarters,mins_per_quarter):
        quarters=4
        mins_per_quarter=7
        total_mins = quarters * mins_per_quarter
        return total_mins

#Three more simple functions that are useful to my domain:
    print("4. Three more simple functions that are useful to my domain (see returns below):")
    print("     1. Average Points Per Quarter")
    print("     2. Team Free Throw Percentage")
    print("     3. Sum of players rebounds")


"""Return the average points scored per quarter"""
def avg_points_per_quarter(quart1, quart2, quart3, quart4):
        quart1=22
        quart2=10
        quart3=20
        quart4=35
        avg_PPQ = (quart1 + quart2 + quart3+ quart4)/4
        return avg_PPQ

"""Return the free throw percentage for the team."""
def team_free_throw_perc(play1_FTA, play2_FTA, play3_FTA, play1_FTM, play2_FTM, play3_FTM):
    play1_FTA=9
    play2_FTA=3
    play3_FTA=5
    play1_FTM=8
    play2_FTM=0
    play3_FTM=2
    total_attempts = play1_FTA + play2_FTA + play3_FTA
    total_made = play1_FTM + play2_FTM + play3_FTM
    free_throw_percentage = (total_made / total_attempts) * 100
    return int(free_throw_percentage)

"""Return the sum of players' rebounds using the math.fsum function."""
#Using list of rebounds as integers, see below
import math
Team_Rebounds = (9,11,5)

##Call functions here
print()
print("Returns here:")

print(f"minutes_per_game(4,7) = {minutes_per_game(4,7)}")
print(f"avg_points_per_quarter(22,10,20,35) = {avg_points_per_quarter(22,10,20,35)}")
print(f"team_free_throw_perc(9,3,5,8,0,2) = {team_free_throw_perc(9,3,5,8,0,2)}")
print("Total Rebounds =", math.fsum(Team_Rebounds))




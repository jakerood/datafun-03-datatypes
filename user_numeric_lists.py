"""
Jake Rood
September 10, 2023

Purpose: Illustrate options for working with lists in Python in the domain of baseball
"""

# import some standard modules first - how many can you make use of?
# import from standard library
import math
import statistics


# TODO: import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# TODO: Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

# TODO: Create some shared data lists if you like - or just create them in your functions
# First, let's create a list of the number of hits by each player on a team
hits_list = [
    62,
    102,
    75,
    113,
    58,
    50,
    75,
    94,
    63,
    75,
    70,
    66,
    65,
    62,
    36,
    35,
    30,
    16,
    12,
    5,
    4
]

# Next, let's create use some univariant time series data
# We can show the number of home runs hit over the course of a player's career
seasons_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
homeruns_list = [7, 11, 16, 17, 24, 22, 29, 34, 35, 41]

# TODO: define some custom functions
def quick_list_stats():
    """The function calculates descriptive statistics for a numeric list"""

    logger.info(f"hits_list: {hits_list}")
    
    # Descriptive statistics: averages and measures of central tendency

    mean = statistics.mean(hits_list)
    median = statistics.median(hits_list)
    mode = statistics.mode(hits_list)
    stdev = statistics.stdev(hits_list)
    variance = statistics.variance(hits_list)

    logger.info(f"mean: {mean}")
    logger.info(f"median: {median}")
    logger.info(f"mode: {mode}")
    logger.info(f"standard deviation: {stdev}")
    logger.info(f"variance: {variance}")

def list_correlation():
    """The function calculates correlation between two lists"""

    logger.info(f"seasons_list: {seasons_list}")
    logger.info(f"homeruns_list: {homeruns_list}")

    # Use statisitics module to get correlation between the two lists

    correlation = statistics.correlation(seasons_list, homeruns_list)
    logger.info(f"correlation between seasons and home runs: {correlation}")

# use statistics module to get linear regression for season_list and homeruns_list

slope, intercept = statistics.linear_regression(seasons_list, homeruns_list)
logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")

# Set future x value as 15

future_x = 15

# Use the slope and intercept and future x to predict a future y value for the future x value
# where y = mx + b

future_y = slope * future_x + intercept
logger.info(f"We predict that when the player's season = {future_x}, the player will hit about {future_y} home runs")

# Now lets call some built-in Python functions and apply them to our lists

def quick_list_built_in_functions():
    """The function calls multiple built-in functions that work on lists"""

    max_value = max(hits_list)
    min_value = min(hits_list)

    logger.info(f"Given hits list: {hits_list}")
    logger.info(f"The max() is {max_value}")
    logger.info(f"The min() is {min_value}")

    # Calculate the length of the list
    len_list = len(hits_list)
    logger.info(f"The len() is {len_list}")

    # Calculate the sum of the list
    sum_list = sum(hits_list)
    logger.info(f"The sum() is {sum_list}")

    # Calculate the average of the list
    avg_list = sum_list / len_list
    logger.info(f"The average is {avg_list}")

    logger.info(f"Given hits list: {hits_list}")
    # Return a new list soreted in ascending order
    asc_hits = sorted(hits_list)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_hits}")

    # Return a new list soreted in descending order
    desc_hits = sorted(hits_list, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_hits}"
    )

def quick_list_methods():
    """This function illustrates methods that can be called on a list"""

    """

     LIST METHODS ............................................... 

     Here are some common methods that operate on an instance of a list.

     append(x): Add an item to the end of the list.
     extend(iterable): Add all the items from an iterable (such as another list)
          to the end of the list.
     insert(i, x): Insert an item at a given position.
     remove(x): Remove the first occurrence of an item.
     pop([i]): Remove the item at the given position in the list, 
     and return it. If no index is specified, 
     removes and returns the last item in the list.
     clear(): Remove all items from the list.
     index(x[, start[, end]]): Return the index of the first occurrence of
          an item.
     count(x): Return the number of occurrences of an item.
     sort(key=None, reverse=False): Sort the items in the list 
          in ascending order.
     reverse(): Reverse the order of the items in the list.
     copy(): Return a shallow copy of the list.

     """

    # append an item to the end of the list
    lst = ["twins", "yankees", "cubs"]
    lst.append("cardinals")

    # extend the list with another list
    lst.extend(["pirates", "dodgers", "white sox"])

    # insert an item at a given position (0 = first item)
    i = 2
    newvalue = "red sox"
    lst.insert(i, newvalue)

    # remove an item
    item_to_remove = "red sox"
    lst.remove(item_to_remove)

    # Count how many times twins appears in the list
    ct_of_twins = lst.count("twins")

    # Sort the list in ascending order using the sort() method
    asc_lst = lst.sort()

    # Sort the list in descending order using the sort() method
    desc_lst = lst.sort(reverse=True)

    # Copy the list to a new list
    new_lst = lst.copy()
    logger.info(f"new_lst is: {new_lst}")

    # Remove the first item from the new list
    # The first item in a list is at index 0
    # Think of it as an offset from the beginning of the list
    first = new_lst.pop(0)
    logger.info(
        f"Popped the first (index=0): {first} and now, new_lst is: {new_lst}"
    )

    # Remove the last item from the new list
    # The last item in a list is at index -1
    last = new_lst.pop(-1)
    logger.info(
        f"Popped the last (index=-1): {last} and now, new_lst is: {new_lst}"
    )

def quick_list_transformations():
    """This function illustrates transformations that can be applied to a list"""

    logger.info("Hits list: {hits_list}")

    # TRANFORMATIONS ............................

    # FILTER and MAP are critical tranformations in big data applications

    # Filter the hits list to only include hits greater than 60
    # Say "KEEP x such that x > 60 is True" given hits_list
    # Cast the result using square brackets to get back a list
    hits_over_60 = [filter(lambda x: x > 60, hits_list)]
    logger.info(f"Hits over 60: {hits_over_60}")

    # Use the built-in function map() anywhere you need to transform a list

    # Map each element to its cuberoot
    # Say "map x to the cuberoot of x" given hits_list
    # Cast the result using square brackets to get a list
    cuberoot_hits = [map(lambda x: math.cbrt(x), hits_list)]
    logger.info(f"Cuberoot hits: {cuberoot_hits}")

    # Map each element to calculate the hypothetical volume of a cube
    # Say "map x to x cubed" given hits_list
    # remember to cast the result to a list (using square brackets)
    volume_hits = map(lambda x: x ** 3, hits_list)
    logger.info(f"Voulme of hits: {volume_hits}")

def quick_list_comprehensions():
    """This function illustrates list comprehensions"""

    logger.info(f"Hits list: {hits_list}")

    # TRANFORMATIONS - Using List Comprehensions
    # List comprehensions are a concise way to create lists
    # They work like map and filter, but are more concise

    # Filter the new list to only include hits greater than 60
    # Say "KEEP x (for each x in hits_list) IF  x > 60"
    # Cast the result to a list using square brackets

    hits_over_60 = [x for x in hits_list if x > 60]
    logger.info(f"Hits over 60 (using list comprehensions!): {hits_over_60}")

    # Now triple each value in the list
    hits_tripled = [x * 3 for x in hits_list]
    logger.info(f"Hits tripled (using list comprehensions!): {hits_tripled}")

    # Map each element to its square root
    # Say "give me the square root of x (for each x in hits_list)"
    # Cast the result to a list using square brackets
    sqrt_hits = [math.sqrt(x) for x in hits_list]
    logger.info(f"Square root of hits (using list comprehensions!): {sqrt_hits}")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here (see instructions)
    quick_list_stats()
    list_correlation()
    quick_list_built_in_functions()
    quick_list_methods()
    quick_list_transformations()
    quick_list_comprehensions()
    show_log()

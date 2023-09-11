"""
Jake Rood
September 10, 2023
Purpose: Illustrate tuples, sets and dictionaries in Python

"""

# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)


# Create some tuples and use the examples to practice with tuples
def illustrate_tuples():
    """This function illustrates tuples in Python."""

    # Create some tuples
    tuple_twins = ("Minnesota Twins", 75, 68, .524, 0)
    tuple_guardians = ("Cleveland Guardians", 68, 76, .472, 7.5)
    tuple_tigers = ("Detroit Tigers", 66, 77, .462, 9.0)

    logger.info(f"{tuple_twins = }")
    logger.info(f"{tuple_guardians = }")
    logger.info(f"{tuple_tigers = }")

    # tuple concatenation
    tupleCat = tuple_twins + tuple_guardians
    logger.info(f"{tupleCat = }")


def illustrate_sets():
    """This function illustrates sets in Python."""

    set_AL_Central = {"Twins", "Guardians", "White Sox", "Royals", "Tiger"}
    set_NL_Central = {"Cubs", "Cardinals", "Pirates", "Brewers", "Reds"}

    logger.info(f"{set_AL_Central = }")
    logger.info(f"{set_NL_Central = }")

    # set union
    union = set_AL_Central | set_NL_Central
    logger.info(f"The union is: {union}")

    # set intersection
    intersection = set_AL_Central & set_NL_Central
    logger.info(f"The intersection is: {intersection}")

# Use a dictionary to create key-value pairs of each word and its count from a file
def illustrate_dictionaries():
    """This function illustrates dictionaries in Python."""

    playerA_dict = {"name": "Joe Mauer", "position": "C", "team": "Minnesota Twins"}
    playerB_dict = {"name": "Mike Trout", "position": "OF", "team": "Los Angeles Angels"}

    logger.info(f"{playerA_dict = }")
    logger.info(f"{playerB_dict = }")

 # Dictionaries can be used to store and aggregate statistical data,
 # such as counts or sums. For example, a dictionary of word-count pairs.

    with open("text_juliuscaesar.txt") as file_object:
        word_list = file_object.read().split()
    
    word_counts_dict = {word: word_list.count(word) for word in word_list}
    logger.info("Given text_juliuscaesar.txt and comprehensions,")
    logger.info(f"the {word_counts_dict = }")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!
# Remember, code blocks must be indented consistently after a colon.

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here
    illustrate_tuples()
    illustrate_sets()
    illustrate_dictionaries()
    show_log()
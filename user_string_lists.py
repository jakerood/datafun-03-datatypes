"""
Jake Rood
September 10, 2023

"""

# imports first

# reusable functions next

# call functions and execute code
# use if __name__ == "__main__":

import random

from util_datafun_logger import setup_logger

# Set up logging .............................................

logger, logname = setup_logger(__file__)

# Define shared data ..........................................

# Define a few string lists
list_teams = ["Minnesota Twins", "Chicago White Sox", "Cleveland Guardians", "Detroit Tigers", "Kansas City Royals"]
list_stadiums = ["Target Field", "Guaranteed Rate Field", "Progressive Field", "Comerica Park", "Kauffman Stadium"]
list_terms = ["hits", "runs", "errors", "strikeouts", "wins"]
list_players = ["Joe Mauer", "Justin Morneau", "Johan Santana", "Kirby Puckett", "Kent Hrbek"]
list_minor_league_levels = ["AAA", "AA", "High A", "A", "Rookie"]

logger.info(f"The list of teams is: {list_teams}")
logger.info(f"The list of stadiums is: {list_stadiums}")
logger.info(f"The list of terms is: {list_terms}")
logger.info(f"The list of players is: {list_players}")
logger.info(f"The list of minor league levels is: {list_minor_league_levels}")

# Use the built-in functions to combine 2 or more lists into tuples
new_tuple = tuple(zip(list_teams, list_stadiums))
logger.info(f"The tuple is: {new_tuple}")

# Use random.choice() to pick a random value from one of your lists.
# Customize the sentence generator to create random sentences about your domain. 
def create_random_sentence():
    """Create a random sentence from our pre-defined lists"""
    logger.info("Calling create_random_sentence()")

    # Pick a random team

    random_team = random.choice(list_teams)
    logger.info(f"The random team is: {random_team}")

    # Create a random sentence
    sentence = (
        f"The {random_team} signed {random.choice(list_players)} to a three year contract."
        f"\nHe led the league in {random.choice(list_terms)} last season."
    )

    logger.info(f"Random sentence: {sentence}")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!
# Remember, code blocks must be indented consistently after a colon.

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    create_random_sentence()
    show_log()

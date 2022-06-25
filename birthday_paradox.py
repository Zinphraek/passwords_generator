import datetime
import random


def get_birthdays(nbr_of_birthdays):
    """Return a list of number random date objects for birthdays."""
    birthdays_ = []
    for n in range(nbr_of_birthdays):
        #  The year is unimportant for this simulation, as long as all birthdays have the same year.
        start_of_year = datetime.date(2001, 1, 1)
        #  Let's get a random day into the year
        random_nbr_of_days = datetime.timedelta(random.randint(0, 364))
        birthday_ = start_of_year + random_nbr_of_days
        birthdays_.append(birthday_)
    return birthdays_


def get_match(birthdays_list):
    """Return the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays_list) == len(set(birthdays_list)):
        return None  # All birthdays are unique, so we return None.
    #  Let's compare each birthday to every other birthday.
    for a, birthday_A in enumerate(birthdays_list):
        for b, birthday_B in enumerate(birthdays_list[a + 1:]):
            if birthday_A == birthday_B:
                return birthday_A  # We return the matching birthday.


# Display the introduction
print('''Birthday Paradox

The Birthday Paradox shows us that in a group of N people, the odds that two of them have matching birthdays is
surprising large.
This program does a Monte Carlo simulation (that is, repeated random simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

# Setting up a tuple of month name in order.
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # We keep looping until the user enter a valid quantity
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        nbr_days = int(response)
        break  # The user a]has entered a valid quantity.
print()

# Generate and display the birthdays:
print(f"Here are {nbr_days} birthdays:")
birthdays = get_birthdays(nbr_days)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #  Display a comma for each birthday after the first birthday.
        print(', ', end='')
        month_name = MONTHS[birthday.month - 1]
        date_text = f"{month_name} {birthday.day}"
        print(date_text, end='')
print('\n\n')

# Determining if there are two birthdays that match.
match = get_match(birthdays)

# Displaying results:
print('In this simulation, ', end='')
if match is not None:
    month_name = MONTHS[match.month - 1]
    date_text = f"{month_name} {match.day}"
    print('Multiple people have a birthday on', date_text)
else:
    print('There are no matching birthdays.\n')

# Run through 100,000 simulations:
print('Generating', nbr_days, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print("let's run another 100,000 simulations.")
sim_match = 0  # How many simulations had matching birthdays in them.
for i in range(100_000):
    # Report on the progress every 10,000 simulations.
    if i % 10_000 == 0:
        print(i, 'simulations run...')
        birthdays = get_birthdays(nbr_days)
        if get_match(birthdays) is not None:
            sim_match += 1
print('100,000 simulations run.')

# Display simulation results:
probability = round(sim_match / 100_000 * 100, 2)
print(f"Out of 100,000 simulations of {nbr_days} people, there was a matching birthday in that group {sim_match} times."
      f" This means that {nbr_days} people have a {probability}% chance of having a matching birthday in their group."
      f"\nThat's probably more than you would think!")

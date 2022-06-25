from random import randint


def get_guess(v_length):
    """Check whether the user entered a valid number and return it."""
    while True:
        guess_ = input('> ')
        if guess_:
            try:
                int(guess_)
            except ValueError:
                print(f"{guess_} is not an integer number.")
                continue
            else:
                if len(guess_) != v_length:
                    print(f"The number must have {v_length} digits.")
                    continue
                elif (-1) * int(guess_) == abs(int(guess_)) and int(guess_) != 0:
                    print("Only positive integer are accepted.")
                else:
                    return guess_


def the_game():
    """This is the main game function."""
    nbr_of_digit = 3
    max_guesses = 10
    nbr_to_guess = ''
    for i in range(nbr_of_digit):
        nbr_to_guess += str(randint(0, 9))
    print(f"""**** Bagels, a deductive logic game. ****\n
    I am thinking of a {nbr_of_digit}-digit number. Try to guess what it is.
    Here are some clues:
    When I say:       That means:
        Pico               One digit is correct but in the wrong place.
        Fermi              One digit is correct and in the right place.
        Bagels             No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico""")
    print(f"I have thought up a number.\n You have {max_guesses} guesses to get it.")

    guess_nbr = 1
    while guess_nbr <= max_guesses + 1:
        if guess_nbr == max_guesses + 1:
            print(f"You ran out of guesses.\nThe number was {nbr_to_guess}\n**** Game Over ****")
            break
        print(f"Guess #{guess_nbr}:")
        guess = get_guess(nbr_of_digit)
        if guess == nbr_to_guess:
            print("You got it!")
            break
        else:
            p = []
            for i in range(nbr_of_digit):
                if guess[i] == nbr_to_guess[i]:
                    p.append('Fermi')
                elif guess[i] in nbr_to_guess:
                    p.append('Pico')
            if len(p) == 0:
                print('Bagels')
                guess_nbr += 1
                continue
            else:
                p = sorted(p)
                print(' '.join(p))
                guess_nbr += 1
                continue


def main():
    """This is the main game."""
    cond = True
    while cond:
        the_game()
        print("Do you want to play again? y/n")
        while True:
            answer = input('> ')
            if answer.lower() == 'y' or answer.lower() == 'yes':
                break
            elif answer.lower() == 'n' or answer.lower() == 'no':
                cond = False
                print("Thank you!")
                break
            else:
                print(f"{answer} is not a valid answer.")
                continue


if __name__ == '__main__':
    main()

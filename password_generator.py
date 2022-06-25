import random
import string


def generate_password():
    """Return a random generated password."""

    while True:
        n = input('Enter the length of the password. (Minimum 6 digits): ')
        if n.isdecimal() and (6 <= int(n)):
            n = int(n)
            break
    nbr = [str(i) for i in range(10)]
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    all_characters = string.ascii_letters + ''.join(map(str, nbr))
    special_characters = string.punctuation
    a_list = [random.choice(lower_letters), random.choice(upper_letters), random.choice(special_characters),
              random.choice(nbr)]
    random.shuffle(a_list)
    p_word = ''.join(map(str, a_list))
    for i in range(n - 4):
        p_word = ''.join([p_word, random.choice(all_characters)])
    p_word = p_word.split()
    random.shuffle(p_word)
    pass_word = ''.join(map(str, p_word))
    return pass_word


my_password = generate_password()
print(my_password)

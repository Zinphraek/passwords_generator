while True:
    print("Do you want to know how to keep a stupid person busy for Hours? Y/N")
    response = input()
    if response.lower() == 'n' or response.lower() == 'no':
        print("Thank you! Good buy")
        break
    elif response.lower() == 'y' or response.lower() == 'yes':
        continue
    else:
        print(f"{response} is not valid entry!")
        continue

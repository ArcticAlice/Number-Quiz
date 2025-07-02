import random

def easy():
    randomOne = random.randint(10, 99)
    randomTwo = random.randint(10, 99)
    answer = randomOne * randomTwo 
    print(f'Your Question Is: {randomOne} * {randomTwo }')
    human = input("Enter Answer Here: ")
    if int(human) == answer:
        print('CORRECT!')
    else:
        print(f'WRONG! Correct Answer Was {answer}')

def medium():
    randomOne = random.randint(100, 999)
    randomTwo = random.randint(10, 99)
    answer = randomOne * randomTwo
    print(f'Your Numbers Are: {randomOne} * {randomTwo}')
    human = input("Enter Answer Here: ")
    if int(human) == answer:
        print('CORRECT!')
    else:
        print(f'WRONG! Correct Answer Was {answer}')

def hard():
    randomOne = random.randint(100, 999)
    randomTwo = random.randint(100, 999)
    answer = randomOne * randomTwo
    print(f'Your Numbers Are: {randomOne} * {randomTwo}')
    human = input("Enter Answer Here: ")
    if int(human) == answer:
        print('CORRECT!')
    else:
        print(f'WRONG! Correct Answer Was {answer}')

def difficult():
    randomOne = random.randint(10000, 99999)
    randomTwo = random.randint(10000, 99999)
    answer = randomOne * randomTwo
    print(f'Your Numbers Are: {randomOne} * {randomTwo}')
    human = input("ENTER YOUR LAST MEAL HERE: ")
    if int(human) == answer:
        print('SOMEWHAT OKAY!')
    else:
        print(f'WHAT IS WRONG WITH YOU MONKEY?! Correct Answer Was {answer}')


something = input("Which level do you want to do: easy? medium? hard? difficult? ")

if something.lower() == "level1":
    easy()
elif something.lower() == "level1.5":
    medium()
elif something.lower() == "level2":
    hard()
elif something.lower() == "level3":
    difficult()
else:
    print("Wrong Choice! ")

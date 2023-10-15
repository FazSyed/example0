import random

def is_correct(guess,answer):
    return(guess==answer)


def main():
    
    num = random.randint(1,10)
    print (num)
    answer = int(input("Enter a random number: "))
    print(is_correct(num,answer))
main()

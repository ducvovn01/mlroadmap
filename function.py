#Reviewing code functions and conditionals


def main():
    n = int (input ("Enter the number: "))

    if is_even(n):
        print ("even")
    else:
        print ("odd")


def is_even(a):
    if a % 2 == 0:
        return True
    

main()
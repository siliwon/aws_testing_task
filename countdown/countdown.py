import time


def countdown(number):
    for i in range(number, 1, -1):
        if number % 5 == 0 and number % 3 == 0:
            print("Testing")
        elif number % 5 == 0:
            print("Agile")
        elif number % 3 == 0:
            print("Software")
        else:
            print(number)
        time.sleep(1)
        number -= 1
    return 1


if __name__ == "__main__":
    number = input("Enter your integer please: ")
    print(countdown(int(number)))

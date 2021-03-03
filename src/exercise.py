def main():
    #write your code below this line
    number = int(input("Give a number:"))
    remainder = number % 2

    if (remainder == 0):
      print("Number " + str(number) + " is even")
    else:
      print("Number " + str(number) + " is odd")

if __name__ == '__main__':
    main()

def prompt_number():
    while True:
        number = int(input("Enter a positive number: "))
        if number > 0:
            #This print is for the stupid newline issue in test-bed
            print()
            return number
        else:
            print("Invalid entry. The number must be positive.")

def compute_sum(num1, num2, num3):
    return num1 + num2 + num3

def main():
    num1 = prompt_number()
    num2 = prompt_number()
    num3 = prompt_number()

    sum = compute_sum(num1,num2,num3)
    print("The sum is: %d" % (sum))

if __name__ == "__main__":
    main()
def main():
    print("Hey, This is my first python code so to speak.")
    inputFirst = int(input("Give me the first number:"))
    inputSecond = int(input("Give me a second number:"))
    value = inputFirst + inputSecond
    print(f"The value of the addition of these two numbers: {inputFirst} + {inputSecond} = {value}")
    return value
#indentation is key! if main() is one tab away, its considered to be inside def main()
main()

#lets assign a value to the function's return value: 
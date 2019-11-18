number = int(input("一つの自然数を入れてね: "))

if number % 3 == 0:
    output = "Fizz"
elif number % 5 == 0:
    print("Buzz")

else:
    print(str(number))

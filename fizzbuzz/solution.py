def check(number: int):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"

    if number % 3 == 0:
        return "Fizz"

    if number % 5 == 0:
        return "Buzz"

    return str(number)


def solve():
    for i in range(101):
        print(check(i))


if __name__ == "__main__":
    solve()

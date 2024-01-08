def fizz_buzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            result = "FizzBuzz"
        elif i % 3 == 0:
            result = "Fizz"
        elif i % 5 == 0:
            result = "Buzz"
        else:
            result = i  
        print(result)
fizz_buzz(15)
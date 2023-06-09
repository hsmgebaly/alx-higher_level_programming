#!/usr/bin/python3
if __name__ == "__main__":
    # print sum then difference before the multiple
    # and at last print the quotient of 10 and 5
    
    a = 10
    b = 5

    from calculator_1 import add, sub, mul, div

    result = add(a, b)
    print(f"{a} + {b} = {result}")

    result = sub(a, b)
    print(f"{a} - {b} = {result}")

    result = mul(a, b)
    print(f"{a} * {b} = {result}")

    result = div(a, b)
    print(f"{a} / {b} = {result}")

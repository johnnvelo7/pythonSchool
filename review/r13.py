def main():
    x = float(input("Enter x: "))
    result = g(x)
    print(f"x = {x} --> g(x) = {result}")

def g(x):
    if x < 1:
        return - (x * x) + 4
    else:
        return 2 * x - 1

main()
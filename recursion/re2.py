# This lecture will contain some basic problems related to recursion

# Problem 1:
# Print name 5 times
def main(name, count):
    if count == 0:
        return
    print(name)
    main(name, count-1)
main("generalpy", 5)

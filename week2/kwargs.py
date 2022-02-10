
def kwargs_example(**keyword_args):
    """
    A function that uses key word arguments.
    Key word arguments allow unlimited arguments to be passed
    They are stored in a dictionary
    """
    print("These are the keyword arguments")
    for key, val in keyword_args.items():
        print(key, val)


if __name__ == "__main__":
    kwargs_example(a=10, hi="yooo", age=1000, data=[1, 2, 3])
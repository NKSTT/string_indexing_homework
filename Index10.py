def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s (str): parameter
    Returns:
        int: answer
    """

    a = int(s[0]) + int(s[1]) + int(s[2]) + int(s[3]) + int(s[4])
    return a

b = main("22222")
print(b) 
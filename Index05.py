def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a = "1234567890"
    x = 0
    if s[0] in a:
        x+=1
    if s[1] in a:
        x+=1
    if s[2] in a:
        x+=1
    if s[3] in a:
        x+=1
    if s[4] in a:
        x+=1
    return x
print (main('12345'))
def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    x = s.find("*")
    print ("bu xning qiymati = ", x)
    if x != -1:
        return x
    else: 
        return False
print (main('272*'))
        
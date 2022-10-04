"""

Make the password even stronger - no triple repeats

RULE: A strong password requires:

1) a minimum of 8 Characters
2) at least one UpperCase Letter
3) at least one LowerCase Letter
4) at least one Number
5) at least one Special Character
6) no sequence of 3 or more repeating characters

"""
MIN_PW = 8


# Simple function to validate the password meets the specified criteria

def validate_strong_password(password):
    # Assume required characters not found
    upp = False
    low = False
    num = False
    spc = False
    cnt = False

    # Assume three repeating characters not found
    no_rpt = True

    # Validate all conditions

    pw_len = len(password)
    if pw_len >= MIN_PW:
        cnt = True

    for eachChar in password:
        if eachChar in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upp = True
        elif eachChar in "abcdefghijklmnopqrstuvwxyz":
            low = True
        elif eachChar in "0123456789":
            num = True
        elif eachChar in "!@#$%^&*()_-=+/\';><,.>":
            spc = True
        else:
            continue

        """
        Check for triple repeats

       """
    pos = 0
    for eachChar in password:
        if eachChar == password[pos + 1] and password[pos + 2]:
            no_rpt = False

    if upp and low and num and spc and cnt and no_rpt:
        return True
    else:
        return False


# Main Program Starts Here
# ===================================

if __name__ == '__main__':

    if validate_strong_password("A11aBC!!11"):
        print("Strong")
    else:
        print("Weak")

# The End!

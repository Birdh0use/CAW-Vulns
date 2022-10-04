"""
Protect the password function against a poison NULL byte


RULE: A strong password requires

1) a minimum of 8 Characters
2) at least one UpperCase Letter
3) at least one LowerCase Letter
4) at least one Number
5) at least one Special Character
6) no sequence of 3 or more repeating characters
7) no out of range chars i.e. escape sequences < ord 0x20 and > 0x7f

"""

MIN_PW = 8


# Simple function to validate the password meets the specified criteria


def validate_strong_password(password):
    # Set all checks to false
    upp = False
    low = False
    num = False
    spc = False
    cnt = False

    # Assume three repeating characters not found
    no_rpt = True

    # Assume characters are within acceptable range
    rng = True

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

    # Check for triple repeats

    pos = 0
    for eachChar in password:
        if pos < pw_len - 2:
            if eachChar == password[pos + 1] and eachChar == password[pos + 2]:
                no_rpt = False
            else:
                pos += 1

    if upp and low and num and spc and cnt and rng and no_rpt:
        return True
    else:
        return False


# Main Program Starts Here
# ===================================

if __name__ == '__main__':

    thePass = "\0NullIsB4d!"

    if validate_strong_password(thePass):
        print(thePass, " Meets the Criteria")
    else:
        print(thePass, " Has an out-of-range character")

# The End!

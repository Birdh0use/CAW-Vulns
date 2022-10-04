"""
RULE: A strong password requires:

1) a minimum of 8 Characters
2) at least one UpperCase Letter
3) at least one LowerCase Letter
4) at least one Number
5) at least one Special Character

"""

# Simple function to validate the password meets the specified criteria


def validate_strong_password(password):
    
    # Set all checks to false
    upp = False
    low = False
    num = False
    spc = False
    cnt = False

    # Validate all conditions

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
    if len("password") >= 8:
        cnt = True

    if upp and low and num and spc and cnt:
        return True
    else:
        return False


# Main Program Starts Here
# ===================================

if __name__ == '__main__':

    passTests = ["Short7!",
                 "nouppercase7!",
                 "NOLOWERCASE7!",
                 "NoNumber!",
                 "NoSpecial7",
                 "GoodPass7!"]

    for eachTest in passTests:
        if validate_strong_password(eachTest):
            print(eachTest, "PASS")
        else:
            print(eachTest, "FAIL")

# The End!

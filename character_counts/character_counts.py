import string

promt = input("Enter a sentence: ")

upper = 0
lower = 0
digits = 0
punctuation = 0

for char in promt:
    if char in string.ascii_uppercase:
        upper += 1
    elif char in string.ascii_lowercase:
        lower += 1
    elif char in string.digits:
        digits += 1
    elif char in string.punctuation:
        punctuation += 1

print(\
"{:>15}{:>5} \n\
{:>15}{:>5} \n\
{:>15}{:>5} \n\
{:>15}{:>5}".format("Upper", upper, "Lower", lower, "Digits", digits, "Puncuation", punctuation))
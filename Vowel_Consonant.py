character = input("enter a character:")
if len(character)==1 and character.isalpha():
    vowels = "aeiouAEIOU"
    if character in vowels:
         print(f"{character} is a vowel.")
    else:
        print(f"{character} is a consonant.")
else:
    print("Please enter a single alphabet character.")
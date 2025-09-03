word = input("Enter the word: ")
reversed_word = word[::-1]

print(f"Reversed: {reversed_word}")

if word.lower() == reversed_word.lower():
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")

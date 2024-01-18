import itertools
import random
import datetime

numbers = '0123456789'
special_chars = '!@#$%^&*()'

def generate_passwords(words):
    for word in words.split():
        yield word

        # Append numbers and special characters at random positions
        for num in numbers:
            for _ in range(50):  
                i = random.randint(0, len(word))
                yield word[:i] + str(num) + word[i:]
        for char in special_chars:
            for _ in range(50):  
                i = random.randint(0, len(word))
                yield word[:i] + char + word[i:]

        # Append combinations of numbers and special characters
        for num, char in itertools.product(numbers, special_chars):
            for _ in range(50):  
                i = random.randint(0, len(word))
                yield word[:i] + str(num) + char + word[i:]

        # Append multiple special characters at random positions
        for length in range(2, 11):  # 2 to 10 special characters
            for chars in itertools.combinations(special_chars, length):  
                for _ in range(50):  
                    i = random.randint(0, len(word))
                    yield word[:i] + ''.join(str(char) for char in chars) + word[i:]
    for word in words.split():
        word = word[::-1]  # Reverse the word
        yield word

        # Append numbers and special characters at random positions
        for num in numbers:
            for _ in range(50):  
                i = random.randint(0, len(word))
                yield word[:i] + str(num) + word[i:]
        for char in special_chars:
            for _ in range(50):  
                i = random.randint(0, len(word))
                yield word[:i] + char + word[i:]

        # Append combinations of numbers and special characters
        for num, char in itertools.product(numbers, special_chars):
            for _ in range(50):  
                i = random.randint(0, len(word))
                yield word[:i] + str(num) + char + word[i:]

        # Append multiple special characters at random positions
        for length in range(2, 11):  # 2 to 10 special characters
            for chars in itertools.combinations(special_chars, length):  
                for _ in range(50):  
                    i = random.randint(0, len(word))
                    yield word[:i] + ''.join(str(char) for char in chars) + word[i:]
    combined_word = ''.join(word for word in words if word != ' ')

    # Append numbers and special characters at random positions
    for num in numbers:
        for _ in range(50):  
            i = random.randint(0, len(combined_word))
            yield combined_word[:i] + str(num) + combined_word[i:]
    for char in special_chars:
        for _ in range(50):  
            i = random.randint(0, len(combined_word))
            yield word[:i] + char + word[i:]

    # Append combinations of numbers and special characters
    for num, char in itertools.product(numbers, special_chars):
        for _ in range(50):  
            i = random.randint(0, len(combined_word))
            yield word[:i] + str(num) + char + combined_word[i:]

    # Append multiple special characters at random positions
    for length in range(2, 11):  # 2 to 10 special characters
        for chars in itertools.combinations(special_chars, length):  
            for _ in range(50):  
                i = random.randint(0, len(combined_word))
                yield combined_word[:i] + ''.join(str(char) for char in chars) + combined_word[i:]

def save_to_file(passwords):
    filename = "passwords_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".txt"
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')
    print("Success: Passwords saved to file.")

words = input("Enter words to generate passwords: ")
passwords = generate_passwords(words)
save_to_file(passwords)
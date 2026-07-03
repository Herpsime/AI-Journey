def analyze():
    user_input = input("Input:\n").strip()
    
    if not user_input:
        print("\n cannot be empty.")
        return

    vowels_set = "aeiouAEIOU"
    consonants_set = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    length = len(user_input)
    
    vowels_count = 0
    consonants_count = 0
    for char in user_input:
        if char in vowels_set:
            vowels_count += 1
        elif char in consonants_set:
            consonants_count += 1
            
    reverse_text = user_input[::-1]
    
    clean_text = ""
    for char in user_input:
        if char.isalnum():
            clean_text += char.lower()
    is_palindrome = "Yes" if clean_text == clean_text[::-1] else "No"
    
    uppercase_text = user_input.upper()
    lowercase_text = user_input.lower()
    
    words_list = user_input.split()
    word_count = len(words_list)

    print("\n Output:\n")
    print(f"Length: {length}")
    print(f"Vowels: {vowels_count}")
    print(f"Consonants: {consonants_count}")
    print(f"Reverse: {reverse_text}")
    print(f"Palindrome?: {is_palindrome}")
    print(f"Uppercase: {uppercase_text}")
    print(f"Lowercase: {lowercase_text}")
    print(f"Number of words: {word_count}")

if __name__ == "__main__":
    analyze()

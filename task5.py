from collections import Counter
import string

def analyze_text(text):
    print(f"original text: '{text}'")
    print("-" * 40)
    
    chars_to_count = text.lower()
    chars_freq = Counter(chars_to_count)
    
    print("character freq:")
    for char, count in sorted(chars_freq.items()):
        display_char = "' '" if char == " " else repr(char)
        print(f" {display_char}: {count}")
        
    print("-" * 40)
    
    clean_text = text.translate(str.maketrans("", "", string.punctuation))
    words = clean_text.lower().split()
    word_freq = Counter(words)
    
    print("word freq:")
    for word, count in sorted(word_freq.items()):
        print(f" '{word}': {count}")
        
if __name__ == "__main__":
    user_input = input("Enter text to analyze: ")
    
    if user_input.strip():
        analyze_text(user_input)
    else:
        print("Error: you entered an empty string.")
		
	

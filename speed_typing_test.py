import random
import time

def get_random_words(num_words):
    word_list = [
        "python", "programming", "language", "speed", "typing",
        "test", "keyboard", "computer", "developer", "challenge",
        "practice", "openai", "accuracy", "coding", "learning"
    ]
    return random.sample(word_list, num_words)

def calculate_typing_speed(start_time, end_time, num_words):
    total_time = end_time - start_time
    words_per_minute = (num_words / total_time) * 60
    return words_per_minute

def calculate_typing_accuracy(original_text, typed_text):
    correct_characters = sum(1 for a, b in zip(original_text, typed_text) if a == b)
    accuracy = (correct_characters / len(original_text)) * 100
    return accuracy

def main():
    num_words = 5
    words_to_type = get_random_words(num_words)

    print("Welcome to the Speed Typing Test!")
    print("Type the following words:")
    print(" ".join(words_to_type))

    input("Press Enter when you are ready to start...")
    start_time = time.time()

    typed_text = input("Type the words here: ")
    end_time = time.time()

    typing_speed = calculate_typing_speed(start_time, end_time, num_words)
    typing_accuracy = calculate_typing_accuracy(" ".join(words_to_type), typed_text)

    print(f"Typing Speed: {typing_speed:.2f} words per minute")
    print(f"Typing Accuracy: {typing_accuracy:.2f}%")

if __name__ == "__main__":
    main()

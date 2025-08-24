# text_repit.py
# সহজ Text Repeat স্ক্রিপ্ট

# কোন মডিউল ইন্সটল করার দরকার নেই

def repeat_text():
    print("=== Text Repit Program ===\n")
    
    text = input("Enter text to repeat: ")
    
    while True:
        try:
            count = int(input("How many times to repeat: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    print("\n--- Result ---")
    for i in range(count):
        print(f"{i+1}: {text}")

if __name__ == "__main__":
    repeat_text()

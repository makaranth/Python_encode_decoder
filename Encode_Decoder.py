def encode(text):
    return ''.join(chr(ord(char) + 1000) for char in text)

def decode(symbols):
    return ''.join(chr(ord(char) - 1000) for char in symbols)

def main():
    while True: 
        choice = input("Use Decoder or Encoder (e/d): ").strip().lower()

        if choice == 'e':
            text = input("Enter the text to encode: ").strip()
            encoded = encode(text)
            print(f"Output: {encoded}")
            break
        elif choice == 'd':
            symbols = input("Enter the text to decode: ").strip()
            decoded = decode(symbols)
            print(f"Output: {decoded}")
            break
        else:
            print("Invalid choice. Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()

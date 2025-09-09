# RSA Algorithm Implementation in Python
import time

def generateKeys():
    # Step 1: Choose two distinct prime numbers p and q
    p = int(input("Enter First prime number (p): "))
    q = int(input("Enter Second prime number (q): "))

    # Step 2: Compute n = p * q and φ(n) = (p - 1)(q - 1)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # step 3: Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    e = 0
    for e in range(2, phi_n):
        if gcd(e, phi_n) == 1:
            break

    # Compute d such that e * d ≡ 1 (mod phi(n))
    d = mod_inverse(e, phi_n)

    return e, d, n

# Function to compute gcd
def gcd(a, b):
    while b: 
        a, b = b, a % b
    return a

# Function to compute modular inverse of e mod phi_n
def mod_inverse(e, phi_n):
    for d in range(2, phi_n):
        if (d * e) % phi_n == 1:
            return d
    return None

# Funtion to convert message to numeraic representation (A-Z -> 1-26)
def messageToNumber(message):
    message_num = []
    symbol_map = {
        '.': 64,
        ',': 65,
        '!': 66,
        '?': 67
    }
    for char in message:
        if char.isupper():  # A-Z -> 1-26
            message_num.append(ord(char) - ord('A') + 1)
        elif char.islower():  # a-z -> 1-26 + 26 = 27-52
            message_num.append(ord(char) - ord('a') + 27)
        elif char.isdigit():  # 0-9 -> 53-62
            message_num.append(ord(char) - ord('0') + 53)
        elif char == " ":  # space
            message_num.append(63)
        elif char in symbol_map:  # punctuation
            message_num.append(symbol_map[char])
        else:  # fallback
            message_num.append(0)

    return message_num

# Function to convert numbers back to message
def numberToMessage(numbers):
    reverse_map = {
        63: " ",
        64: ".",
        65: ",",
        66: "!",
        67: "?"
    }
    message = ""
    for num in numbers:
        if 1 <= num <= 26:  # A-Z
            message += chr(num + ord('A') - 1)
        elif 27 <= num <= 52:  # a-z
            message += chr(num - 27 + ord('a'))
        elif 53 <= num <= 62:  # 0-9
            message += chr(num - 53 + ord('0'))
        elif num in reverse_map:
            message += reverse_map[num]
        else:
            message += "?"
    return message

# Function to encrypt message
def encryptMessage(message_num, e, n):
    encrypted_msg = [pow(m, e, n) for m in message_num]
    return encrypted_msg

# Function to decrypt message
def decryptMessage(encrypted_msg, d, n):
    return [pow(c, d, n) for c in encrypted_msg]

if __name__ == "__main__":
    
    # Key Generation
    e, d, n = generateKeys()

    print(f"Chosen e: {e}")
    print(f"Computed d: {d}")
    print(f"Computed n: {n}")

    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    # Message Input
    message = input("Enter the message to be encrypted: ")

    # Convert Message to Number
    message_num = messageToNumber(message)
    print(f"Numeric representation of the message: {message_num}")

    # Encrypt Message
    encryptedMessage = encryptMessage(message_num, e, n)
    print(f"Encrypted message: {encryptedMessage}")

    print("\nSending encrypted message...")
    time.sleep(1)
    print("Message sent!\n")
    # Decrypt Message
    decrypted_num = decryptMessage(encryptedMessage, d, n)
    print(f"Decrypted numeric message: {decrypted_num}")

    # Convert back to text
    decryptedMessage = numberToMessage(decrypted_num)
    print(f"Your message is: {decryptedMessage}")
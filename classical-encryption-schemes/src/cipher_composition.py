from . import monoalphabetic, columnar_transposition

def double_encrypt(plaintext, mono_key, columnar_key):
    """
    Perform double encryption:
    1. First apply monoalphabetic substitution
    2. Then apply columnar transposition
    """
    # Step 1: Monoalphabetic encryption
    step1 = monoalphabetic.encrypt(plaintext, mono_key)

    # Step 2: Columnar transposition
    ciphertext = columnar_transposition.encrypt(step1, columnar_key)

    return ciphertext, step1  # Return both final ciphertext and intermediate result

def double_decrypt(ciphertext, mono_key, columnar_key):
    """
    Decrypt double-encrypted text:
    1. First undo columnar transposition
    2. Then undo monoalphabetic substitution
    """
    # Step 1: Columnar transposition decryption
    step1 = columnar_transposition.decrypt(ciphertext, columnar_key)

    # Step 2: Monoalphabetic decryption
    plaintext = monoalphabetic.decrypt(step1, mono_key)

    return plaintext, step1  # Return both plaintext and intermediate result

def attack_double_cipher(ciphertext, cipher_types):
    """
    Attempt to decrypt a double-encrypted ciphertext.
    cipher_types: list like ["monoalphabetic", "columnar"]

    This function provides a framework for attempting cryptanalysis
    without knowing the keys.
    """
    print(f"Attempting to break double cipher with types: {cipher_types}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Ciphertext length: {len(ciphertext)}")

    # Analysis suggestions
    print("\nAnalysis approach:")
    if "columnar" in cipher_types:
        print("- Try different key lengths for columnar transposition")
        print("- Look for patterns that might reveal the grid structure")

    if "monoalphabetic" in cipher_types:
        print("- After removing transposition, use frequency analysis")
        print("- Look for common English words/patterns")

    return None  # Placeholder for manual/automated attack

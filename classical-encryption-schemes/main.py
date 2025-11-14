from src import caesar, monoalphabetic, columnar_transposition
from src import cipher_composition, frequency_analysis

def task1_basic_ciphers():
    """Task 1: Implement and Test Basic Ciphers"""
    print("\n" + "="*70)
    print("TASK 1: BASIC CIPHERS")
    print("="*70)

    # Caesar Cipher
    print("\n1. Caesar Cipher")
    print("-" * 50)
    text = "HELLO"
    shift = 7
    encrypted = caesar.encrypt(text, shift)
    decrypted = caesar.decrypt(encrypted, shift)
    print(f"Plaintext: {text}")
    print(f"Shift: {shift}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Verification: {'✓ PASS' if decrypted == text else '✗ FAIL'}")

    # Monoalphabetic Substitution Cipher
    print("\n2. Monoalphabetic Substitution Cipher")
    print("-" * 50)
    text = "ATTACK"
    key = monoalphabetic.generate_key()
    encrypted = monoalphabetic.encrypt(text, key)
    decrypted = monoalphabetic.decrypt(encrypted, key)
    print(f"Plaintext: {text}")
    print(f"Key: {key}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Verification: {'✓ PASS' if decrypted == text else '✗ FAIL'}")

    # Columnar Transposition Cipher
    print("\n3. Columnar Transposition Cipher")
    print("-" * 50)
    text = "MEETMEATTHEUSUALPLACE"
    key = "CIPHER"
    encrypted = columnar_transposition.encrypt(text, key)
    decrypted = columnar_transposition.decrypt(encrypted, key)
    print(f"Plaintext: {text}")
    print(f"Key: {key}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Verification: {'✓ PASS' if decrypted == text else '✗ FAIL'}")

def task2_cipher_composition():
    """Task 2: Cipher Composition - Double Encryption"""
    print("\n" + "="*70)
    print("TASK 2: CIPHER COMPOSITION (Double Encryption)")
    print("="*70)

    # Create a message to encrypt
    plaintext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"

    # Generate keys
    mono_key = monoalphabetic.generate_key()
    columnar_key = "SET"

    print(f"\nOriginal Plaintext: {plaintext}")
    print(f"Monoalphabetic Key: {mono_key}")
    print(f"Columnar Key: {columnar_key}")

    # Encrypt
    ciphertext, intermediate = cipher_composition.double_encrypt(
        plaintext, mono_key, columnar_key
    )

    print(f"\nAfter Monoalphabetic: {intermediate}")
    print(f"After Columnar (Final): {ciphertext}")

    # Decrypt
    decrypted, intermediate_decrypt = cipher_composition.double_decrypt(
        ciphertext, mono_key, columnar_key
    )

    print(f"\nDecryption Process:")
    print(f"After Columnar Decrypt: {intermediate_decrypt}")
    print(f"Final Plaintext: {decrypted}")
    print(f"Verification: {'PASS' if decrypted == plaintext else 'FAIL'}")

    # Save a ciphertext for "exchange"
    print("\n" + "-"*70)
    print("CIPHERTEXT FOR EXCHANGE WITH OTHER GROUPS:")
    print("-"*70)
    print(f"Ciphertext: {ciphertext}")
    print(f"Cipher Types Used: Monoalphabetic + Columnar Transposition")
    print("(Keys are secret!)")

def task3_frequency_analysis():
    """Task 3: Cryptanalysis by Frequency Analysis"""
    print("\n" + "="*70)
    print("TASK 3: FREQUENCY ANALYSIS CRYPTANALYSIS")
    print("="*70)

    # Read the ciphertext from file
    print("\nAnalyzing Ciphertext 1 from Sample_Ciphertexts_for_Cr.txt")
    ciphertext1 = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"

    # Perform frequency analysis
    letter_freq, suggested_mapping, initial_decrypt = frequency_analysis.analyze_ciphertext(
        ciphertext1, show_top_n=15
    )

    # Manual refinement (if needed)
    print("\n" + "="*70)
    print("REFINEMENT NOTES")
    print("="*70)
    print("The initial frequency-based mapping may not be perfect.")
    print("Common words like 'THE', 'AND', 'FOR' can help refine the mapping.")
    print("\nLooking at the pattern 'QEB' appearing twice...")
    print("This is likely 'THE' (the most common 3-letter word in English)")

    # Apply refined mapping based on pattern recognition
    refined_mapping = suggested_mapping.copy()
    # If we recognize QEB as THE:
    refined_mapping['Q'] = 'T'
    refined_mapping['E'] = 'H'
    refined_mapping['B'] = 'E'

    print("\nApplying refined mapping with Q→T, E→H, B→E:")
    refined_decrypt = frequency_analysis.apply_mapping(ciphertext1, refined_mapping)
    print(f"Refined decryption: {refined_decrypt}")


def main():
    """Main function to run all lab tasks"""
    print("\n" + "#"*70)
    print("# CLASSICAL ENCRYPTION LAB")
    print("# ICS570 - Cybersecurity Essentials")
    print("#"*70)

    # Run Task 1
    task1_basic_ciphers()

    # Run Task 2
    task2_cipher_composition()

    # Run Task 3
    task3_frequency_analysis()
if __name__ == "__main__":
    main()

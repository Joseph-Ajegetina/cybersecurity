from src import caesar, monoalphabetic, columnar_transposition
from src import cipher_composition, improved_frequency_analysis, brute_force

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
    print("\n" + "="*80)
    print(" "*20 + "TASK 3: CRYPTANALYSIS")
    print("="*80)

    # Ciphertext 1 (Monoalphabetic/Caesar)
    ciphertext1 = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"

    # Ciphertext 2 (Columnar Transposition)
    ciphertext2 = "DNETHEEFTLALTAEEWHDLSOCEASTFLLO"

    # Ciphertext 3 (Double Encryption)
    ciphertext3 = "HTEI QUNCI KBRWO NFOXU MPSJO VRETH ELAZY DOG"

    common_words = ["THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL", "CAN",
                    "HER", "WAS", "ONE", "OUR", "OUT", "HAD", "HAS", "HIS", "HOW",
                    "QUICK", "BROWN", "JUMP", "OVER", "LAZY", "DOG", "FOX", "ATTACK",
                    "MEET", "PLACE", "TIME", "HAVE", "FROM", "THEY", "BEEN", "THAT",
                    "WITH", "WILL", "ABOUT", "THERE", "THEIR", "WOULD", "COULD",
                    "DEFEND", "FLEET", "USUAL", "EAST", "WEST", "NORTH", "SOUTH"]

    # CIPHERTEXT 1 ANALYSIS
    print("\n" + "="*80)
    print("CIPHERTEXT 1: Monoalphabetic/Caesar Cipher")
    print("="*80)
    print(f"Ciphertext: {ciphertext1}")

    print("\n[Method 1] Frequency Analysis:")
    mapping1, decrypted1 = improved_frequency_analysis.frequency_attack(ciphertext1)

    print("\n[Method 2] Caesar Brute Force:")
    found_count = 0
    for shift in range(26):
        decrypted = caesar.decrypt(ciphertext1, shift)
        if any(word in decrypted.upper() for word in common_words):
            print(f"    Shift {shift}: {decrypted}")
            found_count += 1

    if found_count == 0:
        print("    No meaningful decryptions found")

    # CIPHERTEXT 2 ANALYSIS
    print("\n\n" + "="*80)
    print("CIPHERTEXT 2: Columnar Transposition")
    print("="*80)
    print(f"Ciphertext: {ciphertext2}")
    print(f"Length: {len(ciphertext2)}")

    print("\n[Method 1] Trying Common Transposition Keys:")
    trans_keys = ["KEY", "CODE", "CIPHER", "SECRET", "HELLO", "WORLD", "FLED",
                  "FLEET", "MEET", "ALPHA", "BETA", "GAMMA"]

    found_trans = False
    for key in trans_keys:
        try:
            decrypted = columnar_transposition.decrypt(ciphertext2, key)
            if any(word in decrypted.upper() for word in common_words):
                print(f"    Key '{key}': {decrypted}")
                found_trans = True
        except:
            pass

    if not found_trans:
        print("    No match with common keys")

    print("\n[Method 2] Pattern Analysis:")
    print(f"    Visible fragments: {'THE' if 'THE' in ciphertext2 else 'None'}, "
          f"{'EAST' if 'EAST' in ciphertext2 else 'None'}, "
          f"{'FLEET' if 'FLEET' in ciphertext2 else 'None'}")

    # CIPHERTEXT 3 ANALYSIS
    print("\n\n" + "="*80)
    print("CIPHERTEXT 3: Double Encryption")
    print("="*80)
    print(f"Ciphertext: {ciphertext3}")
    print(f"Length: {len(ciphertext3.replace(' ', ''))}")

    ciphertext3_clean = ciphertext3.replace(" ", "")

    print("\n[Method 1] Transposition → Caesar:")
    found_double = False
    for trans_key in trans_keys[:10]:
        try:
            intermediate = columnar_transposition.decrypt(ciphertext3_clean, trans_key)
            for shift in range(26):
                decrypted = caesar.decrypt(intermediate, shift)
                if any(word in decrypted.upper() for word in common_words):
                    print(f"    Trans '{trans_key}' + Caesar {shift}: {decrypted}")
                    found_double = True
                    break
            if found_double:
                break
        except:
            pass

    if not found_double:
        print("    No match with Transposition → Caesar")

    print("\n[Method 2] Caesar → Transposition:")
    for shift in range(26):
        intermediate = caesar.decrypt(ciphertext3_clean, shift)
        for trans_key in trans_keys[:10]:
            try:
                decrypted = columnar_transposition.decrypt(intermediate, trans_key)
                if any(word in decrypted.upper() for word in common_words):
                    print(f"    Caesar {shift} + Trans '{trans_key}': {decrypted}")
                    found_double = True
                    break
            except:
                pass
        if found_double:
            break

    if not found_double:
        print("    No match with Caesar → Transposition")

    print("\n[Method 3] Pattern Recognition:")
    print(f"    Visible words: {'LAZY' if 'LAZY' in ciphertext3 else 'None'}, "
          f"{'DOG' if 'DOG' in ciphertext3 else 'None'}")
    print("    This suggests partial transposition or weak encryption")
        

def task_brute_force():
    """Task 4: Comprehensive Brute Force Attack on Double Encryption"""
    print("\n" + "="*70)
    print("TASK 4: COMPREHENSIVE BRUTE FORCE ATTACK")
    print("="*70)

    print("\nThis task attempts to break double-encrypted ciphertexts using")
    print("all possible combinations of cipher techniques:")
    print("  • Caesar cipher (26 shifts)")
    print("  • Columnar transposition (common keys + permutations)")
    print("  • Transposition → Caesar")
    print("  • Caesar → Transposition")
    print("  • Double transposition")
    print("  • Transposition → Monoalphabetic (requires frequency analysis)")

    ciphertexts = [
        "GYQMETIUPK",
        "UESMOBZCLHJFLANXDVWMXIRMIGYQMETIUPK"
    ]

    print("\n" + "="*70)
    print("ATTACKING RECEIVED CIPHERTEXTS FROM OTHER GROUPS")
    print("="*70)

    brute_force.attack_multiple_ciphertexts(ciphertexts)

    print("\n" + "="*70)
    print("CREATING TEST DOUBLE ENCRYPTION FOR DEMONSTRATION")
    print("="*70)

    plaintext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    trans_key = "KEY"
    shift = 5

    print(f"\nPlaintext: {plaintext}")
    print(f"Transposition Key: {trans_key}")
    print(f"Caesar Shift: {shift}")

    intermediate = columnar_transposition.encrypt(plaintext, trans_key)
    test_ciphertext = caesar.encrypt(intermediate, shift)

    print(f"\nAfter Transposition: {intermediate}")
    print(f"After Caesar (Final): {test_ciphertext}")

    print("\n" + "-"*70)
    print("Now attempting to break this ciphertext...")
    print("-"*70)

    brute_force.comprehensive_attack(test_ciphertext)

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

    # Run Task 4
    task_brute_force()

if __name__ == "__main__":
    main()

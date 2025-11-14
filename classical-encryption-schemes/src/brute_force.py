from . import caesar, monoalphabetic, columnar_transposition
import itertools
import string


COMMON_WORDS = ["THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL", "CAN",
                "HER", "WAS", "ONE", "OUR", "OUT", "HAD", "HAS", "HIS", "HOW",
                "QUICK", "BROWN", "JUMP", "OVER", "LAZY", "DOG", "FOX", "ATTACK",
                "MEET", "PLACE", "TIME", "HAVE", "FROM", "THEY", "BEEN", "THAT",
                "WITH", "WILL", "ABOUT", "THERE", "THEIR", "WOULD", "COULD",
                "DEFEND", "FLEET", "USUAL", "EAST", "WEST", "NORTH", "SOUTH"]

COMMON_TRANS_KEYS = ["KEY", "CODE", "CIPHER", "SECRET", "HELLO", "WORLD",
                     "QUICK", "BROWN", "FLED", "FLEE", "FLEET", "ALPHA",
                     "BETA", "GAMMA", "DELTA", "TIGER", "LION", "BEAR",
                     "SET", "GET", "PUT", "NEW", "OLD", "BIG", "TOP"]


def check_english(text):
    text_upper = text.upper()
    word_count = sum(1 for word in COMMON_WORDS if word in text_upper)
    return word_count >= 2


def caesar_attack(ciphertext):
    print("\n[1] CAESAR CIPHER BRUTE FORCE")
    print("-" * 60)

    results = []
    for shift in range(26):
        decrypted = caesar.decrypt(ciphertext, shift)
        if check_english(decrypted):
            results.append((shift, decrypted))
            print(f"    Shift {shift:2d}: {decrypted}")

    return results


def transposition_attack(ciphertext):
    print("\n[2] COLUMNAR TRANSPOSITION BRUTE FORCE")
    print("-" * 60)

    results = []
    tested_count = 0

    print(f"    Testing {len(COMMON_TRANS_KEYS)} common keys...")
    for key in COMMON_TRANS_KEYS:
        try:
            decrypted = columnar_transposition.decrypt(ciphertext, key)
            tested_count += 1
            if check_english(decrypted):
                results.append((key, decrypted))
                print(f"    ✓ Key '{key}': {decrypted}")
        except:
            pass

    print(f"    Testing permutations (2-5 letters)...")
    perm_count = 0
    for length in range(2, 6):
        for perm in itertools.permutations(string.ascii_uppercase[:length]):
            key = ''.join(perm)
            perm_count += 1
            if perm_count % 100 == 0:
                print(f"      Tested {perm_count} permutations...", end='\r')
            try:
                decrypted = columnar_transposition.decrypt(ciphertext, key)
                if check_english(decrypted):
                    results.append((key, decrypted))
                    print(f"\n    ✓ Key '{key}': {decrypted}")
            except:
                pass

    print(f"\n    Total tested: {tested_count + perm_count} keys")
    if not results:
        print(f"    No matches found")

    return results


def transposition_then_caesar_attack(ciphertext):
    print("\n[3] TRANSPOSITION → CAESAR (DOUBLE ENCRYPTION)")
    print("-" * 60)

    results = []

    for trans_key in COMMON_TRANS_KEYS[:15]:
        try:
            intermediate = columnar_transposition.decrypt(ciphertext, trans_key)

            for shift in range(26):
                decrypted = caesar.decrypt(intermediate, shift)
                if check_english(decrypted):
                    results.append((trans_key, shift, decrypted))
                    print(f"    Trans '{trans_key}' + Caesar {shift}: {decrypted}")
                    return results
        except:
            pass

    return results


def caesar_then_transposition_attack(ciphertext):
    print("\n[4] CAESAR → TRANSPOSITION (DOUBLE ENCRYPTION)")
    print("-" * 60)

    results = []

    for shift in range(26):
        intermediate = caesar.decrypt(ciphertext, shift)

        for trans_key in COMMON_TRANS_KEYS[:15]:
            try:
                decrypted = columnar_transposition.decrypt(intermediate, trans_key)
                if check_english(decrypted):
                    results.append((shift, trans_key, decrypted))
                    print(f"    Caesar {shift} + Trans '{trans_key}': {decrypted}")
                    return results
            except:
                pass

    return results


def double_transposition_attack(ciphertext):
    print("\n[5] DOUBLE TRANSPOSITION")
    print("-" * 60)

    results = []

    for key1 in COMMON_TRANS_KEYS[:10]:
        try:
            intermediate = columnar_transposition.decrypt(ciphertext, key1)

            for key2 in COMMON_TRANS_KEYS[:10]:
                try:
                    decrypted = columnar_transposition.decrypt(intermediate, key2)
                    if check_english(decrypted):
                        results.append((key1, key2, decrypted))
                        print(f"    Keys '{key1}' + '{key2}': {decrypted}")
                        return results
                except:
                    pass
        except:
            pass

    return results


def transposition_then_monoalphabetic_attack(ciphertext):
    print("\n[6] TRANSPOSITION → MONOALPHABETIC")
    print("-" * 60)

    print("    Note: Monoalphabetic has 26! possible keys (too large to brute force)")
    print("    This attack requires frequency analysis on the intermediate text")

    results = []

    for trans_key in COMMON_TRANS_KEYS[:5]:
        try:
            intermediate = columnar_transposition.decrypt(ciphertext, trans_key)
            print(f"    Trans '{trans_key}' → Intermediate: {intermediate[:50]}...")
        except:
            pass

    return results


def comprehensive_attack(ciphertext):
    print("\n" + "=" * 70)
    print(" " * 15 + "COMPREHENSIVE BRUTE FORCE ATTACK")
    print("=" * 70)
    print(f"\nTarget Ciphertext: {ciphertext}")
    print(f"Length: {len(ciphertext)} characters")
    print(f"\nAttempting all attack methods...\n")

    all_results = []

    result1 = caesar_attack(ciphertext)
    if result1:
        all_results.extend([("Caesar", r) for r in result1])

    if not result1:
        result2 = transposition_attack(ciphertext)
        if result2:
            all_results.extend([("Transposition", r) for r in result2])

    if not result1 and not result2:
        result3 = transposition_then_caesar_attack(ciphertext)
        if result3:
            all_results.extend([("Trans→Caesar", r) for r in result3])

    if not result1 and not result2 and not result3:
        result4 = caesar_then_transposition_attack(ciphertext)
        if result4:
            all_results.extend([("Caesar→Trans", r) for r in result4])

    if not all_results:
        result5 = double_transposition_attack(ciphertext)
        if result5:
            all_results.extend([("Double Trans", r) for r in result5])

    if not all_results:
        result6 = transposition_then_monoalphabetic_attack(ciphertext)
        if result6:
            all_results.extend([("Trans→Mono", r) for r in result6])

    print("\n" + "=" * 70)
    print("SUMMARY OF RESULTS")
    print("=" * 70)

    if not all_results:
        print("\n⚠  NO SUCCESSFUL DECRYPTIONS FOUND")
        print("\nPossible reasons:")
        print("  • Key not in common key list (need to expand search)")
        print("  • More complex cipher combination than tested")
        print("  • Monoalphabetic substitution (requires frequency analysis)")
        print("  • Custom/uncommon encryption scheme")
        print("\nSuggestions:")
        print("  • Try expanding the common key list")
        print("  • Test longer key permutations (6-7 letters)")
        print("  • Use frequency analysis for substitution ciphers")
    else:
        print(f"\n✓ SUCCESSFULLY DECRYPTED!")
        print(f"Found {len(all_results)} result(s):\n")
        for i, (method, result) in enumerate(all_results, 1):
            print(f"Result {i}:")
            print(f"  Method: {method}")
            if isinstance(result, tuple) and len(result) >= 2:
                if method == "Caesar":
                    print(f"  Shift: {result[0]}")
                    print(f"  Plaintext: {result[1]}")
                elif method == "Transposition":
                    print(f"  Key: '{result[0]}'")
                    print(f"  Plaintext: {result[1]}")
                elif "→" in method:
                    print(f"  Details: {result[:-1]}")
                    print(f"  Plaintext: {result[-1]}")
            print()

    return all_results


def attack_multiple_ciphertexts(ciphertexts):
    print("\n" + "=" * 70)
    print(" " * 10 + "ATTACKING MULTIPLE CIPHERTEXTS")
    print("=" * 70)

    for i, ciphertext in enumerate(ciphertexts, 1):
        print(f"\n{'=' * 70}")
        print(f"CIPHERTEXT {i}")
        print('=' * 70)
        comprehensive_attack(ciphertext)

# Standard English letter frequencies (from the lab document)
ENGLISH_FREQ = {
    'E': 12.7020, 'T': 9.0560, 'A': 8.1670, 'O': 7.5070, 'I': 6.9660,
    'N': 6.7490, 'S': 6.3270, 'H': 6.0940, 'R': 5.9870, 'D': 4.2530,
    'L': 4.0250, 'C': 2.7820, 'U': 2.7580, 'M': 2.4060, 'W': 2.3600,
    'F': 2.2280, 'G': 2.0150, 'Y': 1.9740, 'P': 1.9290, 'B': 1.4920,
    'V': 0.9780, 'K': 0.7720, 'J': 0.1530, 'X': 0.1500, 'Q': 0.0950,
    'Z': 0.0740
}

def compute_frequency(text):
    """
    Compute the frequency of each letter in the text.
    Returns a dictionary with letter counts and percentages.
    """
    # Count only alphabetic characters
    text = text.upper()
    letter_count = {}
    total_letters = 0

    for char in text:
        if char.isalpha():
            total_letters += 1
            letter_count[char] = letter_count.get(char, 0) + 1

    # Calculate percentages
    letter_freq = {}
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        count = letter_count.get(letter, 0)
        percentage = (count / total_letters * 100) if total_letters > 0 else 0
        letter_freq[letter] = {
            'count': count,
            'percentage': percentage
        }

    return letter_freq, total_letters

def display_frequency(letter_freq, total_letters, top_n=10):
    """
    Display frequency analysis results in a readable format.
    """
    # Sort by count descending
    sorted_letters = sorted(letter_freq.items(),
                          key=lambda x: x[1]['count'],
                          reverse=True)

    print(f"\nTotal letters analyzed: {total_letters}")
    print(f"\nTop {top_n} most frequent letters:")
    print("-" * 50)
    print(f"{'Letter':<10}{'Count':<10}{'Percentage':<15}{'Bar'}")
    print("-" * 50)

    for i, (letter, data) in enumerate(sorted_letters[:top_n]):
        count = data['count']
        percentage = data['percentage']
        bar = '█' * int(percentage)
        print(f"{letter:<10}{count:<10}{percentage:>6.2f}%      {bar}")

    return sorted_letters

def compare_with_english(letter_freq):
    """
    Compare computed frequencies with standard English frequencies.
    Returns suggested mappings based on frequency matching.
    """
    # Sort ciphertext letters by frequency
    cipher_sorted = sorted(letter_freq.items(),
                          key=lambda x: x[1]['percentage'],
                          reverse=True)

    # Sort English letters by frequency
    english_sorted = sorted(ENGLISH_FREQ.items(),
                          key=lambda x: x[1],
                          reverse=True)

    print("\n" + "=" * 70)
    print("FREQUENCY ANALYSIS COMPARISON")
    print("=" * 70)
    print(f"{'Cipher':<10}{'Cipher %':<15}{'English':<10}{'English %':<15}{'Suggested Mapping'}")
    print("-" * 70)

    suggested_mapping = {}
    for i in range(min(15, len(cipher_sorted))):
        cipher_letter = cipher_sorted[i][0]
        cipher_pct = cipher_sorted[i][1]['percentage']
        english_letter = english_sorted[i][0]
        english_pct = english_sorted[i][1]

        suggested_mapping[cipher_letter] = english_letter

        print(f"{cipher_letter:<10}{cipher_pct:>6.2f}%       {english_letter:<10}{english_pct:>6.2f}%       {cipher_letter} → {english_letter}")

    return suggested_mapping

def apply_mapping(ciphertext, mapping):
    """
    Apply a character mapping to decrypt the ciphertext.
    """
    result = ""
    for char in ciphertext:
        if char.upper() in mapping:
            mapped_char = mapping[char.upper()]
            # Preserve case
            result += mapped_char if char.isupper() else mapped_char.lower()
        else:
            result += char
    return result

def manual_adjust_mapping(mapping, from_char, to_char):
    """
    Manually adjust the mapping for trial and refinement.
    """
    mapping[from_char.upper()] = to_char.upper()
    return mapping

def analyze_ciphertext(ciphertext, show_top_n=15):
    """
    Perform complete frequency analysis on a ciphertext.
    Returns frequency data and suggested mapping.
    """
    print("=" * 70)
    print("ANALYZING CIPHERTEXT")
    print("=" * 70)
    print(f"\nCiphertext:\n{ciphertext}")
    print(f"\nLength: {len(ciphertext)} characters")

    # Compute frequencies
    letter_freq, total_letters = compute_frequency(ciphertext)

    # Display frequencies
    sorted_letters = display_frequency(letter_freq, total_letters, show_top_n)

    # Compare with English and get suggested mapping
    suggested_mapping = compare_with_english(letter_freq)

    # Apply suggested mapping
    print("\n" + "=" * 70)
    print("APPLYING SUGGESTED MAPPING")
    print("=" * 70)
    initial_decrypt = apply_mapping(ciphertext, suggested_mapping)
    print(f"\nInitial decryption attempt:\n{initial_decrypt}")

    return letter_freq, suggested_mapping, initial_decrypt

def interactive_refinement(ciphertext, mapping):
    """
    Interactive function to refine the mapping.
    (For manual use in the main script)
    """
    print("\n" + "=" * 70)
    print("MANUAL REFINEMENT")
    print("=" * 70)
    print("Use this function to manually adjust mappings.")
    print("Example: mapping = manual_adjust_mapping(mapping, 'Q', 'T')")
    print("Then reapply: apply_mapping(ciphertext, mapping)")

    return mapping

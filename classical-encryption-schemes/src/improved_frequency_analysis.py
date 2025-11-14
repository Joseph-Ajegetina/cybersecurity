from collections import Counter
import re


ENGLISH_FREQ = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
    'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
    'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
    'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
    'Q': 0.10, 'Z': 0.07
}

COMMON_BIGRAMS = ['TH', 'HE', 'IN', 'ER', 'AN', 'RE', 'ON', 'AT', 'EN', 'ND',
                  'TI', 'ES', 'OR', 'TE', 'OF', 'ED', 'IS', 'IT', 'AL', 'AR']

COMMON_TRIGRAMS = ['THE', 'AND', 'ING', 'HER', 'HAT', 'HIS', 'THA', 'ERE',
                   'FOR', 'ENT', 'ION', 'TER', 'WAS', 'YOU', 'ITH', 'VER']

COMMON_WORDS = ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT', 'YOU', 'ALL', 'CAN',
                'HAD', 'HER', 'WAS', 'ONE', 'OUR', 'OUT', 'DAY', 'GET', 'HAS',
                'HIM', 'HIS', 'HOW', 'MAN', 'NEW', 'NOW', 'OLD', 'SEE', 'TWO',
                'WAY', 'WHO', 'BOY', 'DID', 'ITS', 'LET', 'PUT', 'SAY', 'SHE',
                'TOO', 'USE', 'THAT', 'WITH', 'HAVE', 'THIS', 'WILL', 'YOUR',
                'FROM', 'THEY', 'KNOW', 'WANT', 'BEEN', 'GOOD', 'MUCH', 'SOME']


def compute_frequency(text):
    clean_text = re.sub(r'[^A-Z]', '', text.upper())
    total = len(clean_text)

    if total == 0:
        return {}

    counts = Counter(clean_text)
    freqs = {letter: (count / total * 100) for letter, count in counts.items()}

    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if letter not in freqs:
            freqs[letter] = 0.0

    return freqs


def extract_ngrams(text, n):
    clean_text = re.sub(r'[^A-Z]', '', text.upper())
    return [clean_text[i:i+n] for i in range(len(clean_text) - n + 1)]


def score_english_text(text):
    text_upper = text.upper()
    score = 0

    words = text_upper.split()
    for word in words:
        if word in COMMON_WORDS:
            score += 10

    bigrams = extract_ngrams(text_upper, 2)
    bigram_counts = Counter(bigrams)
    for bigram in COMMON_BIGRAMS[:10]:
        score += bigram_counts.get(bigram, 0) * 2

    trigrams = extract_ngrams(text_upper, 3)
    trigram_counts = Counter(trigrams)
    for trigram in COMMON_TRIGRAMS[:10]:
        score += trigram_counts.get(trigram, 0) * 5

    letter_freq = compute_frequency(text_upper)
    freq_diff = sum(abs(letter_freq.get(letter, 0) - ENGLISH_FREQ[letter])
                    for letter in ENGLISH_FREQ)
    score -= freq_diff / 10

    return score


def find_pattern_words(ciphertext):
    words = ciphertext.upper().split()
    patterns = {}

    for word in words:
        pattern = get_word_pattern(word)
        if pattern not in patterns:
            patterns[pattern] = []
        patterns[pattern].append(word)

    return patterns


def get_word_pattern(word):
    pattern = []
    mapping = {}
    counter = 0

    for char in word:
        if char not in mapping:
            mapping[char] = str(counter)
            counter += 1
        pattern.append(mapping[char])

    return '.'.join(pattern)


def suggest_mapping_from_patterns(ciphertext):
    mapping = {}

    words = ciphertext.upper().split()

    for word in words:
        if len(word) == 3 and word[0] == word[2]:
            continue

        if len(word) == 3:
            cipher_pattern = get_word_pattern(word)
            if cipher_pattern == '0.1.2':
                common_3letter = ['THE', 'AND', 'FOR', 'ARE', 'BUT', 'NOT']
                for candidate in common_3letter:
                    temp_mapping = {word[i]: candidate[i] for i in range(3)}
                    if not mapping or all(mapping.get(k) == v for k, v in temp_mapping.items()):
                        mapping.update(temp_mapping)
                        break

    return mapping


def frequency_attack(ciphertext, use_patterns=True, use_ngrams=True):
    print("="*80)
    print("ADVANCED FREQUENCY ANALYSIS ATTACK")
    print("="*80)

    print(f"\nCiphertext: {ciphertext}")
    print(f"Length: {len(ciphertext)} characters")

    cipher_freq = compute_frequency(ciphertext)

    print("\n--- FREQUENCY ANALYSIS ---")
    cipher_sorted = sorted(cipher_freq.items(), key=lambda x: x[1], reverse=True)
    english_sorted = sorted(ENGLISH_FREQ.items(), key=lambda x: x[1], reverse=True)

    print(f"{'Cipher':<10}{'Freq %':<10}{'→':<5}{'English':<10}{'Freq %'}")
    print("-"*50)

    base_mapping = {}
    for i in range(min(10, len(cipher_sorted))):
        if cipher_sorted[i][1] > 0:
            cipher_letter = cipher_sorted[i][0]
            cipher_pct = cipher_sorted[i][1]
            english_letter = english_sorted[i][0]
            english_pct = english_sorted[i][1]

            base_mapping[cipher_letter] = english_letter
            print(f"{cipher_letter:<10}{cipher_pct:>6.2f}%  →  {english_letter:<10}{english_pct:>6.2f}%")

    if use_patterns:
        print("\n--- PATTERN RECOGNITION ---")
        pattern_mapping = suggest_mapping_from_patterns(ciphertext)
        if pattern_mapping:
            print("Found pattern-based mappings:")
            for cipher, plain in pattern_mapping.items():
                print(f"  {cipher} → {plain}")
            base_mapping.update(pattern_mapping)

    if use_ngrams:
        print("\n--- BIGRAM ANALYSIS ---")
        cipher_bigrams = Counter(extract_ngrams(ciphertext, 2))
        top_cipher_bigrams = cipher_bigrams.most_common(5)
        print("Most common bigrams in ciphertext:", [bg for bg, _ in top_cipher_bigrams])
        print("Most common bigrams in English:", COMMON_BIGRAMS[:5])

    best_mapping = base_mapping.copy()
    best_score = score_english_text(apply_mapping(ciphertext, best_mapping))

    print("\n--- TRYING VARIATIONS ---")
    print("Testing different mapping combinations...")

    variations_tested = 0
    improvements = 0

    for i in range(min(5, len(cipher_sorted))):
        for j in range(min(5, len(english_sorted))):
            test_mapping = base_mapping.copy()
            test_mapping[cipher_sorted[i][0]] = english_sorted[j][0]

            test_decrypt = apply_mapping(ciphertext, test_mapping)
            test_score = score_english_text(test_decrypt)

            variations_tested += 1

            if test_score > best_score:
                best_score = test_score
                best_mapping = test_mapping.copy()
                improvements += 1

    print(f"Tested {variations_tested} variations, found {improvements} improvements")

    print("\n--- FINAL DECRYPTION ---")
    final_decrypt = apply_mapping(ciphertext, best_mapping)
    print(f"Decrypted text: {final_decrypt}")
    print(f"English score: {best_score:.2f}")

    print("\n--- FINAL MAPPING ---")
    for cipher, plain in sorted(best_mapping.items()):
        print(f"  {cipher} → {plain}")

    return best_mapping, final_decrypt


def apply_mapping(ciphertext, mapping):
    result = ""
    for char in ciphertext:
        if char.upper() in mapping:
            mapped = mapping[char.upper()]
            result += mapped if char.isupper() else mapped.lower()
        else:
            result += char
    return result



# Classical Encryption Lab

**ICS570 - Cybersecurity Essentials**
**Ashesi University**
**Date:** November 14, 2025

## Overview

This project implements and analyzes classical encryption techniques including substitution and transposition ciphers. The lab demonstrates both the implementation of these ciphers and their cryptanalytic weaknesses.

**Recommended Reading:** William Stallings, "Cryptography and Network Security," Chapter 2 (Classical Encryption Techniques).

## Project Structure

```
classical-encryption-schemes/
├── src/
│   ├── __init__.py
│   ├── caesar.py                    # Caesar cipher implementation
│   ├── monoalphabetic.py            # Monoalphabetic substitution cipher
│   ├── columnar_transposition.py    # Columnar transposition cipher
│   ├── playfair.py                  # Playfair cipher
│   ├── rail_fence.py                # Rail fence cipher
│   ├── cipher_composition.py        # Double encryption (Task 2)
│   └── frequency_analysis.py        # Cryptanalysis tools (Task 3)
├── main.py                          # Main demonstration script
├── REFLECTION.md                    # Task 4 - Written analysis
├── Sample_Ciphertexts_for_Cr.txt   # Sample ciphertexts
└── README.md                        # This file
```

## Lab Tasks Completed

- [x] **Task 1:** Implement and test basic ciphers
  - Caesar Cipher ✓
  - Monoalphabetic Cipher ✓
  - Columnar Transposition Cipher ✓

- [x] **Task 2:** Cipher Composition - Double encryption scheme ✓

- [x] **Task 3:** Cryptanalysis by Frequency Analysis ✓

- [x] **Task 4:** Reflection and Questions ✓

## Running the Lab

```bash
# Run all tasks
python main.py

# The output will show:
# - Task 1: Basic cipher demonstrations
# - Task 2: Double encryption example
# - Task 3: Frequency analysis demonstration
```

## Table of Contents

1.  [Caesar Cipher](#1-caesar-cipher)
2.  [Monoalphabetic Substitution Cipher](#2-monoalphabetic-substitution-cipher)
3.  [Playfair Cipher](#3-playfair-cipher)
4.  [Rail Fence Cipher](#4-rail-fence-cipher)
5.  [Columnar Transposition Cipher](#5-columnar-transposition-cipher)
6.  [Frequency Analysis and Keyspace](#6-frequency-analysis-and-keyspace)
7.  [Task 2: Double Encryption](#7-task-2-double-encryption)
8.  [Task 3: Frequency Analysis](#8-task-3-frequency-analysis)
9.  [AI Usage Declaration](#9-ai-usage-declaration)

---

## 1. Caesar Cipher

The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

*   **Key:** The shift value (e.g., 3).
*   **Encryption:** `C = E(k, p) = (p + k) mod 26`
*   **Decryption:** `p = D(k, C) = (C - k) mod 26`

**Example (Key = 3):**

*   **Plaintext:** `HELLO`
*   **Ciphertext:** `KHOOR`

---

## 2. Monoalphabetic Substitution Cipher

A monoalphabetic substitution cipher is a cipher in which each letter of the plaintext is replaced by a corresponding letter of the ciphertext alphabet. The ciphertext alphabet is a permutation of the plaintext alphabet.

*   **Key:** A permutation of the 26 letters of the alphabet.

**Example:**

*   **Plaintext Alphabet:** `A B C D E F G H I J K L M N O P Q R S T U V W X Y Z`
*   **Ciphertext Alphabet:** `Q W E R T Y U I O P A S D F G H J K L Z X C V B N M`
*   **Plaintext:** `ATTACK`
*   **Ciphertext:** `QZZQEA`

---

## 3. Playfair Cipher

The Playfair cipher is a digraph substitution cipher, meaning that it encrypts pairs of letters (digraphs) instead of single letters. It uses a 5x5 grid of letters constructed from a keyword.

**Key Construction (Keyword: `MONARCHY`):**

The 5x5 grid is filled with the unique letters of the keyword, followed by the remaining letters of the alphabet in order (I and J are typically treated as the same letter).

| M | O | N | A | R |
|---|---|---|---|---|
| C | H | Y | B | D |
| E | F | G | I/J | K |
| L | P | Q | S | T |
| U | V | W | X | Z |

**Encryption Rules:**

1.  **Repeating letters:** If both letters in a digraph are the same, or if there is only one letter left, add an 'X' after the first letter.
2.  **Letters in the same row:** Replace each letter with the letter to its right (wrapping around to the start of the row if necessary).
3.  **Letters in the same column:** Replace each letter with the letter below it (wrapping around to the top of the column if necessary).
4.  **Letters in a rectangle:** Replace each letter with the letter in the same row but in the column of the other letter.

**Example (Plaintext: `BALLOON`):**

1.  `BA` -> `DB` (rectangle rule)
2.  `LX` (X added to L) -> `PT` (rectangle rule)
3.  `LO` -> `PO` (rectangle rule)
4.  `ON` -> `NA` (same row)

*   **Ciphertext:** `DBPT PONA`

---

## 4. Rail Fence Cipher

The Rail Fence cipher is a form of transposition cipher that gets its name from the way in which it is encoded. The plaintext is written downwards and diagonally on successive "rails" of an imaginary fence, then read off in rows.

*   **Key:** The number of rails.

**Example (Key = 3):**

*   **Plaintext:** `WE ARE DISCOVERED FLEE AT ONCE`

```
W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
```

*   **Ciphertext:** `WECRLTEERDSOEEFEAOCAIVDEN`

---

## 5. Columnar Transposition Cipher

The columnar transposition cipher is a transposition cipher that involves writing the plaintext out in rows of a fixed length, and then reading the ciphertext out column by column. The columns are read in an order determined by a keyword.

*   **Key:** A keyword (e.g., `ZEBRA`).

**Example (Keyword: `ZEBRA` -> `5 3 2 4 1`):**

*   **Plaintext:** `WE ARE DISCOVERED FLEE AT ONCE`

| Z(5) | E(3) | B(2) | R(4) | A(1) |
|---|---|---|---|---|
| W | E | A | R | E |
| D | I | S | C | O |
| V | E | R | E | D |
| F | L | E | E | A |
| T | O | N | C | E |

*   **Ciphertext (read by column order 1, 2, 3, 4, 5):** `EOAEEASRNEICLEFWDVFTO`

---

## 6. Frequency Analysis and Keyspace

### Frequency Analysis

Frequency analysis is the study of the frequency of letters or groups of letters in a ciphertext. In most languages, certain letters and combinations of letters appear with characteristic frequencies. This can be used to break substitution ciphers.

*   **English Letter Frequencies:** E is the most common letter, followed by T, A, O, I, N, S, H, R.

### Keyspace

The keyspace of a cipher is the set of all possible keys. The size of the keyspace is a measure of the cipher's resistance to brute-force attacks.

*   **Caesar Cipher:** Keyspace = 26
*   **Monoalphabetic Substitution Cipher:** Keyspace = 26! (approximately 4 x 10^26)
*   **Playfair Cipher:** Keyspace is large, but the cipher has structural weaknesses.

---

## 7. Task 2: Double Encryption

This task implements a cipher composition scheme that combines monoalphabetic substitution and columnar transposition.

### Implementation

The double encryption works in two stages:

1. **Stage 1:** Apply monoalphabetic substitution cipher
2. **Stage 2:** Apply columnar transposition on the result

### Usage Example

```python
from src import cipher_composition, monoalphabetic

plaintext = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
mono_key = monoalphabetic.generate_key()
columnar_key = "SECRET"

# Encrypt
ciphertext, intermediate = cipher_composition.double_encrypt(
    plaintext, mono_key, columnar_key
)

# Decrypt
decrypted, _ = cipher_composition.double_decrypt(
    ciphertext, mono_key, columnar_key
)
```

### Security Analysis

The double encryption provides:
- Increased resistance to frequency analysis (substitution breaks patterns)
- Increased resistance to anagramming (transposition scrambles positions)
- Combined approach significantly stronger than either cipher alone
- Still vulnerable to sophisticated cryptanalysis techniques

---

## 8. Task 3: Frequency Analysis

This task demonstrates cryptanalysis of monoalphabetic substitution ciphers using letter frequency analysis.

### How It Works

1. **Compute letter frequencies** in the ciphertext
2. **Compare with known English frequencies** (E, T, A, O, I, N, S are most common)
3. **Suggest initial mappings** based on frequency matching
4. **Refine mappings** using pattern recognition (common words like THE, AND, FOR)

### Usage Example

```python
from src import frequency_analysis

ciphertext = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"

# Perform complete analysis
letter_freq, mapping, initial_decrypt = frequency_analysis.analyze_ciphertext(
    ciphertext, show_top_n=15
)

# Manual refinement based on patterns
refined_mapping = mapping.copy()
refined_mapping['Q'] = 'T'  # QEB appears twice, likely "THE"
refined_mapping['E'] = 'H'
refined_mapping['B'] = 'E'

result = frequency_analysis.apply_mapping(ciphertext, refined_mapping)
```

### Results

The frequency analysis successfully breaks monoalphabetic ciphers by:
- Identifying the most common letters
- Matching patterns with common English words
- Iteratively refining the mapping until plaintext emerges

---

## 9. AI Usage Declaration

This lab was completed with AI assistance using Claude Code (Anthropic's Claude Sonnet 4.5).

**See `REFLECTION.md` for:**
- Complete AI usage declaration
- All prompts used
- Detailed analysis of security weaknesses
- Keyspace calculations
- Hybrid cipher design proposal

### Key Learning Outcomes

Through this lab, students learn:
1. How classical ciphers work (implementation details)
2. Why classical ciphers are insecure (cryptanalysis techniques)
3. How to combine multiple cipher techniques
4. The importance of understanding both algorithms and their weaknesses
5. Foundation concepts for modern cryptography

---

## Documentation

- **REFLECTION.md** - Complete written analysis for Task 4
- **main.py** - Run to see all tasks demonstrated
- **src/** - Individual cipher implementations

## Author

**Course:** ICS570 - Cybersecurity Essentials
**Institution:** Ashesi University
**Date:** November 14, 2025

# cybersecurity

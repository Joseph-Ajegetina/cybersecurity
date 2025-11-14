import math

def encrypt(text, key):
    # Create a mapping from original position to sorted position
    key_with_indices = [(char, i) for i, char in enumerate(key)]
    key_sorted = sorted(key_with_indices)

    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)

    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    text_index = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if text_index < len(text):
                matrix[i][j] = text[text_index]
                text_index += 1

    ciphertext = ""
    for char, original_col in key_sorted:
        for i in range(num_rows):
            if matrix[i][original_col]:  # Only add non-empty cells
                ciphertext += matrix[i][original_col]

    return ciphertext

def decrypt(text, key):
    # Create a mapping from original position to sorted position
    key_with_indices = [(char, i) for i, char in enumerate(key)]
    key_sorted = sorted(key_with_indices)

    num_cols = len(key)
    num_rows = math.ceil(len(text) / num_cols)

    # Calculate how many columns have full rows
    num_empty_cells = (num_cols * num_rows) - len(text)

    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]

    text_index = 0
    # Read column by column in sorted key order
    for char, original_col in key_sorted:
        # Determine how many rows this column has
        # The last row might be incomplete - check if this column should have num_rows elements
        # Columns at the end (rightmost) are the ones that get cut off first
        rows_in_col = num_rows if original_col < (num_cols - num_empty_cells) else num_rows - 1
        for i in range(rows_in_col):
            if text_index < len(text):
                matrix[i][original_col] = text[text_index]
                text_index += 1

    # Read row by row to get plaintext
    plaintext = ""
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j]:  # Only add non-empty cells
                plaintext += matrix[i][j]

    return plaintext

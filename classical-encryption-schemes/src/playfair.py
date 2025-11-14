def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    for char in key:
        if char not in matrix:
            matrix.append(char)
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
            
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def get_pos(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def encrypt(text, key):
    matrix = generate_matrix(key)
    text = text.upper().replace("J", "I")
    text = text.replace(" ", "")
    
    # Add 'X' for repeated letters
    i = 0
    while i < len(text) - 1:
        if text[i] == text[i+1]:
            text = text[:i+1] + 'X' + text[i+1:]
        i += 2
        
    if len(text) % 2 != 0:
        text += 'X'
        
    ciphertext = ""
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i+1]
        row1, col1 = get_pos(matrix, char1)
        row2, col2 = get_pos(matrix, char2)
        
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
            
    return ciphertext

def decrypt(text, key):
    matrix = generate_matrix(key)
    text = text.upper()
    
    plaintext = ""
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i+1]
        row1, col1 = get_pos(matrix, char1)
        row2, col2 = get_pos(matrix, char2)
        
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    if plaintext.endswith('X'):
        plaintext = plaintext[:-1]
            
    return plaintext

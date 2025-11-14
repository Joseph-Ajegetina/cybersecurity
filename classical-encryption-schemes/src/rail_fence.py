def encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in text:
        fence[rail].append(char)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
            
    return "".join([char for rail in fence for char in rail])

def decrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail_lengths = [0] * rails
    rail = 0
    direction = 1
    
    for _ in text:
        rail_lengths[rail] += 1
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
            
    index = 0
    for i in range(rails):
        fence[i] = list(text[index:index+rail_lengths[i]])
        index += rail_lengths[i]
        
    result = []
    rail = 0
    direction = 1
    
    for _ in range(len(text)):
        result.append(fence[rail].pop(0))
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction
            
    return "".join(result)

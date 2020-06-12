def tribonacci(signature, n):  
    if n < 3: return [signature[i] for i in range(n)]
    else :
        [signature.append(sum(signature[-3:])) for i in range(n-3)]
        return signature
print(tribonacci([1, 1, 1], 10))
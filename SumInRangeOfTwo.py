def get_sum(a,b):
    schowek = 0
    if a==b : return a
    elif b>a:  
        for x in range (a, b): schowek+=x
        if b>=0 : schowek += b
        else : schowek+=b
        return schowek
    else:
        for x in range (b, a): schowek+=x           
        if a>=0 : schowek += a
        else : schowek+=a
        return schowek


print(get_sum(-1,-5))
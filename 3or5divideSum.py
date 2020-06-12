#zlicza sume liczb podzielnych przez 3 lub 5, ponizej podanej. Jesli jakas z liczb jest podzielna przez obie, to do sumy ma sie liczyc tylko raz
def solution(number):
    schowek = 0
    for i in range (number): 
        if (i%3 == 0) or (i%5 == 0): schowek+=i
    return schowek
#print(solution(10))
import random
import math
#i added something hereeee

#chose 2 prime numbers
p, q = 0, 0
while True:
    n1 = random.randint(1, 100)
    n2 = random.randint(100, 1000)
    for i in range(min(n1, n2), max(n1,n2)):
        end = int(i ** 0.5)
        prime = True
        for j in range(2, end+1):
            if i % j == 0:
                prime = False
                break
        if prime == True:
            p = i
            break
    if p != 0:
        break
print('p = ', p)
while True:
    n1 = random.randint(1, 100)
    n2 = random.randint(100, 1000)
    for i in range(min(n1, n2), max(n1,n2)):
        end = int(i ** 0.5)
        prime = True
        for j in range(2, end+1):
            if i % j == 0:
                prime = False
                break
        if prime == True:
            q = i
            break
    if q != 0 and q != p:
        break
print('q = ', q)
eyler_func = (p - 1)*(q - 1)
print("Функция Эйлера: ", eyler_func)
m = p * q
e = 0 #mutually prime with eyler_func
while True:
    n1 = random.randint(1, 100)
    n2 = random.randint(100, 300)
    for i in range(n1, n2):
        if math.gcd(i, eyler_func) == 1:
            e = i
            break
    if e != 0 and e != eyler_func:
        break
print("Открытая часть ключа (m, e): ", m, e)
# def extended_euclidean_algorithm(a, b):
#     """
#     extended_euclidean_algorithm(a, b)

#     The result is the largest common divisor for a and b.

#     :param a: integer number
#     :param b: integer number
#     :return:  the largest common divisor for a and b
#     """

#     if a == 0:
#         return b, 0, 1
#     else:
#         g, y, x = extended_euclidean_algorithm(b % a, a)
#         return g, x - (b // a) * y, y
    
# def modular_inverse(e, t):
#     """
#     modular_inverse(e, t)

#     Counts modular multiplicative inverse for e and t.

#     :param e: in this case e is a public key exponent
#     :param t: and t is an Euler function
#     :return:  the result of modular multiplicative inverse for e and t
#     """

#     g, x, y = extended_euclidean_algorithm(e, t)

#     if g != 1:
#         raise Exception('Modular inverse does not exist')
#     else:
#         return x % t
d = 0
for i in range(e+1, 100000):
    if (e * i) % eyler_func == 1:
        d = i
        break
# d = modular_inverse(e, eyler_func)
print('Закрытая часть ключа d = ', d)
#creating alphabet
alphabet = {}
alphabet_nums_first = {}
ind = 0 
for i in range(ord('А'), ord('Я')+1):
    ind += 1
    alphabet[chr(i)] = ind
    alphabet_nums_first[ind] = chr(i)
# print(alphabet_nums_first)
# print(alphabet)
word = str(input('Введите слово для шифрования: '))
code = []
#encryption process
for letter in word:
    c = alphabet[letter.upper()] ** e % m
    code.append(c)
print("Слово в зашифрованном виде: ", code)
#transcryption process
transcryption = []
for c in code:
    decoding = c ** d % m
    transcryption.append(decoding)
print("Слово в расшифрованном виде (числами): ", transcryption)
result = ''
for t in transcryption:
    letter = alphabet_nums_first[t]
    result += letter
print("Расшифрованное: ", result)
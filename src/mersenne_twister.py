import random

w = 32
n = 624
m = 397
f = 1812433253
r = 31
u = 11
s = 7
t = 15
a = 2567483615
d = 4294967295
b = 2636928640
c = 4022730752
mod = pow(2, w)

MT = [0] * n
index = n + 1
lower_mask = (1 << r) - 1
upper_mask = (~lower_mask) % mod

def seed_mt(seed):
    global index

    index = n
    MT[0] = seed
    for i in range(1, n):
        MT[i] = (f * (MT[i - 1] ^ (MT[i - 1] >> (w - 2)) + i)) % mod

def extract_number():
    global index

    if index >= n:
        if index > n:
            print("Generator was never seeded")
            return -1
        twist()

    y = MT[index]
    y = y ^ ((y >> u) & d)
    y = y ^ ((y << s) & b)
    y = y ^ ((y << t) & c)
    y = y ^ (y >> 1)

    index += 1
    return y % mod

def twist():
    global index

    for i in range(n):
        x = (MT[i] & upper_mask) | (MT[(i  + 1) % n] & lower_mask)
        xa = x >> 1
        if (x % 2) != 0:
            xa = xa ^ a
        MT[i] = MT[(i + m) % n] ^ xa
    index = 0

def test_mersenne():
    random.seed(5)
    print(random.randint(0, mod))

seed_mt(5)

res = [-1] * 624
for i in range(624):
    res[i] = extract_number()
test_mersenne()
print("res = ", res)

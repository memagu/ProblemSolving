n_k = n_b = 0
for letter in input():
    n_k += letter == 'k'
    n_b += letter == 'v'

if n_k == n_b == 0:
    print("none")
elif n_k == n_b:
    print("boki")
elif n_k > n_b:
    print("kiki")
else:
    print("boba")


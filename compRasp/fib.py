# A01732610 - Dafne Vania Peña Cortés

print("Los primeros 19 números de la serie Fibonacci son:")
n = 18

n_minus_two = 0
print(f"{n_minus_two}, ", end='', flush=True)
n_minus_one = 1
print(f"{n_minus_one}, ", end='', flush=True)

for num in range(2, n+1):
   temp = n_minus_one + n_minus_two
   if num < n:
       print(f"{temp}, ", end='', flush=True)
   else:
       print(f"{temp}", flush=True)
   n_minus_two = n_minus_one
   n_minus_one = temp

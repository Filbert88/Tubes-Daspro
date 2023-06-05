
import time
# def LCGRecursive(seed:int, multiplier : int,increment : int,modulus : int, n :int) -> int :
#     if n == 0 :
#         return seed
#     else :
#         return (multiplier * LCGRecursive(seed,multiplier,increment,modulus,n-1) + increment) % modulus
    
# def LCGRecursiveList(seed: int, multiplier:int,increment:int,modulus:int,n:int)-> list[int]:
#     if n ==  0 :
#         return [seed]
#     else :
#         return LCGRecursiveList(seed,multiplier,increment,modulus,n-1) + [LCGRecursive(seed,multiplier,increment,modulus,n)]
  
# def random_int(max_value: int) -> int:
#     seed = int(time.time() * 1000) # Use current time in milliseconds as seed
#     multiplier = 1103515245
#     increment = 12345
#     modulus = 2**31 - 1
#     return LCGRecursive(seed, multiplier, increment, modulus, 1) % max_value

# def random_list(length: int, max_value: int) -> list[int]:
#     seed = int(time.time() * 1000) # Use current time in milliseconds as seed
#     multiplier = 1103515245
#     increment = 12345
#     modulus = 2**31 - 1
#     return LCGRecursiveList(seed, multiplier, increment, modulus, length)[:length]

# def LCGRecursive(seed:int, multiplier:int, increment:int, modulus:int, n:int) -> list[int]:
#     if n == 0:
#         return []
#     else:
#         result = [(multiplier * LCGRecursive(seed, multiplier, increment, modulus, n-1)[n-1] + increment) % modulus]
#         return LCGRecursive(seed, multiplier, increment, modulus, n-1) + result

# def RNGkumpul(seed):
#     a = 1103515245
#     b = 12345
#     m = 2 ** 31
#     seed = (a * seed + b) % m
#     rand_num = seed % (6) 
#     print(rand_num)
#     return rand_num, seed

def RNGBangun(seed, min_val, max_val):
    a = 1103515245
    b = 12345
    m = 2 ** 31
    seeds = (a * seed + b) % m
    seed=seeds
    rand_num = (seed % (max_val - min_val + 1)) + min_val
    return rand_num, seed
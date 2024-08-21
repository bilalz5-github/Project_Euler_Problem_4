def is_palindrome(i):
    return str(i) == str(i)[::-1]

max_p = 0

for i in range(100, 1000):
    for j in range(i + 1, 1000):
        p = i * j
        if is_palindrome(p) and p > max_p:
            max_p = p  # Update max_p with the new largest palindrome

print(max_p)  

s = input("Enter the string: ")
d = {}


for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1


max_freq = 0
max_char = ''
for char, freq in d.items():
    if freq > max_freq:
        max_freq = freq
        max_char = char

print(f"The character with maximum frequency is '{max_char}' with frequency {max_freq}.")

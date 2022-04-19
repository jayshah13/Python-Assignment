string = input()
print(string[::-1])
frequencies = {}
for char in string: 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1

sort_frequencies = sorted(frequencies.items(), key = lambda x: x[1], reverse = True)
print(sort_frequencies)
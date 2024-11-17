num_strings = int(input())

strings = []

for _ in range(num_strings):
    strings.append(input())

def fft(strings):
    n = len(strings)
    results = []
    
    for i in range(n - 2):
        if strings[i][0] == 'F' and strings[i+1][0] == 'F' and strings[i+2][0] == 'T':
            results.append(f"{strings[i]} {strings[i+1]} {strings[i+2]}")
    
    return results

numOfMatches = len(fft(strings))
print(numOfMatches)

outputs = fft(strings)
for i in range(0,len(outputs)):
    print(outputs[i])
print("Podaj liczbe po enterze podaj kolejne liczby")

areTheSame = "true"
n = input()
numbers = [n]
numbers = input()
for i in range(int(n)):
    if numbers[i] != numbers[i+1]:
        areTheSame = "false"
        break
    else:
        i+1

print(areTheSame)
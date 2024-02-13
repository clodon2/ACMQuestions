numSequence = input("Enter 0-4 numbers 2-9: ")

numLetters = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
              "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

possibleCombos = [""]

for num in numSequence:
    combos = []
    for letter in numLetters[num]:
        for combo in possibleCombos:
            combos.append(combo + letter)
    possibleCombos = combos

print(possibleCombos)

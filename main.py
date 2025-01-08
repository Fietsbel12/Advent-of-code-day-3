rucksacksFile = open("dag.txt", "r", encoding="UTF-8")
rucksacksList = rucksacksFile.read().splitlines()

def calculate_priority(item):
    if 'a' <= item <= 'z':
        return ord(item) - ord('a') + 1
    elif 'A' <= item <= 'Z':
        return ord(item) - ord('A') + 27
    else:
        return 0  # Ongeldig itemtype

for sack in rucksacksList:
    line = sack.strip()

    compartment_size = len(line) // 2
    left = line[:compartment_size]
    right = line[compartment_size:]

    print("Rucksack contents:", line)
    print("Left compartment:", left)
    print("Right compartment:", right)

    # Bereken de prioriteit van het gedeelde itemtype tussen de compartimenten
    common_item = set(left) & set(right)
    if common_item:
        common_item_priority = calculate_priority(common_item.pop())
        print("Priority of common item:", common_item_priority)
    else:
        print("No common item found")

    print("------")

    

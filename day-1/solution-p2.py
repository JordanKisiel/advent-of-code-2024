# take in two lists of nums from file
# for each num in the first list, find the number
# of occurrences in the second list,
# mulitiply the num being searched for by the
# occurrences in the second list and total
# all those products 

# thought:
# I should cache the occurrences for each num
# in the first list so I don't have to recalculate
# needlessly

def main():
    with open("day-1/input.txt", 'r') as input:
        lines = input.readlines()
        lst1 = []
        lst2 = []
        for line in lines:
            num1 = line.split("   ")[0]
            num2 = line.split("   ")[1].strip()
            lst1.append(int(num1))
            lst2.append(int(num2))
        
        occurrences_cache = {}
        similiarity_score = 0

        for num1 in lst1:
            if num1 not in occurrences_cache:
                occurrences_cache[num1] = 0
            
                for num2 in lst2:
                    if num1 == num2:
                        occurrences_cache[num1] += 1
            
            
            similiarity_score += (num1 * occurrences_cache[num1])

        print(similiarity_score)
            

main()
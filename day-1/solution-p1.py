# take in two lists of nums from file
# pair up the number in order of size
# (i.e. smallest with smallest, 2nd smallest with
# 2nd smallest etc.)
# find the distance (absolute value) between each pair
# find sum of all distances

def main():
    with open("day-1/input.txt", 'r') as input:
        lines = input.readlines()
        lst1 = []
        lst2 = []
        for line in lines:
            num1 = line.split("   ")[0]
            num2 = line.split("   ")[1].strip()
            lst1.append(num1)
            lst2.append(num2)
        
        lst1.sort() 
        lst2.sort() 

        sum = 0

        i = 0

        while i < len(lst1):
            distance = abs(int(lst1[i]) - int(lst2[i]))
            sum += distance
            i += 1

        print(sum)


main()
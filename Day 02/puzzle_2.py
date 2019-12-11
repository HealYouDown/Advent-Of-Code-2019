import sys

with open("Day 2/input.txt", "r") as f:
    og_data = [int(i) for i in f.readline().split(",")]

for noun in range(0, 100):
    for verb in range(0, 100):
        
        data = [i for i in og_data]  # copy list
        
        index = 0
        data[1] = noun
        data[2] = verb
        
        while True:
            optcode = data[index]

            num1_pos = data[index+1]
            num1 = data[num1_pos]

            num2_pos = data[index+2]
            num2 = data[num2_pos]
            
            store_pos = data[index+3]
            
            if optcode == 1:
                data[store_pos] = num1 + num2
            elif optcode == 2:
                data[store_pos] = num1 * num2
            elif optcode == 99:
                break
            else:
                print("Unknown Optcode", optcode)

            index += 4

        if data[0] == 19690720:
            result = (100 * noun) + verb
            print(result)
            sys.exit()

with open("Day 2/input.txt", "r") as f:
    data = [int(i) for i in f.readline().split(",")]

data[1] = 12
data[2] = 2

index = 0
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

print(data[0])

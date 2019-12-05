with open("Day 5/input.txt", "r") as f:
    data = [int(i) for i in f.readline().split(",")]

index = 0
while True:
    instruction = str(data[index])
    optcode = int(instruction[-2:])

    if optcode == 99:
        break

    # 0 = position mode
    # 1 = immediate mode
    # checks the instruction string and if there are not enough modes given
    # fill up with 0's
    parameter_modes = [0, 0, 0]
    for count, char in enumerate(reversed(instruction[:-2])):
        parameter_modes.insert(count, int(char))

    if optcode in [1, 2]:
        param1_value = data[index+1]
        param2_value = data[index+2]

        param1 = data[param1_value] if parameter_modes[0] == 0 else param1_value    
        param2 = data[param2_value] if parameter_modes[1] == 0 else param2_value

        store_pos = data[index+3] 

        if optcode == 1:
            res = param1 + param2
        else:
            res = param1 * param2
        increase = 4
        
        data[store_pos] = res
    
    elif optcode == 3:
        res = 1 # int(input("Number: "))
        store_pos = data[index+1]
        increase = 2
        
        data[store_pos] = res
    
    elif optcode == 4:
        param1_value = data[index+1]
        param1 = data[param1_value] if parameter_modes[0] == 0 else param1_value    

        print("Output:", param1)
        increase = 2

    else:
        print("Unknown Optcode", optcode)

    index += increase

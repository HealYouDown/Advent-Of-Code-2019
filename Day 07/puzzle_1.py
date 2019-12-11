from itertools import permutations
from intcode_computer import IntcodeComputer

with open("Day 7/input.txt", "r") as f:
    codes = [int(i) for i in f.readline().split(",")]

sequences = list(permutations(range(5)))

max_val = 0
max_sequence = None

for sequence in sequences:
    amp_a = IntcodeComputer(codes)
    amp_a.set_inputs(sequence[0], 0)
    amp_a.run()
    
    amp_b = IntcodeComputer(codes)
    amp_b.set_inputs(sequence[1], amp_a.outputs[0])
    amp_b.run()

    amp_c = IntcodeComputer(codes)
    amp_c.set_inputs(sequence[2], amp_b.outputs[0])
    amp_c.run()

    amp_d = IntcodeComputer(codes)
    amp_d.set_inputs(sequence[3], amp_c.outputs[0])
    amp_d.run()
    
    amp_e = IntcodeComputer(codes)
    amp_e.set_inputs(sequence[4], amp_d.outputs[0])
    amp_e.run()

    thrusters_val = amp_e.outputs[0]
    if thrusters_val > max_val:
        max_val = thrusters_val
        max_sequence = sequence

print(max_val)
print(max_sequence)

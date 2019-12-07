import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from itertools import permutations
from intcode_computer import IntcodeComputer

with open("Day 7/input.txt", "r") as f:
    codes = [int(i) for i in f.readline().split(",")]
sequences = list(permutations(range(5, 10)))

"""Example 1
codes = [
    3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
    27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
]
sequences = [[9, 8, 7, 6, 5]]
outputs 129 instead of 139629729
"""

"""Example 2
codes = [
    3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
    -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
    53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10
]
sequences = [[9, 7, 8, 5, 6]]
outputs 48 instead of 18216
"""

max_e = 0

for sequence in sequences:
    amp_a = IntcodeComputer(codes, stop_on_output=True)
    amp_b = IntcodeComputer(codes, stop_on_output=True)
    amp_c = IntcodeComputer(codes, stop_on_output=True)
    amp_d = IntcodeComputer(codes, stop_on_output=True)
    amp_e = IntcodeComputer(codes, stop_on_output=True)
    
    amps = [amp_a, amp_b, amp_c, amp_d, amp_e]
    
    last_output = 0
    loop_count = 0

    while True:
        for index, amp in enumerate(amps):
            
            if loop_count == 0:
                amp.set_inputs(sequence[index], last_output)
            else:
                amp.set_inputs(last_output)

            amp.run()

            last_output = amp.outputs[-1]

        else:
            # check if AMP E reached code 99 
            if amps[-1].exited_normally:
                val = amps[-1].outputs[-1]
                if val > max_e:
                    max_e = val
                break

        loop_count += 1

print(max_e)
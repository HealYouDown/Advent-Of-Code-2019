from intcode_computer import IntcodeComputer
import copy

with open("Day 9/input.txt", "r") as f:
    codes = [int(i) for i in f.readline().split(",")]

comp = IntcodeComputer(optcodes=copy.deepcopy(codes), print_output=True)
comp.set_inputs(2)
comp.run()

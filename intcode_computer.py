import sys

class Parameter:
    def __init__(self, mode: int, index: int, optcodes: list):
        try:
            self.__optcode_value = optcodes[index]
            if mode == 0:
                self.__value = optcodes[self.__optcode_value]
            elif mode == 1:
                self.__value = self.__optcode_value
        except IndexError:
            self.__value = None

    @property
    def val(self) -> int:
        """Returns the value either in position or immediate mode"""
        return self.__value

    @property
    def opt_value(self) -> int:
        """Always returns the position mode value"""
        return self.__optcode_value

    def _get_value_of_obj(self, obj):
        if isinstance(obj, Parameter):
            return obj.val
        else:
            return obj

    def __str__(self) -> str:
        return str(self.val)

    def __int__(self) -> int:
        return int(self.val) 

    def __index__(self):
        return self.val

    def __add__(self, obj):
        return self.val + self._get_value_of_obj(obj)

    def __sub__(self, obj):
        return self.val - self._get_value_of_obj(obj)

    def __mul__(self, obj):
        return self.val * self._get_value_of_obj(obj)

    def __lt__(self, obj):
        return self.val < self._get_value_of_obj(obj)

    def __gt__(self, obj):
        return self.val > self._get_value_of_obj(obj)

    def __eq__(self, obj):
        return self.val == self._get_value_of_obj(obj)

    def __ne__(self, obj):
        return self.val != self._get_value_of_obj(obj)


class IntcodeComputer:
    def __init__(self,
                 optcodes: list,
                 print_output: bool = False,
                 stop_on_output: bool = False
                 ):
        self._print_output = print_output
        self._stop_on_output = stop_on_output
        self._exited_normally = False

        self._optcodes = optcodes
        self._index = 0

        self._input_counter = 0
        self._outputs = []
        self._inputs = []

    @property
    def optcodes(self) -> list:
        return self._optcodes

    @property
    def outputs(self) -> list:
        return self._outputs
    
    @property
    def exited_normally(self) -> bool:
        return self._exited_normally

    def set_inputs(self, *inputs):
        self._inputs = inputs

    def set_input_counter(self, num: int):
        self._input_counter = num

    def run(self):
        self._input_counter = 0
        
        while True:
            instruction = str(self._optcodes[self._index])
            optcode = int(instruction[-2:])
            
            # Create Parameters
            parameter_modes = [0, 0, 0]
            for count, char in enumerate(reversed(instruction[:-2])):
                parameter_modes.insert(count, int(char))

            param1 = Parameter(mode=parameter_modes[0],
                               index=self._index+1,
                               optcodes=self._optcodes)
            param2 = Parameter(mode=parameter_modes[1],
                               index=self._index+2,
                               optcodes=self._optcodes)
            param3 = Parameter(mode=parameter_modes[2],
                               index=self._index+3,
                               optcodes=self._optcodes)

            if optcode == 99:
                self._exited_normally = True
                break

            elif optcode in [1, 2]:
                store_pos = self._optcodes[self._index + 3]

                if optcode == 1:
                    res = param1 + param2
                else:
                    res = param1 * param2
                
                self._index += 4
                self._optcodes[store_pos] = res
            
            elif optcode == 3:
                if self._inputs:
                    res = self._inputs[self._input_counter]
                    self._input_counter += 1
                else:  # ask for a number if there is no list given
                    res = int(input("Number: "))

                store_pos = self._optcodes[self._index+1]

                self._index += 2
                self._optcodes[store_pos] = res

            elif optcode == 4:
                if self._print_output:
                    print("Output:", param1)

                self._outputs.append(int(param1))

                self._index += 2

                if self._stop_on_output:
                    break

            elif optcode in [5, 6]:
                if optcode == 5:
                    if param1 != 0:
                        self._index = param2
                    else:
                        self._index += 3
                
                else:
                    if param1 == 0:
                        self._index = param2
                    else:
                        self._index += 3
                
            elif optcode in [7, 8]:
                if optcode == 7:
                    self._optcodes[param3.opt_value] = 1 if param1 < param2 else 0

                elif optcode == 8:
                    self._optcodes[param3.opt_value] = 1 if param1 == param2 else 0

                self._index += 4

            else:
                print("Unkown Optcode", optcode)
                sys.exit()

with open("Day 8/input.txt", "r") as f:
    data = f.readline()

# Consists of layers which are each 25x6 pixels width/tall. => 100 layers

MAX_WIDTH = 25
MAX_HEIGHT = 6

layers = []

number_of_layers = len(data) // (25*6)
digits_per_layer = len(data) // number_of_layers

for i in range(number_of_layers):
    rows = []
    layer_digits = data[i*digits_per_layer : i*digits_per_layer + digits_per_layer]

    for k in range(MAX_HEIGHT):
        rows.append(layer_digits[k*MAX_WIDTH : k*MAX_WIDTH + MAX_WIDTH])
    
    layers.append(rows)


lowest_number_of_zeros = None
lowest_number_of_zeros_layer_index = None

for index, layer in enumerate(layers):
    number_of_zeros = sum([row.count("0") for row in layer])
    
    if lowest_number_of_zeros is None or number_of_zeros < lowest_number_of_zeros:
        lowest_number_of_zeros = number_of_zeros
        lowest_number_of_zeros_layer_index = index

# Calc 1's * 2's
layer = layers[lowest_number_of_zeros_layer_index]

ones = sum([row.count("1") for row in layer])
twos = sum([row.count("2") for row in layer])
print(ones*twos)

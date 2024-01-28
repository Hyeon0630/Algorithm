power = lambda item: item * item
under_3 = lambda item: item < 3

list_input = [1, 2, 3, 4, 5]

list_output_map = map(power, list_input)
print("map:", list(list_output_map))

list_output_filter = filter(under_3, list_input)
print("filter:",list(list_output_filter))
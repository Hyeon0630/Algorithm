list_input1 = [1, 2, 3, 4, 5]

list_output_map = map(lambda item: item * item, list_input1)
print("map:", list(list_output_map))

list_output_filter = filter(lambda item: item < 3, list_input1)
print("filter:",list(list_output_filter))
def power(item):
    return item * item

def under_3(item):
    return item < 3

list_input = [1, 2, 3, 4, 5]

list_output_map = map(power, list_input)
print("map:", list(list_output_map))

list_output_filter = filter(under_3, list_input)
print("filter:",list(list_output_filter))
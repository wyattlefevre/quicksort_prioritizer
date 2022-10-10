# Python3 implementation of QuickSort copeied from geeksforgeeks
def is_better(item1, item2):
    print("\033[2J")
    print("\033[H")
    print("select the better option")
    better_item = input(f"a: {item1} b: {item2}\n")
    return better_item == "a"


def partition(array, low, high):
    input("new pivot\npress enter to continue\n")
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if not is_better(array[j], pivot):
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

user_input = ""
inputs = []
while True:
    print("\033[2J")
    print("\033[H")
    print(inputs)
    user_input = input("enter an item: ")
    if user_input == "done":
        break
    inputs.append(user_input)

quick_sort(inputs, 0, len(inputs) - 1)
inputs.reverse()
print("\033[2J")
print("\033[H")
print("Results:")
for i, item in enumerate(inputs):
    print(f"{i + 1} {item}")

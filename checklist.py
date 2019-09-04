checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)
checklist[0]
checklist = ['Blue', 'Orange']
checklist[1] = 'Cats'
print(checklist)
checklist = ['Blue', 'Cats']
checklist.pop(1)
print(checklist)

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        destroy(input_item)
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True

    # User Selection Code here

def user_input(prompt):
    user_input = input(prompt)
    return user_input
    # Get user input here


def test():
    create("purple sox")
create("red cloak")

print(read(0))
print(read(1))

update(0, "purple socks")

destroy(1)

print(read(0))
# print(read(1))

list_all_items()

test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list and Q to exit list")
    select(selection)
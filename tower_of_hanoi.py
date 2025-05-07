from stack import Stack

print("\nLet's play Towers of Hanoi!!")

stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

num_disks = int(input("\nHow many disks do you want to play with: ")) 
while num_disks < 3:
  num_disks = int(input("\nEnter a number greater than or equal to 3\n"))
for i in range(num_disks, 0, -1):
  left_stack.push(i)

num_optimal_moves = 2 ** num_disks - 1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")

def get_input():
  choice = ['L','M','R']

  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choice[i]
      print(f"Enter {letter} for {name}")
    user_input = input("")
    if user_input.upper() in choice:
      for i in range(len(stacks)):
        if user_input.upper() == choice[i]:
          return stacks[i]

moves = 0
while right_stack.get_size() != num_disks:
    print("\n\n=====Current Tower Of Hanoi state=====")
    for stack in stacks:
        stack.print_items()
    
    while True:
        print("\nWhich stack do you want to move from?")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?")
        to_stack = get_input()
        if from_stack.is_empty():
            print("\nCannot move from empty stack! Try again.")
        elif not to_stack.is_empty() and from_stack.peek() > to_stack.peek():
            print("\nCannot place larger disk on smaller one! Try again.")
        else:
            disk = from_stack.pop()
            to_stack.push(disk)
            moves += 1
            break

print(f"\n\nCongratulations! You solved the puzzle in {moves} moves.")
print(f"The optimal number of moves is {num_optimal_moves}")
if moves == num_optimal_moves:
    print("Perfect! You achieved the optimal solution!")
else:
    print(f"Try again to solve it in {num_optimal_moves} moves!")


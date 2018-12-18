from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack =Stack("Middle")
right_stack = Stack("Right")
stacks += [left_stack, middle_stack, right_stack]
#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))
for disk in range(num_disks, 0,  -1):
  left_stack.push(disk)
#left_stack.print_items()

num_optimal_moves = (2**num_disks)-1
print("\nThe fastest you can solve this game is in {num} moves".format(num = num_optimal_moves ))

#Get User Input
def get_input():

  choices = [(stack.get_name()[0])for stack in stacks]

  while True:

    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {a} for {b}".format(a = letter, b = name))

    user_input = input("Input: ")

    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]


#Play the Game
num_user_moves = 0

while right_stack.get_size() != num_disks:

  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()

  while True:

    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()

    if from_stack.get_size() == 0:
      print("\n\n Mongeloid Invalid Move. Try Again")

    elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
      print ("Goed bezig henkie")
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1

    else:
      print("\n\n Loser Invalid Move. Try Again")
    break

print("\n\nYou completed the game in {a} moves, and the optimal number of moves is {b}".format(a = num_user_moves, b = num_optimal_moves))




#print(stacks)

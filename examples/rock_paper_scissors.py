import random

#file i/o functions for historical results
def load_results():
    text_file = open("history.txt", "r")
    history = text_file.read().split(",")
    text_file.close()
    return history

def save_results( w, t, l):
    text_file = open("history.txt", "w")
    text_file.write( str(w) + "," + str(t) + "," + str(l))
    text_file.close()


def start_game():
    # print updated stats
    print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
    # prompt user to make another selection
    print("Please choose to continue...")
    # initialize user, computer choices
    global computer
    computer = random.randint(1, 3)
    global user
    user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))


def check_inputs(cmd, cpu_cmd):
    if cmd == cpu_cmd:
        return 0
    elif cmd == 1 and cpu_cmd == 3 \
        or cmd == 2 and cpu_cmd == 1 \
        or cmd == 3 and cpu_cmd == 2:
        return 1
    else:
        return -1


results = load_results()
wins = int(results[0])
ties = int(results[1])
losses = int(results[2])
choices = ['Zero', 'Rock', 'Paper', 'Scissors']

#welcome message
print("Welcome to Rock, Paper, Scissors!")
start_game()


#gamplay loop
while not user == 9:
    if user == 1 or user == 2 or user == 3:
        result = check_inputs(computer, user)
        if result == 0:
            print(f"Computer chose {choices[computer]}...tie!")
        if result == 1:
            print(f"Computer chose {choices[computer]}...computer wins :(")
        if result == -1:
            print(f"Computer chose {choices[computer]}...you wins :)")
    else:
        print("Invalid selection. Please try again.")
    start_game()
# #game over, save results
save_results(wins, ties, losses)
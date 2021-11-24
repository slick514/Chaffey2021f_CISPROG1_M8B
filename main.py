'''
Programmer: Justin Gries
Date: 24 November, 2021
Course: Chaffey College CISPROG-1

Project: Magic 8-ball
Summary:    Replicates a "Magic 8-ball"
            Produces a random "answer" upon <Enter>
            Quits upon <Tab>

Methods, constants, and variables have been named such that this should be reasonably self-documenting
'''

import random
import os
import time
import keyboard
from keyboard import KeyboardEvent

# Human-readable constants
SLEEP_SECONDS = 1.0
ENTER_KEY = 'enter'
QUIT_KEY = 'tab'
NEWLINE_CHAR = os.linesep

# There's got to be a better way than using a global sentinel like this, right??
KEEP_RUNNING = True

MESSAGE_MAP = {
    0: "It is certain",
    1: "Outlook good",
    2: "You may rely on it",
    3: "Ask again later",
    4: "Concentrate and ask again",
    5: "Reply hazy; try again",
    6: "My reply is 'No'",
    7: "My sources say 'No'"
}


def run_8ball():
    setup_keyboard_listeners()
    print_warning()
    print_prompt()
    # Keyboard listeners will handle functionality via callbacks to appropriate functions
    # We'll just check periodically to see if we are done.
    while KEEP_RUNNING:
        time.sleep(SLEEP_SECONDS)
    print(f'{NEWLINE_CHAR}Goodbye')


def print_warning():
    print('A WARNING TO THE INCREDULOUS!!!')
    print('The power of the Magical 8-Ball is vast, but it can\'t understand gibberish!!!')
    print('So like... a djinn may mildly curse you for a few minutes or something if you type nonsense.')
    print(f'No further warnings will be given! Beware!! BEWARE!!!{NEWLINE_CHAR}')

def setup_keyboard_listeners():
    keyboard.on_press_key(QUIT_KEY, quit_program)
    keyboard.on_press_key(ENTER_KEY, display_answer_and_reprompt)


'''
Tried just doing a program exit via sys.exit() and it wouldn't work.
Tried directly raising an exception and catching it
os._exit() worked, but I don't like using functionality that is overtly indicated as private/protected
My IDE hated os._exit(), even though it worked. Problem in the import, from what I read.
Multithreading issue?
'''
def quit_program(event: KeyboardEvent):
    global KEEP_RUNNING  # Global variables are gross. Any tips here?
    KEEP_RUNNING = False


def display_answer_and_reprompt(event: KeyboardEvent):
    answer = random.randint(0, 7)
    print(MESSAGE_MAP.get(answer))
    print_prompt()


def print_prompt():
    print(f"Think, or type a 'yes' or 'no' question to the Magic 8-Ball: (Press <{QUIT_KEY}> to exit)")


if __name__ == '__main__':
    run_8ball()

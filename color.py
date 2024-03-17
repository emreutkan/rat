# ANSI color codes
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'
RESET = '\033[0m'

def black(text): return f"{BLACK}{text}{RESET}"
def red(text): return f"{RED}{text}{RESET}"
def green(text): return f"{GREEN}{text}{RESET}"
def yellow(text): return f"{YELLOW}{text}{RESET}"
def blue(text): return f"{BLUE}{text}{RESET}"
def magenta(text): return f"{MAGENTA}{text}{RESET}"
def cyan(text): return f"{CYAN}{text}{RESET}"
def white(text): return f"{WHITE}{text}{RESET}"
def bright_black(text): return f"{BRIGHT_BLACK}{text}{RESET}"
def bright_red(text): return f"{BRIGHT_RED}{text}{RESET}"
def bright_green(text): return f"{BRIGHT_GREEN}{text}{RESET}"
def bright_yellow(text): return f"{BRIGHT_YELLOW}{text}{RESET}"
def bright_blue(text): return f"{BRIGHT_BLUE}{text}{RESET}"
def bright_magenta(text): return f"{BRIGHT_MAGENTA}{text}{RESET}"
def bright_cyan(text): return f"{BRIGHT_CYAN}{text}{RESET}"
def bright_white(text): return f"{BRIGHT_WHITE}{text}{RESET}"

# Example usage:
def test():
    print(black('This is black text'))
    print(red('This is red text'))
    print(green('This is green text'))
    print(yellow('This is yellow text'))
    print(blue('This is blue text'))
    print(magenta('This is magenta text'))
    print(cyan('This is cyan text'))
    print(white('This is white text'))
    print(bright_black('This is bright black text'))
    print(bright_red('This is bright red text'))
    print(bright_green('This is bright green text'))
    print(bright_yellow('This is bright yellow text'))
    print(bright_blue('This is bright blue text'))
    print(bright_magenta('This is bright magenta text'))
    print(bright_cyan('This is bright cyan text'))
    print(bright_white('This is bright white text'))

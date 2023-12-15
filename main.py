import requests
from colorama import Fore, Back, Style, init
import os
import time

# Enable ANSI escape codes for color formatting in Windows Command Prompt
os.system('color')

def print_rainbow_ascii_art(ascii_art, duration=0.1):
    rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    init(autoreset=True)

    for _ in range(len(ascii_art[0])):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        colored_art_lines = []

        for line in ascii_art.split('\n'):
            colored_line = ''
            for i, char in enumerate(line):
                if char.isspace():
                    colored_line += char
                else:
                    color_index = (i + _) % len(rainbow_colors)
                    colored_line += f'{rainbow_colors[color_index]}{char}{Style.RESET_ALL}'

            colored_art_lines.append(colored_line)

        colored_art = '\n'.join(colored_art_lines)
        print(colored_art)
        time.sleep(duration)

def check_username(username):
    url = f'https://api.mojang.com/users/profiles/minecraft/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        return f'{Fore.RED}[-] {username}{Style.RESET_ALL}'
    elif response.status_code == 404:
        return f'{Fore.GREEN}[+] {username}{Style.RESET_ALL}'
    elif response.status_code == 429:
        return f'{Fore.RED}[-] To Many Requests {Style.RESET_ALL}'
    else:
        return f'{Fore.YELLOW}[?] {username}{Style.RESET_ALL}'

if __name__ == '__main__':
    ascii_art = """
____       _     _          _ 
|  ___|_ _| |__ | | ___  __| |
| |_ / _` | '_ \| |/ _ \/ _` |
|  _| (_| | |_) | |  __/ (_| |
|_|  \__,_|_.__/|_|\___|\__,_|
    """

    num_cycles = 5  # You can adjust the number of rainbow cycles
    for _ in range(num_cycles):
        print_rainbow_ascii_art(ascii_art, duration=0.05)
    
    file_path = 'usernames.txt'
    with open(file_path, 'r') as file:
        usernames_to_check = file.read().splitlines()

    for username in usernames_to_check:
        result = check_username(username)
        print(result)

    con = input("Press enter to continue...")

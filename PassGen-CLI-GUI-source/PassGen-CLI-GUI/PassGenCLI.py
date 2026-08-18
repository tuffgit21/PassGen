import secrets
import time
import os
import argparse
parser = argparse.ArgumentParser(description="PassGen - A simple CLI password generator")
parser.add_argument(
    "--length",
    "-l",
    type=int,
    default=20,
    help="Set the password length (default: 20)"
)
parser.add_argument(
    "--output",
    "-o",
    help="Save generated password to a text file"
)
args = parser.parse_args()
PassGenVers = "v"+"1.8" + "-" + "release" # DO NOT CHANGE THIS UNLESS FIXING A bug or a new update 
def Window():
    print("______________________________________________________________________________________________")
    print("|############################################################################################|")
    print("|#|----------------------------------------------------------------------------------------|#|")
    print("|#|   PPPPPP      AAAA       SSSSSSS      SSSSSSS     GGGGGG      EEEEEEE   NNNN      NN   |#|")
    print("|#|   PP   PP    AA  AA     SS           SS         GG            EE        NN  NN    NN   |#|")
    print("|#|   PPPPPP    AA    AA      SSSS         SSSS     GG     GGGG   EEEEEE    NN   NN   NN   |#|")
    print("|#|   PP       AAAAAAAAAA          SS          SS   GG      GG    EE        NN     NN NN   |#|")
    print("|#|   PP      AA        AA   SSSSSSS     SSSSSSS      GGGGGG      EEEEEEE   NN      NNNN   |#|")
    print(f"|#|    {PassGenVers}                                                                        |#|")
    print("|#|----------------------------------------------------------------------------------------|#|")
    print("|############################################################################################|")
    print("----------------------------------------------------------------------------------------------")
    print("# - - - - - - - - - - - - - - { Made By tuffgit21 on GitHub } - - - - - - - - - - - - - - #")
    print("#{ Official site: https://tuffgit21.github.io/ |#| GitHub repo: https://github.com/tuffgit21/tuffgit21.github.io }#")
Window()

# - - - Prints loading texts - - - #
text = [f"Loading PassGenCLI {PassGenVers}...", "Making sure everything is working...", "Initialization complete."]
for i in text:
    print(i)
    time.sleep(5)
# - - - Variables to randomly generates a password - - - #
Alphabet = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
Symbols = ["!", "@", "#", "$", "&", "*", "_","^","+","."]
UpperCase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# - - - Generates a password if the user wants to - - - #

password_chars = []

# - - - Can be changed (recommended to set it between 20 and 25 is ideal for a strong password) - - - #
if (args.length >= 15 and args.length <= 30): # - - - Checks the variable 'n' if it's greater than the 15 or equal to 15 AND if it's smaller than 30 or equal to 30 - - - #
    print("Generating password...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.abspath(os.path.join(script_dir, args.output)) if args.output else None

    def Password():
        for i in range(args.length):
            time.sleep(0.5)
            password_chars.append(secrets.choice(Alphabet + Numbers + Symbols + UpperCase))
            print(password_chars[-1], end="", flush=True)
            password = "".join(password_chars)
            timestamp = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
        print(f"\nPassword generated at: {timestamp}")
        print(f"Password length: {args.length} digits")
        
        if output_path:
            input("Press Enter to save password...")
            with open(output_path, "a", encoding="utf-8") as file:
                file.write(f"\n{password} - {args.length} digits - Generated at {timestamp} - Version: {PassGenVers}")
            print(f"Password saved to: {output_path}")
            input("Press Enter to exit...")
        else:
            input("Press Enter to exit...")
    Password()
else:
    print("An Error occurred: Choose between 15 and 30 digits.")
    time.sleep(0.5)
    input("Press Enter to exit...")
    exit()

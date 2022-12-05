#!/usr/bin/env python3
import hashlib, argparse
from colorama import init, Fore
init(autoreset=True)
avmethod = ["sha256", "sha512", "md5"]
## Argparse setup ##
parser = argparse.ArgumentParser(
                    prog = 'Hashzam',
                    description = 'Calculates and compares hashes! Available hash methods are' + str(avmethod),
                    epilog = 'SpamixOfficial 2022')
m = parser.add_mutually_exclusive_group()
m.add_argument("-cp", nargs=3, metavar=("| filename |", "original hash |" , "method |"), help="Compare hashes", action="store")
m.add_argument("-ca", nargs=2, metavar=("| filename |", "method |"), help="Calculate hashes", action="store")
args = parser.parse_args()
filename = "None"
method = "None"
mode = None
## Start of script ##
def main():
    global filename, mode, method, ohash
    if args.cp:
        arglist = args.cp 
        filename, ohash, method = arglist[-3], arglist[-2], arglist[-1]
        mode = "compare"
        try:
            with open(filename,"rb") as f:
                f.close()
        except FileNotFoundError:
            print(Fore.RED + "FileNotFoundError: File not found! Are you sure you didn't do a tYpO?\n")
            quit()


        if method not in avmethod:
            print(Fore.RED + "That is not a method! Choose a valid one.\nValid methods:\n" + str(avmethod))
            quit()

    elif args.ca:
        arglist = args.ca 
        filename, method = arglist[-2], arglist[-1]
        mode = "calculate"

        try:
            with open(filename,"rb") as f:
                f.close()
        except FileNotFoundError:
            print(Fore.RED + "FileNotFoundError: File not found! Are you sure you didn't do a tYpO?\n")
            quit()

        if method not in avmethod:
            print(Fore.RED + "That is not a method! Choose a valid one.\nValid methods:\n" + str(avmethod))
            quit()
    else:
        print("Use hashzam -h for help.")
        quit

    if mode == "compare":
        if method == "md5":
            md5_hash = hashlib.md5()

            with open(filename,"rb") as f:
                # Read and update hash in chunks of 4K
                for byte_block in iter(lambda: f.read(4096),b""):
                    md5_hash.update(byte_block)
                    result = str(md5_hash.hexdigest())
                f.close()


            if result == ohash:
                print("The hash of the file and the hash you provided does match!" + Fore.GREEN + " (PASS)")
            elif not result == ohash:
                print("The hash of the file does not match the hash you provided!" + Fore.RED + " (FAIL)")
                print("Hash of the file: " + md5_hash.hexdigest() + "\nHash you provided: " + ohash)    

        elif method == "sha256":
            sha256_hash = hashlib.sha256()

            with open(filename,"rb") as f:
                # Read and update hash in chunks of 4K
                for byte_block in iter(lambda: f.read(4096),b""):
                    sha256_hash.update(byte_block)
                    result = str(sha256_hash.hexdigest())
                f.close()


            if result == ohash:
                print("The hash of the file and the hash you provided does match!" + Fore.GREEN + " (PASS)")
            elif not result == ohash:
                print("The hash of the file does not match the hash you provided!" + Fore.RED + " (FAIL)")
                print("Hash of the file: " + sha256_hash.hexdigest() + "\nHash you provided: " + ohash)

        elif method == "sha512":
            sha512_hash = hashlib.sha512()

            with open(filename,"rb") as f:
                # Read and update hash in chunks of 4K
                for byte_block in iter(lambda: f.read(4096),b""):
                    sha512_hash.update(byte_block)
                    result = str(sha512_hash.hexdigest())
                f.close()


            if result == ohash:
                print("The hash of the file and the hash you provided does match!" + Fore.GREEN + " (PASS)")
            elif not result == ohash:
                print("The hash of the file does not match the hash you provided!" + Fore.RED + " (FAIL)")
                print("Hash of the file: " + sha512_hash.hexdigest() + "\nHash you provided: " + ohash)

    elif mode == "calculate":
        if method == "md5":
            md5_hash = hashlib.md5()

            with open(filename,"rb") as f:
                # Read and update hash in chunks of 4K
                for byte_block in iter(lambda: f.read(4096),b""):
                    md5_hash.update(byte_block)
                    result = str(md5_hash.hexdigest())
                f.close()

            print("Hash of the file: " + Fore.GREEN + md5_hash.hexdigest())   


        elif method == "sha256":
            sha256_hash = hashlib.sha256()

            with open(filename,"rb") as f:
                # Read and update hash in chunks of 4K
                for byte_block in iter(lambda: f.read(4096),b""):
                    sha256_hash.update(byte_block)
                    result = str(sha256_hash.hexdigest())
                f.close()

            print("Hash of the file: " + Fore.GREEN + sha256_hash.hexdigest())



        elif method == "sha512":
            sha512_hash = hashlib.sha512()

            with open(filename,"rb") as f:
                # Read and update hash in chunks of 4K
                for byte_block in iter(lambda: f.read(4096),b""):
                    sha512_hash.update(byte_block)
                    result = str(sha512_hash.hexdigest())
                f.close()

            print("Hash of the file: " + Fore.GREEN + sha512_hash.hexdigest())

if __name__ == "__main__":
    main()
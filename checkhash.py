import hashlib
import os
import argparse

parser = argparse.ArgumentParser(
    prog="Check Hash v0.9.0",
    description="Verifies hash of file with provided hash",
    epilog="Insert text")

parser.add_argument('filepath', help="File to be hashed")
parser.add_argument('hash', help="Hash to verify")

BUFSIZE = 65536

def sha256(filepath: str):
    sha256_object = hashlib.sha256()

    with open(filepath, 'rb') as f:
        while True:
            data = f.read(BUFSIZE)
            if not data:
                break

            sha256_object.update(data)

    return sha256_object.hexdigest()

def sha512(filepath: str):
    sha512_object = hashlib.sha512()

    with open(filepath, 'rb') as f:
        while True:
            data = f.read(BUFSIZE)
            if not data:
                break

            sha512_object.update(data)

    return sha512_object.hexdigest()

def sha1(filepath: str):
    sha1_object = hashlib.sha1()

    with open(filepath, 'rb') as f:
        while True:
            data = f.read(BUFSIZE)
            if not data:
                break

            sha1_object.update(data)
        
    return sha1_object.hexdigest()

def md5(filepath: str):
    md5_object = hashlib.md5()

    with open(filepath, 'rb') as f:
        while True:
            data = f.read(BUFSIZE)
            if not data:
                break

            md5_object.update(data)
    
    return md5_object.hexdigest()

def compare_hashes(calc_hash, given_hash):
    if calc_hash == given_hash:
        print("MATCH")
        print(f"Calculated Hash: \t{calc_hash}\nGiven Hash: \t\t{given_hash}")
    else:
        print("NO MATCH")
        print(f"Calculated Hash: \t{calc_hash}\nGiven Hash: \t\t{given_hash}")

def main():
    args = parser.parse_args()

    filepath = args.filepath
    hash = args.hash
    length = len(hash)

    if os.path.exists(filepath) != True:
        print("Error: File path does not exist")
        exit(1)
    
    if os.path.isfile(filepath) != True:
        print("Error: Path specified is not a file")
        exit(1)

    calculated_hash = ""

    match length:
        case 40:
            calculated_hash = sha1(filepath)
        case 64:
            calculated_hash = sha256(filepath)
        case 128:
            calculated_hash = sha512(filepath)
        case 32:
            calculated_hash = md5(filepath)
        case _:
            print("Input hash not supported")
            exit(1)


    compare_hashes(calculated_hash, hash)


if __name__ == "__main__":
    main()
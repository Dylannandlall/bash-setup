import hashlib
import sys
import os

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

    if len(sys.argv) != 4:
        print(f"Expected 3 input arguments. Got {len(sys.argv)} instead")
        exit(1)
    
    type = sys.argv[1]
    filepath = sys.argv[2]
    hash = sys.argv[3]
    
    calculated_hash = ""

    if os.path.exists(filepath):
        if os.path.isfile(filepath):
            match type:
                case "sha256":
                    calculated_hash = sha256(filepath)
                case "sha512":
                    calculated_hash = sha512(filepath)
                case "sha1":
                    calculated_hash = sha1(filepath)
                case "md5":
                    calculated_hash = md5(filepath)
        else:
            print("Error: Path is not a file")
            exit(1)
    else:
        print("Error: file does not exist")
        exit(1)

    compare_hashes(calculated_hash, hash)


if __name__ == "__main__":
    main()
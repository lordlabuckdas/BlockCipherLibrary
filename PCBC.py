import argparse

def encrypt(filename):
    pass

def decrypt(filename):
    pass

def main():
    ap = argparse.ArgumentParser(description='encrypt or decrypt using ECB')
    ap.add_argument('-f', '--filename', help='filename to encrypt or decrypt')
    ap.add_argument('-o', '--output', help='output filename')
    ap.add_argument('-e', '--encrypt', help='add this flag to encrypt (default)', default=True, action='store_true')
    ap.add_argument('-d', '--decrypt', help='add this flag to decrypt', default=False, action='store_true')
    args = ap.parse_args()

if __name__ == "__main__":
    main()
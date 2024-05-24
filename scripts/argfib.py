import sys
import argparse

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("a", nargs="?")
    parser.add_argument("-n", nargs="?")
    return parser

def fibonacci(n: int):
    a = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        a[i] = a[i-1] + a[i-2]
    return a[-1]

if __name__ == "__main__":
    parser = arg_parser()
    argv = parser.parse_args(sys.argv[1:])
    print(fibonacci(int(argv.n or argv.a)))
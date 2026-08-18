"""Command-line interface for the simple calculator."""

import argparse
import sys
from calculator import add, subtract, multiply, divide, power, mod


def parse_args():
    parser = argparse.ArgumentParser(description="Simple calculator")
    subparsers = parser.add_subparsers(dest="op", required=True)

    def make_subcmd(name, help):
        p = subparsers.add_parser(name, help=help)
        p.add_argument("a", type=float)
        p.add_argument("b", type=float)
        return p

    make_subcmd("add", "Add two numbers")
    make_subcmd("sub", "Subtract two numbers (a - b)")
    make_subcmd("mul", "Multiply two numbers")
    make_subcmd("div", "Divide two numbers (a / b)")
    make_subcmd("pow", "Power a^b")
    make_subcmd("mod", "Modulo a % b")

    return parser.parse_args()


def main():
    args = parse_args()
    a = args.a
    b = args.b

    try:
        if args.op == "add":
            res = add(a, b)
        elif args.op == "sub":
            res = subtract(a, b)
        elif args.op == "mul":
            res = multiply(a, b)
        elif args.op == "div":
            res = divide(a, b)
        elif args.op == "pow":
            res = power(a, b)
        elif args.op == "mod":
            res = mod(a, b)
        else:
            print("Unknown operation", file=sys.stderr)
            sys.exit(2)
    except ZeroDivisionError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Print integer results without decimal when appropriate
    if abs(res - int(res)) < 1e-12:
        print(int(res))
    else:
        print(res)


if __name__ == "__main__":
    main()

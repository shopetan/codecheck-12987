#!/usr/bin/env python
import argparse
from app.main import main

parser = argparse.ArgumentParser(description='Write description here')
parser.add_argument('basic_arguments', nargs='*')

args = parser.parse_args()

main(args.basic_arguments, args)

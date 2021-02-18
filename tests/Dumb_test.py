import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('usr', help='User email address', type=str)
args = parser.parse_args()
user = args.usr

print('wHo ThE bEsT?')
bestusr = 'jp643@sussex.ac.uk'

if not user == bestusr:
    print('hahaha.... no.')
    sys.exit(1)
else:
    print('YeS hE iS!')
import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-a", "--foperand", required=True,
   help="first operand")
ap.add_argument("-b", "--soperand", required=True,
   help="second operand")
args = vars(ap.parse_args())

# Calculate the sum
print("Sum is {}".format(int(args['foperand']) + int(args['soperand'])))

from easynmt import EasyNMT
import sys
import argparse
from pathlib import Path
model = EasyNMT('mbart50_m2m')

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="..."
    )
    parser.add_argument(
        "--input", type=Path, required=True, help="..."
    )
    parser.add_argument(
        "--output", type=Path, required=True, help="..."
    )
   
    args = parser.parse_args()
    return args

if __name__ == "__main__":
	args = parse_arguments()
	
	sys.stdout = open(args.output,"wt")
	with open(args.input, "r") as file:
		file = file.read()
		document = file
		
		print(model.translate(document, source_lang = 'eng', target_lang='pl'))

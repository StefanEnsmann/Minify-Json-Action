import json
import os
import sys

def main(args):
    if len(args) < 1:
        print('No input file was given!')
        sys.exit(1)

    in_path = args[0]
    out_path = args[1] if len(args) > 1 else args[0]

    if not os.path.isfile(in_path):
        print('{:} is not a file!'.format(in_path))
        sys.exit(1)
    
    content = None
    print('Reading file {:}'.format(in_path))
    with open(in_path, 'r', encoding='utf-8') as f_in:
        content = json.load(f_in)

    print('Writing file {:}'.format(out_path))
    with open(out_path, 'w', encoding='utf-8') as f_out:
        json.dump(content, f_out, ensure_ascii=False, check_circular=False, indent=None, separators=(',', ':'))

if __name__ == "__main__":
    main(sys.argv[1:])
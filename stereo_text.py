#!/usr/bin/python
import argparse
import re
import sys

parser = argparse.ArgumentParser(description='generate blocks of text with a hidden 3d'
                                             'message in the form of an autostereogram')
parser.add_argument('-s', dest = 'double_space', action = 'store_true', default = False,
                    help = 'Convert single spaces to double spaces. This can help with'
                    'with formatting.')
parser.add_argument('-p', dest = 'padding', type = int, default = 10, help = 'Number of'
                    'spaces between the end of the longest line on the first panel, and'
                    'beginning of the next panel. Default: 10')
args = parser.parse_args()

def do_3d_text(lines):
    ''' This function takes a multiline document as input, with words wrapped in
    /forward slashes/ and returns a list with the lines formatted normally, and
    a second list with the words in forward slashes offset by one space in order
    to appear on a different plane of text when the 2 lists are arranged side-by-side
    as an autostereogram '''
    
    lines = map(lambda line: line.strip(), lines)
    if args.double_space == True:
        lines = map(lambda line: line.replace(' ', '  '), lines)
    lines_stripped = map(lambda line: line.replace('/',''), lines)
    longest_line = max(lines, key=lambda line: len(line))
    padding = len(longest_line) + args.padding 
    lines_3d = map(lambda line: re.sub(r' ?\/(.*)\/ ?',r'\1  ', line), lines) 

    return padding, zip(lines_stripped, lines_3d)

if __name__ == '__main__':
            padding, lines = do_3d_text(sys.stdin)
            for line, line_3d in lines:
                # Loop over all the lines and print.
                print('{}{}{}'.format(line, ' ' * (padding - len(line)), line_3d))

import random
import re
import string

PADDING = 1
VPADDING = 1
DOUBLE_SPACE = False
PATTERN_LEN = 15
PATTERN_CHARS = string.ascii_uppercase + string.digits


class stereo_panel(object):
    """This is a class for building text-based autostereograms.
       Any text passed in 'lines' surrounded by /forward slashes/ will
       pop out in the foreground. Any text passed in 'lines' surrounded
       by \backslashes\ will pop out in the background."""
    def __init__(self, lines, padding_len=PADDING,
                 vpadding_len=VPADDING, double_space=DOUBLE_SPACE):
        """lines: (multiline string) Text to be used in autostereogram,
           with text in /forward slashes/ placed in the foreground, and
           text in \backslashes\ placed in the background
           padding_len: (int) Number of spaces to place before and after
           the longest line of text
           vpadding_len: (int) Number of blank lines to place above and
           below the block of text"""
        self.lines = []
        for line in lines.split('\n'):
            self.lines.append(line.strip())
        self.padding_len = padding_len
        self.vpadding_len = vpadding_len
        self.double_space = double_space

    def get_lines(self):
        return self.lines.copy()

    def get_longest_line(self):
        """returns length of longest line from self.lines, which is
           needed for calculating padding"""
        longest_line = 0
        for line in self.get_stripped_lines():
            if len(line) > longest_line:
                longest_line = len(line)
        return longest_line

    def get_padding_len(self):
        """returns number of spaces to be placed before and after the
           longest line"""
        return self.padding_len

    def set_padding_len(self, pad_len):
        """pad_len: (int) Number of spaces to be placed before and
           after the longest line"""
        self.padding_len = pad_len

    def get_vpadding_len(self):
        """Returns number of blank lines to be placed before and after
           block of text"""
        return self.vpadding_len

    def set_vpadding_len(self, vpad_len):
        """vpad_len: (int) Number of blank lines to be placed before and
           after block of text"""
        self.vpadding_len = vpad_len

    def get_double_space(self):
        return self.double_space

    def set_double_space(self, double_space):
        self.double_space = double_space

    def get_stripped_lines(self):
        """Returns list of lines with forward slashes, and backslashes
           stripped"""
        stripped_lines = []
        for line in self.get_lines():
            if self.get_double_space():
                line = line.replace(' ', '  ')
            stripped_line = line.replace('/', '')
            stripped_line = stripped_line.replace('\\', '')
            stripped_lines.append(stripped_line)
        return stripped_lines.copy()

    def get_stereo_lines(self):
        """Returns list of lines with words in forward slashes and
           backslashes offset appropriately"""
        stereo_lines = []
        regex_fg = re.compile(r' ?\/(.*)\/ ?')
        regex_bg = re.compile(r' ?\\(.*)\\ ?')
        for line in self.get_lines():
            if self.get_double_space():
                line = line.replace(' ', '  ')
            while re.search(regex_fg, line) is not None:
                line = re.sub(regex_fg, r'\1  ', line)
            while re.search(regex_bg, line) is not None:
                line = re.sub(regex_bg, r'  \1', line)
            stereo_lines.append(line)
        return stereo_lines.copy()

    def get_padded_str(self, line_text, pad_len, longest_line):
        """returns line with padding before and after string.
           line_text: (string) line of text to add padding to
           pad_length: (int) length of padding to be added to longest
           line
           longest_line: (int) length of longest line"""
        line_len = longest_line + (pad_len * 2)
        padding = ' ' * int((line_len - len(line_text)) / 2)
        padded_line = padding + line_text + padding
        if len(padded_line) == line_len:
            return padded_line
        else:
            return padded_line + ' '

    def __str__(self):
        lines = self.get_stripped_lines()
        stereos = self.get_stereo_lines()

        # set beginning of text block
        start_end = '*' * (self.get_longest_line() + 2 +
                           (self.get_padding_len() * 2))
        ret = (start_end * 2)[:-1] + '\n'

        # add vertical padding to top of text block
        for i in range(self.get_vpadding_len()):
            ret += '*' + (' ' * ((self.get_padding_len() * 2) +
                                 self.get_longest_line())) + '*'
            ret += (' ' * ((self.get_padding_len() * 2) +
                           self.get_longest_line())) + '*\n'

        # add text block panels
        for line, stereo in zip(lines, stereos):
            ret += '*' + self.get_padded_str(line,
                                             self.get_padding_len(),
                                             self.get_longest_line()) + '*'
            ret += self.get_padded_str(stereo,
                                       self.get_padding_len(),
                                       self.get_longest_line()) + '*\n'

        # add vertical padding to bottom of text block
        for i in range(self.get_vpadding_len()-1):
            ret += '*' + (' ' * ((self.get_padding_len() * 2) +
                                 self.get_longest_line())) + '*'
            ret += (' ' * ((self.get_padding_len() * 2) +
                           self.get_longest_line())) + '*\n'
        ret += (start_end * 2)[:-1]
        return ret


class stereo_sirt(object):
    """This is a class for building 'single image random text'
       autostereograms. A depth map should be passed consisting of
       equal-length lines of text made up of numbers 0 through 9. The
       output will be an autostereogram with the depth of the 3d effect
       following the depth map, with 0 being the farthest away from the
       view, and 9 being closest."""

    def __init__(self, depth_map, pattern_len=PATTERN_LEN):
        """depth_map: (multiline string of numbers 0 through 9) Depth
           map for 3d effect. All lines should be of equal length, all
           characters should be numbers, and no number should be more or
           less than 1 higher/lower than the number before it.
           pattern_len: (integer) The length of the repeating pattern
           for each line."""
        self.depth_map = []
        lineLen = 0
        for line in depth_map.split('\n'):
            if len(line.strip()) > 0:
                if lineLen == 0:
                    lineLen = len(line.strip())
                elif len(line.strip()) is not lineLen:
                    raise AssertionError('All lines in depth map must be the '
                                         'same length')
                c = 0
                for i in line:
                    if re.search(r'[^0-9]', line[c]) is not None:
                        raise AssertionError('Depth map can only contain '
                                             'numbers')
                    if abs(int(line[c]) - int(line[c-1])) > 1:
                        raise AssertionError('All numbers in depth map must '
                                             'be no more than 1 more or less '
                                             'than the numbers before and '
                                             'after it')
                    c += 1
                self.depth_map.append(line.strip())
        self.pattern_chars = PATTERN_CHARS
        if pattern_len <= len(self.pattern_chars) and pattern_len > 5:
            self.pattern_len = pattern_len
        else:
            raise AssertionError('Pattern length cannot be less than 5, or '
                                 'greater than the number of pattern '
                                 'characters')

    def get_pattern_len(self):
        """Returns integer for length of pattern to generate."""
        return self.pattern_len

    def set_pattern_len(self, pattern_len):
        """Changing the pattern length may make it easier to focus on
           the final image that's generated.
           pattern_len: (integer) Length of pattern to generate"""
        if pattern_len <= len(self.pattern_chars) and pattern_len > 5:
            self.pattern_len = pattern_len
        else:
            raise AssertionError('Pattern length cannot be less than 5, or '
                                 'greater than the number of pattern '
                                 'characters')

    def set_pattern_chars(self, pattern_chars):
        """pattern_chars: (string) characters to choose from when
           generating random pattern."""
        if self.pattern_len <= len(pattern_chars):
            self.pattern_chars = pattern_chars
        else:
            raise AssertionError('The number of pattern characters cannot be '
                                 'less than the pattern length')

    def get_pattern_chars(self):
        """Returns characters to choose from when generating random
           pattern."""
        return self.pattern_chars

    def get_pattern(self):
        """Returns random pattern."""
        pattern_len = self.get_pattern_len()
        chars = self.get_pattern_chars()
        pattern = ''
        for _ in range(pattern_len):
            random_char = random.choice(chars)
            while random_char in pattern:
                random_char = random.choice(chars)
            pattern += random_char
        return pattern

    def get_pattern_char(self, current_pattern):
        """Returns random character that does not exist in the current
           pattern.
           current_pattern: (string) String containing characters that
           should not be returned by this method."""
        chars = self.get_pattern_chars()
        random_char = random.choice(chars)
        while random_char in current_pattern:
            random_char = random.choice(chars)
        return random_char

    def get_depth_map(self):
        """Returns list object with each element being a line of the
           depth map."""
        return self.depth_map.copy()

    def get_depth_map_str(self):
        """Returns multiline string containing the entire depth map."""
        depth_map = self.get_depth_map()
        result = ''
        for line in depth_map:
            result += line + '\n'
        return result

    def __str__(self):
        ret = ''
        depth_map = self.get_depth_map()
        for line in depth_map:
            pattern = self.get_pattern()
            # 'p' tracks where we are in the pattern
            # 'c' tracks where we are in the line
            # 'new_pattern' will hold changes to the pattern
            # 'new_line' will hold the current line that we're building
            p = 0
            c = 0
            new_pattern = ''
            new_line = pattern
            for _ in line[:-1]:
                if p == len(pattern):
                    p = 0
                    pattern = new_pattern
                    new_pattern = ''
                if line[c] < line[c+1]:
                    new_char = ''
                elif line[c] < line[c-1]:
                    new_char = (self.get_pattern_char(pattern + new_pattern) +
                                pattern[p])
                else:
                    new_char = pattern[p]
                new_pattern += new_char
                new_line += new_char
                c += 1
                p += 1
            ret += new_line + '\n'
        return ret

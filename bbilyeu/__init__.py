#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""New Relic Python Coding Challenge."""

import time
import os
import sys
from string import punctuation

# elected for simplistic route for help args argparse seemed like overkill
HELP_ARGS = ['-h', '/h', '-?', '/?', '--h', '--?']


class ThreeWordSequenceSeeker():
    """Search contents for most common three-word sequences."""

    def __init__(self):
        """Initialize variables to respective types."""
        # this can and should be replaced with a standard single-quote
        self.sneaky_quote = '’'
        # punctuation string for sterilization
        self.punctuation_str = punctuation.replace("'", "")
        # don't forget mean ol' fancy quotes
        self.punctuation_str += '“”‘'

        # all untested filepaths strings
        self.possible_files = []
        # all existence-tested filepath strings
        self.valid_files = []
        # store input from stdin
        self.stdin_data = ""
        # most common three-word sequences to return
        # Ending type will be list[tuple(str, int)]
        self.results = []
        # calculate total runtime in seconds for sake of ego
        self.total_runtime = -1

    def run(self, argv=[], print_output=True):
        """Take passed files and return top three most common sequences."""
        start_epoch = time.time()

        # check for files first
        if len(argv) > 1:
            if argv[1] in HELP_ARGS:
                self.print_help_and_exit()
            else:
                self.possible_files = argv[1:]

        # check for stdin next
        if not self.possible_files and not sys.stdin.isatty():
            try:
                self.stdin_data = sys.stdin.readlines()
            except:
                pass

        # abort if neither exist
        if len(self.possible_files) == 0 and self.stdin_data == "":
            print("ERROR: No filenames passed to parse.")
            self.print_help_and_exit(rc=1)

        if len(self.possible_files) > 0:
            # list of existing files (if applicable)
            self.find_valid_files()
            # seek out results in files
            self.find_common_sequences_in_files()
        elif self.stdin_data != "":
            # seek out results in stdin
            self.find_common_sequences_in_stdin()

        # if nothing returned, inform user and exit with non-zero return code
        if len(self.results) == 0:
            print("ERROR: No results were returned")
            sys.exit(1)

        # optionally run to allow for testing
        if print_output:
            self.print_results()

        # get total runtime
        self.total_runtime = time.time() - start_epoch

    def find_valid_files(self):
        """Test and notate valid files from passed list."""
        for f in self.possible_files:
            full_path = os.path.realpath(f)
            if os.path.exists(full_path) and os.path.isfile(full_path):
                self.valid_files.append(full_path)

        # invalid or typo'ed file(s) passed, abort
        if len(self.valid_files) == 0:
            print("ERROR: No valid files passed.\n")
            self.print_help_and_exit(rc=1)

    def find_common_sequences_in_stdin(self):
        """Return up to 100 most common three word sequences in stdin."""
        tmp_dict = {}

        # using this as a lazy circular buffer
        mini_buffer = []

        # iterate over each line for memory efficiency
        for line in self.stdin_data:

            # sterilize and explode line into list
            line_as_list = self.sterilize_line(line)

            # iterate over the newly created list
            for word in line_as_list:

                # add current word to our buffer
                mini_buffer.append(word)

                # assuming we have 3+ words, track occurrence count
                if(len(mini_buffer)) > 3:

                    # drop the front entry (bringing size back to 3)
                    mini_buffer.pop(0)

                    # create our key from the assembled string of words
                    seq_str = '{} {} {}'.format(
                        mini_buffer[0],
                        mini_buffer[1],
                        mini_buffer[2]
                    )

                    if seq_str in tmp_dict:
                        # if this is not new, increment counter
                        tmp_dict[seq_str] += 1
                    else:
                        # else, create the entry and set counter
                        tmp_dict[seq_str] = 1

        # sort the temporary dict for a list with the most common sequences
        # sorted with highest count at the beginning
        results = sorted(tmp_dict.items(), key=lambda k: k[1], reverse=True)

        # cap the returned results at 100 (if more than 100 entries)
        list_max_value = len(results) if len(results) < 100 else 100

        # store up to 100 sequences
        self.results = results[0:list_max_value]

    def find_common_sequences_in_files(self):
        """Return up to 100 most common three word sequences in files."""
        tmp_dict = {}

        # iterate over each valid file
        for file in self.valid_files:

            # open the file
            with open(file, 'r') as file_handle:

                # using this as a lazy circular buffer
                mini_buffer = []

                # iterate over each line for memory efficiency
                for line in file_handle:

                    # sterilize and explode line into list
                    line_as_list = self.sterilize_line(line)

                    # iterate over the newly created list
                    for word in line_as_list:

                        # add current word to our buffer
                        mini_buffer.append(word)

                        # assuming we have 3+ words, track occurrence count
                        if(len(mini_buffer)) > 3:

                            # drop the front entry (bringing size back to 3)
                            mini_buffer.pop(0)

                            # create our key from the assembled string of words
                            seq_str = '{} {} {}'.format(
                                mini_buffer[0],
                                mini_buffer[1],
                                mini_buffer[2]
                            )

                            if seq_str in tmp_dict:
                                # if this is not new, increment counter
                                tmp_dict[seq_str] += 1
                            else:
                                # else, create the entry and set counter
                                tmp_dict[seq_str] = 1

        # sort the temporary dict for a list with the most common sequences
        # sorted with highest count at the beginning
        results = sorted(tmp_dict.items(), key=lambda k: k[1], reverse=True)

        # cap the returned results at 100 (if more than 100 entries)
        list_max_value = len(results) if len(results) < 100 else 100

        # store up to 100 sequences
        self.results = results[0:list_max_value]

    def sterilize_line(self, dirty_line):
        """Sterilize passed line and explode into list.

        :param dirty_line: line to sterilize
        :type dirty_line: str
        :returns: sterilized string as list
        :rtype: list[str]
        """
        # NOTE: The 1-2 action per line below is intentional.
        #    There are less verbose ways to do this, but the task
        # list suggested extremely easy-to-read code.

        # enforce string type, force lowercase
        cleaner_line = str(dirty_line).lower()

        # replace fancy single-quotes with normal single-quotes
        cleaner_line = cleaner_line.replace(self.sneaky_quote, "'")

        # remove surrounding whitespace/newlines
        cleaner_line = cleaner_line.strip()

        # remove all remaining punctuation (ignoring contractions)
        cleaner_line = cleaner_line.translate(
            str.maketrans("", "", self.punctuation_str)
        )

        # return cleaned-up line as a list
        return cleaner_line.split()

    def print_help_and_exit(self, rc=0):
        """Inform the user of proper usage and exit.

        Please note that the decision to omit instructions
        for using stdin was an *intentional* one.

        More verbose instructions are less likely to be read

        :param rc: return code for sys.exit()
        :type rc: int
        """
        print("\nUsage: python myscript.py file.txt [file2.txt, ...]\n")
        sys.exit(rc)

    def print_results(self):
        """Print the results to screen."""
        # from: "('the white whale', 71)"
        #   to: "the white whale - 71"
        for s in self.results:
            print('{} - {}'.format(s[0], s[1]))

    def print_ego_trip(self):
        """Print the recorded runtime for giggles."""
        runtime_output = ""
        if self.total_runtime < 1.0:
            runtime_in_ms = int(self.total_runtime * 1000)
            runtime_output = "{} milliseconds".format(runtime_in_ms)
        else:
            runtime_output = "{} seconds".format(self.total_runtime)

        # final output
        print("\nTotal Runtime: {}\n".format(runtime_output))

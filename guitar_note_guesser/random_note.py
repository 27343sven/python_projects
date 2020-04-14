#!/bin/env python3

from random import randint
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--flats", help="Only show flat notes", action="store_true")
parser.add_argument("-s", "--sharps", help="Only show sharp notes", action="store_true")
parser.add_argument("-a", "--all", help="Show the note on all the strings", action="store_true")

ARGS = parser.parse_args()



notes = [
    ["A"],
    ["A#", "Bb"],
    ["B"],
    ["C"],
    ["C#", "Db"],
    ["D"],
    ["D#", "Eb"],
    ["E"],
    ["F"],
    ["F#", "Gb"],
    ["G"],
    ["G#", "Ab"]
]

strings = ["E", "A", "D", "G", "B", "e"][::-1]
denotions = [1, 3, 5, 7, 9, 12, 15, 17, 19, 21]
guitar_length = 12

def print_guitar(string, note):
    guitar = [["{:>2}x".format(_string) if string.upper() == note and _string == string else "{:>2}|".format(_string)] + ["-"] * guitar_length for _string in strings]
    fret_numbers = [" "] + ["{:>2}".format(fret) if fret in denotions else "  " for fret in range(1 + min(max(denotions), guitar_length))]
    for string in strings if ARGS.all else [string]: 
        start_index = [i for i in range(len(notes)) if string.capitalize() in notes[i]][0]
        for fret in range(1, 1 + guitar_length):
            if note in notes[(start_index + fret) % len(notes)]:
                guitar[strings.index(string)][fret] = "x"
    print("".join(fret_numbers))
    print("\n".join([" ".join(string) for string in guitar]))
    print("".join(fret_numbers))


def main():
    if ARGS.sharps and ARGS.flats:
        raise Exception("Cannot exclude both sharps and flats")
    while True:
        os.system("clear")
        selected_note = notes[randint(0, len(notes)-1)]
        if ARGS.sharps:
            note = selected_note[0]
        elif ARGS.flats:
            note = selected_note[0] if len(selected_note) == 1 else selected_note[1]
        else:
            note = selected_note[randint(0, len(selected_note)-1)]
        string = strings[randint(0, len(strings) - 1)]
        print("Find the '{}' on the '{}' string.".format(note, string))
        if input() == "q":
            exit(0)
        print("Answer:")
        print_guitar(string, note)
        if input() == "q":
            exit(0)



if __name__ == "__main__":
    main()

import argparse
import math

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fasta_file")
    args = parser.parse_args()

    id_sequence_dict = parse_fasta_file(args.fasta_file)
    id, gc_content = get_highest_gc_content(id_sequence_dict)
    print(id)
    print(gc_content)


def parse_fasta_file(fasta_file):

    id_sequence_dict = {}

    with open(fasta_file, "r") as fasta:
        id = ""
        sequence = ""

        for line in fasta:
            if line[0] == ">":
                if sequence:
                    id_sequence_dict[id] = sequence

                id = line[1:].strip()
                sequence = ""

            else:
                sequence += line.strip()

        id_sequence_dict[id] = sequence

    return id_sequence_dict


def get_highest_gc_content(id_sequence_dict: dict):
    gc_content_dict = {}

    # calculate all gc-contents
    for id, sequence in id_sequence_dict.items():
        gc_content = calculate_gc_content(sequence)
        gc_content_dict[gc_content] = id

    # find the highest gc-content sequence
    max_gc_content = max(gc_content_dict.keys())

    return gc_content_dict[max_gc_content], max_gc_content


def calculate_gc_content(sequence: str):
    # upper case for standardization
    sequence = sequence.upper()

    # count C and G apparances
    c_count = sequence.count("C")
    g_count = sequence.count("G")

    # calculate GC-content
    gc_content = ((c_count + g_count) * 100) / len(sequence)

    return gc_content


if __name__ == "__main__":
    main()

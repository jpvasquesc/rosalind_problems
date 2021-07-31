import argparse
import math

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fasta_file")
    args = parser.parse_args()

    id, gc_content = get_highest_gc_content(args.fasta_file)
    print(id)
    print(gc_content)


def get_highest_gc_content(fasta_file):
    gc_content_dict = {}

    # parse the FASTA file
    with open(fasta_file, "r") as fasta:
        sequence = ""

        for line in fasta:

            # Save id
            if line[0] == ">":
                if sequence:
                    gc_content = calculate_gc_content(sequence)
                    gc_content_dict[gc_content] = id
                    print(gc_content)

                id = line[1:].strip()
                sequence = ""

            # Calculate gc-content, save in dict
            else:
                sequence += line.strip()

        gc_content = calculate_gc_content(sequence)
        gc_content_dict[gc_content] = id
        print(gc_content)

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

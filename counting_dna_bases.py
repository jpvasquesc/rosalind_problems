# Program to count how many appearances of an base there are in an DNA sequence
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sequence")
    args = parser.parse_args()

    print(count_nucleotides_in_sequence(args.sequence.upper()))
    print(single_iteration(args.sequence.upper()))


def count_nucleotides_in_sequence(dna_sequence: str) -> tuple:
    a_count = dna_sequence.count("A")
    c_count = dna_sequence.count("C")
    g_count = dna_sequence.count("G")
    t_count = dna_sequence.count("T")

    return a_count, c_count, g_count, t_count


def single_iteration(dna_sequence: str) -> tuple:
    # list with the possible bases for a DNA sequence
    possible_bases = ["A", "C", "G", "T"]
    # dictionarie with the total number of appearences of each base
    total = {}

    for base in dna_sequence:
        # If it's a valid base value
        if base in possible_bases:
            if base not in total:
                total[base] = 1
            else:
                total[base] = total[base] + 1

        # If it's not a valide base value
        else:
            print("Not a DNA base")
            break

    return total["A"], total["C"], total["G"], total["T"]


if __name__ == "__main__":
    main()

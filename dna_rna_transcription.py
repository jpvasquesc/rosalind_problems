# Program to find the RNA trancription of an DNA sequence
import argparse


def main():
    # Get sequence from input
    parser = argparse.ArgumentParser()
    parser.add_argument("sequence")
    args = parser.parse_args()

    dna_sequence = args.sequence.upper()
    dna_nucleotides = set(["A", "T", "C", "G"])

    # Check if the given sequence is valid
    if set(dna_sequence) != dna_nucleotides:
        print("Not a DNA sequence!")

    else:
        # Replace T with U
        rna_seq = args.sequence.replace("T", "U")
        print(f"RNA Sequence: {rna_seq}")

if __name__ == "__main__":
    main()

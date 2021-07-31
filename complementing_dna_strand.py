# Creating the complementari DNA strand
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sequence")
    args = parser.parse_args()

    complement_sequence = get_complement_sequence(args.sequence.upper())

    print(f"Complementing DNA sequence: {complement_sequence}")


def get_complement_sequence(dna_sequence: str) -> str:
    # Replace each nucleotide with it's compliment in lowecase
    complement_sequence = dna_sequence.replace('A', 't')
    complement_sequence = complement_sequence.replace('T', 'a')
    complement_sequence = complement_sequence.replace('C', 'g')
    complement_sequence = complement_sequence.replace('G', 'c')

    # Reverse the sequence and turn back to upper case
    complement_sequence = complement_sequence[::-1].upper()

    return complement_sequence


if __name__ == "__main__":
    main()

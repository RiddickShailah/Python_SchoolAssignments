#"""
#Program Description: This program takes a given DNA sequence translates it to a protein sequence.

##Author:
#"""

import helper

def transcription(dna_sequence):
    # Step 1: Replace Thymine (T) with Uracil (U)
    dna_sequence = dna_sequence.replace('T', 'U')

    # Step 2: Create the base pair complement
    complement = ''
    for nucleotide in dna_sequence:
        if nucleotide == 'A':
            complement += 'U'
        elif nucleotide == 'U':
            complement += 'A'
        elif nucleotide == 'C':
            complement += 'G'
        elif nucleotide == 'G':
            complement += 'C'
    return complement


def translate(mrna):
    protein = ''
    triplets_list = helper.chunk(mrna,3)
    print(triplets_list)
    for triplet in triplets_list:
        protein_list = helper.chunk(mrna,3)
        protein = protein_list
    return protein

dna_sequence = "ATGCGTTA"
print(dna_sequence)

mrna = transcription(dna_sequence)
print(mrna)

protein = translate(mrna)
print(protein)
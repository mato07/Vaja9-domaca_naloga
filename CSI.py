# -*- coding: utf-8 -*-

criminal_DNA = """ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGG
CCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCA
TAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTC
CTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"""

# Hair color DNA
black_hair = "CCAGCAATCGC"
brown_hair = "GCCAGTGCCG"
blond_hair = "TTAGCTATCGC"

# Facial shape DNA
square_face = "GCCACGG"
round_face = "ACCACAA"
oval_face = "AGGCCTCA"

# Eye color DNA
blue_eyes = "TTGTGGTGGC"
green_eyes = "GGGAGGTGGC"
brown_eyes = "AAGTAGTGAC"

# Gender DNA
female = "TGAAGGACCTTC"
male = "TGCAGGAACTTC"

# Race DNA
white_race = "AAAACCTCA"
black_race = "CGACTACAG"
asian_race = "CGCGGGCCG"

'''Suspects:

EVA:
Gender: Female
Race: White
Hair color: Blonde
Eye color: Blue
Face shape: Oval

LARISA:
Gender: Female
Race: White
Hair color: Brown
Eye color: Brown
Face shape: Oval

MATEJ:
Gender: Male
Race: White
Hair color: Black
Eye color: Blue
Face shape: Oval

MIHA:
Gender: Male
Race: White
Hair color: Brown
Eye color: Green
Face shape: Square'''

print

if white_race in criminal_DNA:
    if square_face in criminal_DNA:
        print "The ice-cream eater is no one other than Miha. There will be no ice-cream for you in Dob prison because Bavcar ate it all."
    else:
        if male in criminal_DNA:
            print "The ice-cream eater is no one other than Matej. Enjoy the rest of your days in Dob prison playing basketball with Bavcar."
        else:
            if blond_hair in criminal_DNA:
                print "The ice-cream eater is no one other than Eva. You get an exclusive free prison tour with Hilda."
            else:
                print "The ice-cream eater is no one other than Matej. Congratulations! You are Hilda's new prison roommate."
else:
    print "It was an outside job! The criminal was either Jackie Chan or Denzel Washington!"

print
# Confirmation that Miha was the one behind this hideous crime against humanity.

if brown_hair in criminal_DNA and green_eyes in criminal_DNA and male in criminal_DNA:
    print "The second test also confirm that the man we are looking for is Miha. Lock him up boys."
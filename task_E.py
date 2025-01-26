# DA-108 : Python Programming - Task E
# Consider a fragment of the DNA sequence Assign it to a variable and Reverse each 8 length sequence (excluding space) & Countnumber of times- “TTACT” has occurred

import shutil

terminal_width = shutil.get_terminal_size().columns #linebreak based on terminal width
linebreak = ("━" * terminal_width) # Special Character (Box Drawings Heavy Horizontal - Unicode code point - U+2501)

title = "Task_E - Reverse DNA and Count TTACT"
padding = (terminal_width - len(title)) // 2 # Calculate padding for centering
centered_title = " " * max(0, padding) + title
print(linebreak)
print(centered_title)
print(linebreak)

# Define the DNA sequence
DNA_sequence = "ATGTACTC ATTCGTTTCG GAAGAGACAG GTACGTTAAT AGTTAATAGC GTACTTCTTT TTCTTGCTTT CGTGGTATTC TTGCTAGTTA CACTAGCCAT CCTTACTGCG CTTCGATTGT GTGCGTACTG CTGCAATATT GTTAACGTGA GTCTTGTAAA ACCTTCTTTT TACGTTTACT CTCGTGTTAA AAATCTGAAT TCTTCTAGAG TTCCTGATCT TCTGGTCTAA"

# Remove Spaces from DNA sequence
DNA_without_spaces = DNA_sequence.replace(" ", "")

# Define chunk sizes
first_part_size = 8
remaining_part_size = 10

# Create empty list to contain the reversed DNA sequence
reverse_sequence_list = []

# Handle the first 8 characters (reverse it)
first_part = DNA_without_spaces[:first_part_size]
reverse_sequence_list.append(first_part[::-1])

# Handle the remaining characters in chunks of 10 (reverse each chunk)
for i in range(first_part_size, len(DNA_without_spaces), remaining_part_size):
    part = DNA_without_spaces[i:i + remaining_part_size]  # Get the part of 10 characters
    reverse_sequence_list.append(part[::-1])  # Reverse the part and add it to the list

# Join the reversed sequence with spaces in between and print
reverse_sequence = " ".join(reverse_sequence_list)

count_original = DNA_sequence.replace(" ", "").count("TTACT") # "TTACT" in original DNA sequence
count_reversed = reverse_sequence.replace(" ", "").count("TTACT") # "TTACT" in reversed DNA sequence

# Output the sequences
print("Original DNA Sequence:")
print(DNA_sequence)
print(linebreak)
print("Reversed DNA Sequence:")
print(reverse_sequence)
print(linebreak)
print("'TTACT' in original DNA sequence : ", count_original)
print(linebreak)
print("'TTACT' in original DNA sequence : ", count_reversed)
print(linebreak)
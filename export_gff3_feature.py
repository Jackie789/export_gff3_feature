#!/usr/bin/env python3
import sys
import re

#Open and read the gff3 file
this_program_is_cray = re.search(r"--source_gff=/(.*)", sys.argv[1])
gff3_opening = open(this_program_is_cray.group(1))
gff3_contents =  gff3_opening.read()

#Create variables from sys.argv input
raw_type = re.search(r"--type=(.*)", sys.argv[2])
raw_attribute = re.search(r"--attribute=(.*)", sys.argv[3])
raw_value = re.search(r"--value=(.*)", sys.argv[4])

#Separates out strings from input
type = raw_type.group(1)
attribute = raw_attribute.group(1)
value = raw_value.group(1)
key_value_pair = attribute + "=" + value

# Split the gff3 file by newline
line_list = gff3_contents.split("\n")
#Both of the following are lists of lists.
formatted_list = []
searchable_list = []

#Splits the file by occurrence of 2 or more spaces
for number in range(len(line_list)):
		formatted_list.append(1)
		formatted_list[number] = re.split(r"  +", line_list[number])
		#formatted_list[number] = line_list[number].split("    ")
		
#		print(len(formatted_list[number]))
		#print((formatted_list[number]))
#The variable searchable_list will contain only gff3-formatted lines with 9 columns. 
#It is a list of lists
		if len(formatted_list[number]) == 9: 
			searchable_list.append(formatted_list[number])
#print(searchable_list[0])
match = []
for num in range(len(searchable_list)):
#	print("num=" + str(num) + ", coordinate is:" + searchable_list[num][2])
	if type == searchable_list[num][2]:
		if searchable_list[num][8].find(key_value_pair) > -1:	
			match.append(num)
			
#			print("Boo-yah!!!" + str(searchable_list[num]))
if len(match) == 0:
	print("Sorry, no matches were found.")
if len(match) > 1: 
	print("Warning: multiple matches found. Showing the first match only.")	
	
#print(str(match))

print(">" + type + ":" + attribute + ":" + value)
match_start = searchable_list[match[0]][3]
match_end = searchable_list[match[0]][4]

chromosome = ">" + searchable_list[match[0]][0]
#print(match_start + "," + match_end + "," + chromosome)

sequence = gff3_contents.find(chromosome)
print(gff3_contents[sequence:(sequence+len(chromosome))])

print(gff3_contents[(sequence + len(chromosome) + int(match_start)):(sequence+len(chromosome) + int(match_end))])

# Example input and output
$ python export_gff3_feature.py --source_gff=/home/jzuker1/final/Saccharomyces_cerevisiae_S288C.annotation.gff --type=gene --attribute=ID --value=YAL068W
>gene:ID:YAL068W
>chrI
CACTCACATCATTATGCACGGCACTTGCCTCAGCGG
TCTATACCCTGTGCCATTTACCCATAACGCCCATCATTATCCACATTTTGATATCTATATCTCATTCGGCGGTCCCAAAT
ATTGTATAACTGCCCTTAATACATACGTTATACCACTTTTGCACCATATACTTACCACTCCATTTATATACACTTATGTC
AATATTACAGAAAAATCCCCACAAAAATCACCTAAACATAAAAATATTCTAC


$ python export_gff3_feature.py --source_gff=/home/jzuker1/final/Saccharomyces_cerevisiae_S288C.annotation.gff --type=gene --attribute=ID --value=YAL063C-A
>gene:ID:YAL063C-A
>chrI
TAGGTCGAAAATTTAAGGCCACATAAATCCAGAGCCCGCAACTTGGATAGGTATTTACTTGATTTTTAGTTTG
CTTTCAATAGTGTCGTGAAATTATAAAGTACGCCGCATATATATCTTGATTAGTTAAAAATAGCAGTGTTCAATGATGAT
TTGATAGGGTTCATAACTGGTACCAGCGTAGTACAATTACGATTATCCATGAACATAAAAGTGGTTTAAGTACTATATAT
CAGTGAAGCTTCAAAGTAAGCAAACGAGATACCAAGATCTTGTAGGACCAC

$ python export_gff3_feature.py --source_gff=/home/jzuker1/final/Saccharomyces_cerevisiae_S288C.annotation.gff --type=gene --attribute=ID --value=YAL065C
>gene:ID:YAL065C
>chrI
GCCATTAACTAACAAGAGAATTAATAATGTTAAAACACAGATACCTCGAAACAAACTCTATGTAAACACTTATTTTATT
GTGGTAATATTTTTTGATAACAACACATCTGAAACAAAATAATGCAAAGCCGAATAGTTAGGCTAAAAATGTACTCTTAG
ACATTTAAAAAGGTTTATGAATCCTATGGTATTTAATATATTAAAGAACGAAGTAAATGGGAAAAAATGTGTAAACACTA
TAAGCGTGATGATAGAATTATTAATATAAGATGATGCCGTGCGTTTACCATACGATTGCCAGCAATACGGTGGAAATAAA
AACACTTATGCCATTATTGGTCAACAGACCATTGGCAATACCAACGTAGGTTGAGATTT

$ python export_gff3_feature.py --source_gff=/home/jzuker1/final/Saccharomyces_cerevisiae_S288C.annotation.gff --type=ARS --attribute=ID --value=ARS102FS
Sorry, no matches were found.
>ARS:ID:ARS102FS

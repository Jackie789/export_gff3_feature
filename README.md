# export_gff3_feature
This python script parses features within .gff and .gff3 annotation files and prints the feature type and sequence.  

Use the following parameters to use this program. 

**--source_gff** Enter the filepath of the file. 

**--type** Enter the type of attribute

**--attribute** Provide the type of the value. 

**--value** Provide the gene value or other feature to return. 

### Example input and output
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

### An example where the feature does not exist within the file
$ python export_gff3_feature.py --source_gff=/home/jzuker1/final/Saccharomyces_cerevisiae_S288C.annotation.gff --type=ARS --attribute=ID --value=ARS102FS
>Sorry, no matches were found.
>ARS:ID:ARS102FS

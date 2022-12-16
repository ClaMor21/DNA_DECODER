#! /usr/bin/ Python

import subprocess
import os
import shutil



print("[+]" + "UNZIPPING IMAGE")
subprocess.call(["unzip" , "<file_name>"])

print("[+]" + "MAKING NEW DIRECTORY")
newpath = r'/home/kali/Desktop/DNA'
if not os.path.exists(newpath):
	os.makedirs(newpath)

print ("[+]" + "MOVING FILE INTO THE DIRECOTRY" )
shutil.move('dna_E.txt' , '/home/kali/Desktop/DNA/dna_E.txt')


map = {

	'AAA': 'a',

	'AAC': 'b',

	'AAG': 'c',

	'AAT': 'd',

	'ACA': 'e',

	'ACC': 'f',

	'ACG': 'g',

	'ACT': 'h',

	'AGA': 'i',

	'AGC': 'j',

	'AGG': 'k',

	'AGT': 'l',

	'ATA': 'm',

	'ATC': 'n',

	'ATG': 'o',

	'ATT': 'p',

	'CAA': 'q',

	'CAC': 'r',

	'CAG': 's',

	'CAT': 't',

	'CCA': 'u',

	'CCC': 'v',

	'CCG': 'w',

	'CCT': 'x',

	'CGA': 'y',

	'CGC': 'z',

	'CGG': 'A',

	'CGT': 'B',

	'CTA': 'C',

	'CTC': 'D',

	'CTG': 'E',

	'CTT': 'F',

	'GAA': 'G',

	'GAC': 'H',

	'GAC': 'I',

	'GAG': 'J',

	'GAT': 'K',

	'GCC': 'L',

	'GCG': 'M',

	'GCT': 'N',

	'GGA': 'O',

	'GGC': 'P',

	'GGG': 'Q',

	'GGT': 'R',

	'GTA': 'S',

	'GTC': 'T',

	'GTG': 'U',

	'GTT': 'V',

	'TTA': 'W',

	'TAC': 'X',

	'TAG': 'Y',

	'TAT': 'Z',

	'TCA': '1',

	'TCC': '2',

	'TCG': '3',

	'TCT': '4',

	'TGA': '5',

	'TGC': '6',

	'TGG': '7',

	'TGT': '8',

	'TTA': '9',

	'TTC': '0',

	'TTG': ' ',

	'TTT': '.',

}



file = open('/home/kali/Desktop/DNA/dna_E.txt').read().strip()



#to print file with decode text



decoded_text= []

for x in range(0,len(file), 3):

	piece = file[x:x+3]

	decoded_text.append(map[piece])

print ("[+]" "IMAGE UNZIPPED")
print ("[+]" "==========DNA CODE DECODED==========")
print (''.join(decoded_text))
print ("[+]""==========DECODED COMPLETED==========")

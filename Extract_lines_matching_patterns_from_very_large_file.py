#Matches the words in keep_file with input_file, then outputs the lines containing the words in keep_file to output_file
#Similar to UNIX command (but for both keep_file and input_file are large): grep -f keep_file input_file > output_file
#module load python/3.5
import os
import gzip
import sys
WorkingDirectory = '~/current_working_directory/' #Edit Working Directory
files_to_query=["a","b","c"] #files to be looped over

keep_file = open(WorkingDirectory + 'keep_file.txt', 'r') #Your file which contains patterns/words to be kept (one word per line)
lines=keep_file.readlines()
#print("read input files")

To_keep=[] #a list: e.g. ["a", "b", "c"]
for x in lines:
	To_keep.append(str(x.split('\t')[0])+'_'+str(x.split('\t')[1])) #appends chr and pos to 'To_keep' list

for i in chromosomes_to_query:
	output_file = open(WorkingDirectory + i+".txt", "w") #Edit name of output file (use 'files_to_query' list above)
	input_file = gzip.open('input_file.txt','rt') #Your very large data file (should be tab delimited - but change "\t" on line 16 to preferred delimiter if not tab delimited)
	lines_input=input_file.readlines()
	for line in lines_input:
	#for line in test:
		if not line.startswith("#"): #You can start from lines that do not start with "#"
			line=line.strip().split("\t")
			line_chr_pos=str(str(line[0])+'_'+str(line[1]))
			#print(line_chr_pos)
			if line_chr_pos in To_keep: #If the words you're interested in is in the queried line, then output general info from that line - separated by tabs
				chrom=line[0]
				pos=line[1]
				rsid=line[2]
				ref=line[3]
				alt=line[4]
				infor=line[7]
				infor=infor.split(";")
				af=infor[2]
				output_file.write(str(rsid)+"\t"+str(chrom)+"\t"+str(pos)+"\t"+str(ref)+"\t"+str(alt)+"\t"+str(af) + "\n")
	output_file.close()
				
#Testing with smaller dataset
# with gzip.open('/rds/project/rjh234/rds-rjh234-cc-mrc-epid/Reference_Data/gnomAD/r3.0/gnomad.genomes.r3.0.sites.chr19.vcf.bgz','rt') as myfile:
	# test = [next(myfile) for x in range(5000000)]
# #print(test)
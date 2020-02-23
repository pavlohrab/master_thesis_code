import os
import re
from Bio import SeqIO

path = os.path.dirname(os.path.realpath(__file__)) + "/genomes/"
print("The path of working script is:", path)
entries = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) and re.search(r'.txt*', os.path.splitext(f)[1])]
print("I found such files in genomes directory:", ', '.join(entries))
faa_path = path + "faa/"
os.mkdir(faa_path)
for i in entries:
    new_path = path+i
    filename, file_extension = os.path.splitext(i)
    #print(filename)
    fl = open(new_path,'r')
    record = SeqIO.read(fl, 'fasta')

    organism = record.id
    print(organism)

    new_path1 = path + organism
    os.rename(new_path, new_path1+".faa")
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            #print(name)
            #print(i)
            #print(file_extension)
            if (name == filename +"."+ name.rsplit('.')[-1]) and ("."+name.rsplit('.')[-1] != file_extension):
                os.rename(path+"/"+name, faa_path +organism.replace(' ', '_') + ".faa")
                break
        else:
            continue
        break
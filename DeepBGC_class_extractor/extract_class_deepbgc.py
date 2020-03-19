import os
import re
from Bio import SeqIO
from itertools import chain
import operator

path = os.path.dirname(os.path.realpath(__file__)) + "/gbks/"
print("The path of working script is:", path)
entries = [f for f in os.listdir(path) ] #if os.path.isfile(os.path.join(path,f)) and re.search(r'.gbk*', os.path.splitext(f)[1])]
print("I found such files in genomes directory:", ', '.join(entries))
faa_path = path + "renamed/"
os.mkdir(faa_path)
for i in entries:
    new_path = path+i
    filename, file_extension = os.path.splitext(i)
    fl = open(new_path,'r')
    final_features = []
    for record in SeqIO.parse(fl, 'genbank'):
        class_lst = str(''.join(list(chain.from_iterable([feature.qualifiers['product_class_score'] for feature in record.features if feature.type == 'cluster' ]))))
        matches = class_lst.split(',')
        dic= dict()
        matches = [m.split('=', 1) for m in matches]
        d = dict(matches)
        dict_int = dict((k.replace(' ', ''),float(v)) for k,v in d.items())
        key_max, val_max = max(dict_int.items(), key=operator.itemgetter(1))[0], max(dict_int.items(), key=operator.itemgetter(1))[1]
        if key_max == 'NRP':
            key_max = 'nrps'
        elif key_max == 'RiPP':
            key_max = 'microcin'
        elif key_max == 'Saccharide':
            key_max = 'saccharide'
        elif key_max == 'Polyketide':
            key_max = 't2pks'
        elif key_max == 'Terpene':
            key_max = 'terpene'
        for feature in record.features:
            if feature.type == 'cluster':
                od = feature.qualifiers
                add_list = []
                add_list.append(key_max)
                od['product'] = add_list
            final_features.append(feature)
        record.features = final_features
        new_path1 = faa_path + record.id +'_region_'+ i + ".gbk"
        with open(new_path1, "w") as new_gb:
            SeqIO.write(record, new_gb, "genbank")
        
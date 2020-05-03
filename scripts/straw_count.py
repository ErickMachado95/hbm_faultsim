import pandas as pd
import sys



csv_name = sys.argv[1]

df = pd.read_csv(csv_name);

s_out = open("cs_"+csv_name,"w")

s_out.write("trans_1bit,trans_1word,trans_1col,trans_1row,trans_1bank,trans_nbank,trans_nrank,"
+"perm_1bit,perm_1word,perm_1col,perm_1row,perm_1bank,perm_nbank,perm_nrank\n")

s_out.close()

df = df.loc[df['the_straw'] >= 0]
df = df['the_straw']

vals = df.values

count = [0 for i in range(0,14)]

for i in vals:
    count[i] +=1


str_count = [str(i) for i in count]

s = ','.join(str_count)


s_out = open("cs_"+csv_name,"a")

s_out.write(s)






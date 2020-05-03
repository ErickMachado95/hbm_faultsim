import pandas as pd


def get_the_straws(csv_name):
    df = pd.read_csv("comp_s.csv");

    s_out = open(csv_name+"_s.csv","w")

    s_out.write("dram_module,sim_num,sim_stat,trans_1bit,trans_1word,trans_1col,trans_1row,trans_1bank,trans_nbank,trans_nrank,"
    +"perm_1bit,perm_1word,perm_1col,perm_1row,perm_1bank,perm_nbank,perm_nrank,the_straw\n")

    s_out.close()

    df = df.loc[df['the_straw'] >= 0]


    df.to_csv(csv_name+"_s.csv",mode="a",index=False,header=False)





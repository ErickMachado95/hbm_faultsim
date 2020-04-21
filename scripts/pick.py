import pandas as pd


def filter_and_print(csv_name):
    dff = pd.read_csv("comp_f.csv")
    dfc = pd.read_csv("comp_c.csv")

    f_out = open(csv_name+"_f.csv","w")
    c_out = open(csv_name+"_c.csv","w")
    f_out.write("dram_module,sim_num,sim_stat,trans_1bit,trans_1word,trans_1col,trans_1row,trans_1bank,trans_nbank,trans_nrank,"
    +"perm_1bit,perm_1word,perm_1col,perm_1row,perm_1bank,perm_nbank,perm_nrank\n")

    c_out.write("dram_module,sim_num,sim_stat,trans_1bit,trans_1word,trans_1col,trans_1row,trans_1bank,trans_nbank,trans_nrank,"
    +"perm_1bit,perm_1word,perm_1col,perm_1row,perm_1bank,perm_nbank,perm_nrank\n")
    f = []
    c = []

    f.append(dff.loc[dff['trans_1bit'] > 0])
    f.append(dff.loc[dff['trans_1word'] >0])
    f.append(dff.loc[dff['trans_1col'] > 0])
    f.append(dff.loc[dff['trans_1row'] >0])
    f.append(dff.loc[dff['trans_1bank'] > 0])
    f.append(dff.loc[dff['trans_nbank'] >0])
    f.append(dff.loc[dff['trans_nrank'] > 0])


    f.append(dff.loc[dff['perm_1bit'] > 0])
    f.append(dff.loc[dff['perm_1word'] >0])
    f.append(dff.loc[dff['perm_1col'] > 0])
    f.append(dff.loc[dff['perm_1row'] >0])
    f.append(dff.loc[dff['perm_1bank'] > 0])
    f.append(dff.loc[dff['perm_nbank'] >0])
    f.append(dff.loc[dff['perm_nrank'] > 0])

    c.append(dfc.loc[dfc['trans_1bit'] > 0])
    c.append(dfc.loc[dfc['trans_1word'] >0])
    c.append(dfc.loc[dfc['trans_1col'] > 0])
    c.append(dfc.loc[dfc['trans_1row'] >0])
    c.append(dfc.loc[dfc['trans_1bank'] > 0])
    c.append(dfc.loc[dfc['trans_nbank'] >0])
    c.append(dfc.loc[dfc['trans_nrank'] > 0])


    c.append(dfc.loc[dfc['perm_1bit'] > 0])
    c.append(dfc.loc[dfc['perm_1word'] >0])
    c.append(dfc.loc[dfc['perm_1col'] > 0])
    c.append(dfc.loc[dfc['perm_1row'] >0])
    c.append(dfc.loc[dfc['perm_1bank'] > 0])
    c.append(dfc.loc[dfc['perm_nbank'] >0])
    c.append(dfc.loc[dfc['perm_nrank'] > 0])


    for i in f:
        i.to_csv(csv_name+"_f.csv",mode="a",index=False,header=False)

    for i in c:
        i.to_csv(csv_name+"_c.csv",mode="a",index=False,header=False)

    f_out.close()



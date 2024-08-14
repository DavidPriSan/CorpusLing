import pandas as pd

df = pd.read_csv("./collocates.tsv", sep = "\t")

rslt_df = df[df['ID'] < 3000]

rslt_df.to_csv("collocates2.tsv", sep = "\t", index = False, header = True)


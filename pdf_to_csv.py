import fitz
import pandas as pd
def ptc(filename):
    doc = fitz.open(filename+".pdf")
    page_df_lst=[]
    for page in doc:
        tables = page.find_tables()
        table = tables[0]
        page_df = table.to_pandas()
        page_df_lst.append(page_df)

    df = pd.concat(page_df_lst)
    df.to_csv(f"{filename}.csv",index =False)
    print('done')
    return
ptc("EB purchase")
ptc("EB redemption")
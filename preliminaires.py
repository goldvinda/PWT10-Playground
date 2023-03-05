import pandas as pd
pwt = pd.read_excel('pwt1001.xlsx', sheet_name="Data")
pwt_subset = pwt[['country','countrycode','year','cgdpo','pop','emp','hc','cn','labsh','ctfp']]
pwt_subset = pwt_subset[pwt_subset['year'] > 2009].set_index('countrycode').dropna()

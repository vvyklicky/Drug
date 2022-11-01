#!/usr/bin/env python
# encoding: utf-8

import pandas as pd

drug_list = ["Adenosine","Adenocard","BG8967","Bivalirudin","BAYT006267","diflucan","ibrutinib","PC-32765"]

if __name__ == '__main__':

    def name_norm(org_form):
        normed_form = []

        for i in org_form:
            df = pd.read_json('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{}/synonyms/json'.format(i))
            df.columns =['json_format']
            df_split = pd.json_normalize(df['json_format'][0])
            synonym = str(df_split.iloc[0,[1]])
            list = synonym.split(',')
            item = list[0]
            item = item[12:]
            item_upp = item.upper()
            normed_form.append(item_upp)

        dict = {'org_form': org_form, 'normed_form': normed_form}
        df_out = pd.DataFrame(dict, columns=['org_form', 'normed_form'])
        return(df_out)

    print(name_norm(drug_list))
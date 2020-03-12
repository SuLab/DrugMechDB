import pandas as pd

def auto_adjust_columns_width(writer, sheet, df):
    worksheet = writer.sheets[sheet]  # pull worksheet object
    for idx, col in enumerate(df):  # loop through all columns
        series = df[col]
        max_len = max((
            series.astype(str).map(len).max(),  # len of largest item
            len(str(series.name))  # len of column name/header
            )) + 1  # adding a little extra space
        worksheet.set_column(idx, idx, max_len)  # set column width

# Change DOI to get newer version of DrugMechDB
DOI = 3708278
file_location = "https://zenodo.org/record/{}/files/".format(DOI) + \
                "indication_MOA_paths.xlsx?download=1"

# Get the latest iteration of DrugMech DB

print('Downloading: ', file_location)
dmdb = pd.read_excel(file_location, None)
mps = dmdb['metapaths']

# Import our local mapper for edge types
mapper = pd.read_csv('dmdb_to_bl_map.csv')
edge_mapper = (mapper.set_index(['start_label', 'sem_type', 'end_label'])['type_bl']
                     .dropna()
                     .to_dict())

if __name__ == "__main__":
    # Update the edge types
    for idx, row in enumerate(mps.itertuples(index=False)):
        for i in range(0, len(mps.T)-1, 2):
            if pd.isnull(row[i+1]):
                continue
            tup = (row[i], row[i+1], row[i+2])
            # Fill missing map values with ALL CAPS version
            out = edge_mapper.get(tup, tup[1].upper())
            mps.iloc[idx, i+1] = out

    # Create a mapper for update node types
    node_map = pd.Series(data=mapper[['start_bl', 'end_bl']].stack(dropna=False).values,
                         index=mapper[['start_label', 'end_label']].stack().values)
    node_map = node_map.fillna(pd.Series(node_map.index.str.upper().values))
    node_map = node_map.to_dict()

    n_cols = [c for c in mps.columns if c.startswith('n')]
    for col in n_cols:
        mps.loc[:, col] = mps.loc[:, col].map(node_map)

    # Insert the updated biolink metapaths back into the spreadsheet
    dmdb['metapaths_biolink'] = mps

    # Write the output
    print('Writing: indication_MOA_paths.xlsx')
    with pd.ExcelWriter('indication_MOA_paths.xlsx', engine='xlsxwriter') as writer:
        for sheet, data in dmdb.items():
            data.to_excel(writer, sheet, index=False)
            auto_adjust_columns_width(writer, sheet, data)
        writer.save()


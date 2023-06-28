import functools
from itertools import chain
from wikidataintegrator.wdi_core import WDItemEngine
from data_tools.df_processing import char_combine_iter, expand_col_on_char, add_curi


def parse_result_uris(result):
    """Parse the result URI to get just the WikiData identifier"""
    for c in result:
        if 'Label' not in c:
            idx = result[c].fillna('').str.startswith('http://www.wikidata.org/entity')
            if idx.sum() != 0:
                idx = idx[idx].index
                result.loc[idx, c] = result.loc[idx, c].apply(lambda u: u.split('/')[-1])
    return result.drop_duplicates()


def execute_sparql_query(query_text, endpoint='https://query.wikidata.org/sparql'):
    """Wrapper for wikidataintegrator.wdi_core.WDItemEngine.execute_sparql_query to get useful output formatting"""

    query_func = functools.partial(WDItemEngine.execute_sparql_query, endpoint=endpoint, as_dataframe=True)

    # Enforce the proper column order
    col_order = query_text.lstrip('\n').split('\n')[0].strip().split(' ?')[1:]
    qres = query_func(query_text)
    if len(qres) == 0:
        return None

    # if there are zero results for a query term, the column is removed... we still want the column....
    for c in col_order:
        if c not in qres.columns:
            qres[c] = float('nan')

    return parse_result_uris(qres)[col_order]


def standardize_nodes(result, item_name):
    """Standardizes DataFrame format for nodes queried from wikidata"""
    # Get the columns that are not the item id or name
    xrefs = [c for c in result.columns if c not in [item_name, item_name+'Label']]

    # Make a map from id to name
    id_to_name = result.set_index(item_name)[item_name+'Label'].to_dict()

    # Group all the xrefs for a given ID and pipe separate them all
    out = (result.groupby(item_name)[xrefs]
                  .apply(lambda f: char_combine_iter([v for v in chain(*f.values) if str(v) != 'nan'], sort=True))
                  .rename('xrefs'))

    # Standardize the colnames
    out = out.to_frame().reset_index().rename(columns={item_name: 'id'})
    out['name'] = out['id'].map(id_to_name)
    out['label'] = item_name.replace('_', ' ').title()

    return out[['id', 'name', 'label', 'xrefs']]


def standardize_edges(q_res, start_id, end_id, sem_type, d_source_type='crowd_sourced'):
    """Standardizes DataFrame format for edges queried from wikidata"""
    # Create the map for column renaming
    col_rename_map = {start_id: 'start_id', end_id: 'end_id'}

    # rename the column containing the semantics
    if sem_type in q_res.columns:
        col_rename_map[sem_type] = 'type'
    # Some results are uniform semanitcs, therefore contain no semantics column
    else:
        q_res['type'] = sem_type

    # rename the columns and return with proper order
    out = q_res.rename(columns=col_rename_map).copy()
    out['dsrc_type'] = d_source_type

    return out[['start_id', 'end_id', 'type', 'dsrc_type']]


def node_query_pipeline(query_text, curi_map, item_name):
    """Run the entire pipeline for querying WikiData for nodes"""
    # Execute the Query
    result = execute_sparql_query(query_text)
    if result is None:
        return result
    # Add CURIs
    result = add_curi(result, curi_map)
    # Format the DataFrame to nodes
    result = standardize_nodes(result, item_name)

    return result


def get_xrefs(nodes):
    return expand_col_on_char(nodes[['id', 'xrefs']], 'xrefs', '|', dropna=True)


def get_curi_xrefs(nodes, curi):
    out = get_xrefs(nodes)
    return out[out['xrefs'].str.startswith(curi+':')].copy()


def xref_to_wd_item(nodes, xref_id, always_list=False):
    out = get_xrefs(nodes)
    out = out.query('xrefs == @xref_id')['id'].tolist()
    if always_list or len(out) > 1:
        return out
    elif len(out) == 1:
        return out[0]
    else:
        return None


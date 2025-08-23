#!/usr/bin/env python
# coding: utf-8

# In[1]:
#pip install mofax
import cptac
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as sns
import os
import umap
import mofax as mofa
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from mofapy2.run.entry_point import entry_point
os.environ['R_HOME'] = '/Library/Frameworks/R.framework/Resources'


# In[2]:
def read_csv_df(file_path, sep=',', index_col=None, nrows=None, header='infer'):
    """
    Parameters:
        file_path (str): Path to the CSV file.
        sep (str): Column separator (default = ',').
        index_col (int or None): Column to use as row labels.
        nrows (int or None): Number of rows to read (for preview/testing).
        header (int, list of int, or 'infer'): Row(s) to use as header.
    """
    df = pd.read_csv(file_path, sep='\t', index_col=index_col, header=header)
    return df
TF_df = pd.read_csv('/Users/sathya/work/Data/TFactivity/CPTACdatasets/TFs/TF_names_v_1.01.txt', header=None) #manually curated TFs proteins are obtained from https://humantfs.ccbr.utoronto.ca/
TF_df.shape
#TF_list = TF_df['feature'].dropna().unique().tolist()
TF_list = TF_df[0].dropna().unique().tolist()
#print(TF_list)


# In[3]:
def filter_genes(df, gene_list, axis=0):
    """
    Parameters:
        df (pd.DataFrame): The input DataFrame (genes as rows or columns).
        gene_list (list or set): List of gene names to keep.
        axis (int): 0 = filter rows (default), 1 = filter columns.
    """
    if axis == 0:
        return df.loc[df.index.intersection(gene_list)]
    elif axis == 1:
        return df.loc[:, df.columns.intersection(gene_list)]
    else:
        raise ValueError("axis must be 0 (rows) or 1 (columns)")


# In[4]:
def filter_genes_ppm(df, gene_list, axis=0):
    """
    Parameters:
        df (pd.DataFrame): The input DataFrame (genes as rows or columns).
        gene_list (list or set): List of gene names to keep.
        axis (int): 0 = filter rows (default), 1 = filter columns.
    """
    if axis == 0:
        df = df.loc[df['Gene'].isin(gene_list)]
        df.drop(columns=['Gene'], inplace=True)
        return df
        #return df.loc[df['Gene'].intersection(gene_list)]
    elif axis == 1:
        df = df.loc[:, df['Gene'].isin(gene_list)]
        f.drop(columns=['Gene'], inplace=True)
        return df
        #return df.loc[:, df['Gene'].isin(gene_list)]
    else:
        raise ValueError("axis must be 0 (rows) or 1 (columns)")


# In[5]:
#Scale dfs
scaler = StandardScaler()
def scale_df(df, axis=1):
    if axis == 1:
        df_scaled = pd.DataFrame(scaler.fit_transform(df.T).T, index=df.index, columns=df.columns)
        return df_scaled
    if axis == 0:    
        df_scaled = pd.DataFrame(scaler.fit_transform(df), index=df.index, columns=df.columns)
        return df_scaled


# In[6]:
def make_long(df, view):
    """
    Parameters:
        df (pd.DataFrame): The input wide df (rows = genes, cols = samples)
        view = string denoting the view type .e.g. "RNA"/"Protein"/"PPM"
    """
    df_long = df.reset_index().melt(id_vars='attrib_name', var_name='Patient_ID', value_name='Value')
    df_long = df_long.rename(columns={'index': 'Name'})
    df_long['view'] = view
    return df_long

def print_non_numeric_values(df, column):
    coerced = pd.to_numeric(df[column], errors='coerce')
    non_numeric = df.loc[coerced.isna() & df[column].notna(), column]
    print(non_numeric.unique())


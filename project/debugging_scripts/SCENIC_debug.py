import os
import glob
import pickle
import pandas as pd
import numpy as np
from sys import argv

from dask.distributed import Client, progress
from dask.diagnostics import ProgressBar

from arboreto.utils import load_tf_names
from arboreto.algo import grnboost2

#from ctxcore.rnkdb import FeatherRankingDatabase as RankingDatabase
#from pyscenic.utils import modules_from_adjacencies, load_motifs
#from pyscenic.prune import prune2df, df2regulons
#from pyscenic.aucell import aucell

import env_variables as env

#import seaborn as sns

def get_matrix(fh, cols):
    ex_matrix = pd.read_csv(fh, sep='\t', header=0, index_col=0).T
    ex_matrix = ex_matrix.iloc[:, :cols]
    return ex_matrix
    

if __name__ == '__main__':
    #Variable names
    #c = argv[1]
    c = Client()
    matrix_fh = env.SC_EXP_FNAME
    
    #Get matrix
    ex_matrix = get_matrix(matrix_fh, 12000)

    #Run
    adjacencies2 = grnboost2(ex_matrix, verbose=True, client_or_address=c)


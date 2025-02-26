# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:59:29 2025

@author: maxle
"""

# plotting the combo ones again

#Importing packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as scp
#PCA plots
from sklearn.decomposition import PCA
#for adjusting labels
from adjustText import adjust_text
#for exploring dataset with many scatterplots
from pandas.plotting import scatter_matrix

custom_order = ['SLK', 'Other A', 'Other B', 'Other C']
texts = []

ComboSplit = pd.read_csv('C:/Python/Thesis/Means - Combo Split.csv')
ComboSplitIndex = ComboSplit.copy()
ComboSplitIndex.set_index('Sample', inplace=True)

# Ca-Si
plt.figure(dpi=200)
sns.scatterplot(x='Ca in wt%', y='Si in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Combo[i] == 'Yes':
        texts.append(
            plt.text(x=ComboSplit.Ca[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()

# Ca-Fe
plt.figure(dpi=200)
sns.scatterplot(x='Ca in wt%', y='Fe in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Combo[i] == 'Yes':
        texts.append(
            plt.text(x=ComboSplit.Ca[i],y=ComboSplit.Fe[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()


# Fe-Mg
plt.figure(dpi=200)
sns.scatterplot(x='Fe in wt%', y='Mg in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Combo[i] == 'Yes':
        texts.append(
            plt.text(x=ComboSplit.Fe[i],y=ComboSplit.Mg[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()



# Ca-Fe
plt.figure(dpi=200)
sns.scatterplot(x='Ca in wt%', y='Fe in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
# for i in range(ComboSplit.shape[0]):
#     if ComboSplit.Combo[i] == 'Yes':
#         texts.append(
#             plt.text(x=ComboSplit.Fe[i],y=ComboSplit.Mg[i],
#                   s=ComboSplit.Sample[i], 
#                   fontdict=dict(color='black',size=5),
#                   bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
#             )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()




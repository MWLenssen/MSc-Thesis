# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:18:39 2025

@author: maxle
"""

# SLK variation plots

# Mn-Al
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Mn', y='Al', data=SLKonlySquares, hue='Square', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=ComboSplit.Mn[i],y=ComboSplit.Al[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# Mn-Ca
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Mn', y='Ca', data=SLKonlySquares, hue='Fragment', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=ComboSplit.Mn[i],y=ComboSplit.Ca[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# Cr-Al
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Cr', y='Al', data=SLKonlySquares, hue='Fragment', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=ComboSplit.Cr[i],y=ComboSplit.Al[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# Cr-K
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Cr', y='K', data=SLKonlySquares, hue='Fragment', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=ComboSplit.Cr[i],y=ComboSplit.K[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# V-Si
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='V', y='Si', data=SLKonlySquares, hue='Fragment', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=ComboSplit.V[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# S-Fe
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='S', y='Fe', data=SLKonlySquares, hue='Fragment', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=ComboSplit.S[i],y=ComboSplit.Fe[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# S-Si
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='S', y='Si', data=SLKonlySquares, hue='Fragment', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=ComboSplit.S[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# P-Al
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='P', y='Al', data=SLKonlySquares, hue='Fragment', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=ComboSplit.P[i],y=ComboSplit.Al[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# P-Si
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='P', y='Si', data=SLKonlySquares, hue='Fragment', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=ComboSplit.P[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# Al-Fe
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Al', y='Fe', data=SLKonlySquares, hue='Fragment', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=ComboSplit.Al[i],y=ComboSplit.Fe[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# Ca-Si
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Si', data=SLKonlySquares, hue='Fragment', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=ComboSplit.Ca[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# Fe-K
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='K', data=SLKonlySquares, hue='Fragment', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=ComboSplit.Fe[i],y=ComboSplit.K[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# Fe-Si
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Si', data=SLKonlySquares, hue='Fragment', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=ComboSplit.Fe[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()


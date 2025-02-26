# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 19:31:56 2025

@author: maxle
"""

# Crazy data exploration section

# Further data exploration using ComboSplit
# Trying the following elements because they look promising
    # Mn
    # Cr
    # V
    # Cl
    # S
    # P
    # Al
# The following elements were already proven quite useful
    # Ca
    # Fe
    # K
    # Si
# Specific combos
    # Si-V
    # Mg-Ti

#  Si-V
plt.figure(dpi=200)
sns.scatterplot(x='Si', y='V', data=ComboSplit, hue='Prov')
plt.title('Bivariate plot Si & V')
plt.show()

# Mg-Ti
plt.figure(dpi=200)
sns.scatterplot(x='Mg', y='Ti', data=ComboSplit, hue='Prov')
plt.title('Bivariate plot Mg & Ti')
plt.show()

# Lots of Mn combinations now
# Also not doing title to save time rn
# Mn-Ca
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Mn', y='Ca', data=ComboSplit, hue='Prov', edgecolor=('black'))
# for i in range(ComboSplit.shape[0]):
#     if ComboSplit.Prov[i] == 'SLK':
#         texts.append(
#             plt.text(x=ComboSplit.Mn[i],y=ComboSplit.Ca[i],
#                  s=ComboSplit.Sample[i], 
#                  fontdict=dict(color='black',size=5),
#                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
#             )
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# Mn-Fe
#  DONT WANT TO USE------------------------------------------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Mn', y='Fe', data=ComboSplit, hue='Prov', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=ComboSplit.Mn[i],y=ComboSplit.Fe[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# Mn-K
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Mn', y='K', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Mn-Si
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Mn', y='Si', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Mn-Cr
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Mn', y='Cr', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
    # V
    # Cl
    # S
    # P
    # Al
# Mn-V
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Mn', y='V', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Mn-Cl
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Mn', y='Cl', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Mn-S
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Mn', y='S', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Mn-P
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Mn', y='P', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Mn-Al
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Mn', y='Al', data=ComboSplit, hue='Prov', edgecolor=('black'))
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
# Trying the following elements because they look promising
    # Mn
    # Cr
    # V
    # Cl
    # S
    # P
    # Al
# The following elements were already proven quite useful
    # Ca
    # Fe
    # K
    # Si
# Cr-V
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Cr', y='V', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Cr-Cl
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Cr', y='Cl', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Cr-S
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Cr', y='S', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Cr-P
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Cr', y='P', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Cr-Al
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Cr', y='Al', data=ComboSplit, hue='Prov', edgecolor=('black'))
# for i in range(ComboSplit.shape[0]):
#     if ComboSplit.Prov[i] == 'SLK':
#         texts.append(
#             plt.text(x=ComboSplit.Cr[i],y=ComboSplit.Al[i],
#                   s=ComboSplit.Sample[i], 
#                   fontdict=dict(color='black',size=5),
#                   bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
#             )
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# Cr-Ca
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Cr', y='Ca', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Cr-Fe
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Cr', y='Fe', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Cr-K
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Cr', y='K', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Cr-Si
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Cr', y='Fe', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Trying the following elements because they look promising
    # Mn
    # Cr
    # V
    # Cl
    # S
    # P
    # Al
# The following elements were already proven quite useful
    # Ca
    # Fe
    # K
    # Si
# V-Cl
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='V', y='Cl', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# V-S
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='V', y='S', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# V-P
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='V', y='P', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# V-Al
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='V', y='Al', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# V-Ca
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='V', y='Ca', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# V-Fe
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='V', y='Fe', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# V-K
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='V', y='K', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# V-Si
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='V', y='Si', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Trying the following elements because they look promising
    # Mn
    # Cr
    # V
    # Cl
    # S
    # P
    # Al
# The following elements were already proven quite useful
    # Ca
    # Fe
    # K
    # Si
# Cl-S
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Cl', y='S', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Cl-P
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Cl', y='P', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Cl-Al
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Cl', y='Al', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Cl-Ca
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Cl', y='Ca', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Cl-Fe
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Cl', y='Fe', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Cl-K
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Cl', y='K', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Cl-Si
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Cl', y='Si', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Trying the following elements because they look promising
    # Mn
    # Cr
    # V
    # Cl
    # S
    # P
    # Al
# The following elements were already proven quite useful
    # Ca
    # Fe
    # K
    # Si
# S-P
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='S', y='P', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# S-Al
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='S', y='Al', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# S-Ca
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='S', y='Ca', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# S-Fe
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='S', y='Fe', data=ComboSplit, hue='Prov', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
        texts.append(
            plt.text(x=ComboSplit.S[i],y=ComboSplit.Fe[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    if ComboSplit.Prov[i] == 'Other C':
        texts.append(
            plt.text(x=ComboSplit.S[i],y=ComboSplit.Fe[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# S-K
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='S', y='K', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# S-Si
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='S', y='Si', data=ComboSplit, hue='Prov', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
        texts.append(
            plt.text(x=ComboSplit.S[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    if ComboSplit.Prov[i] == 'Other C':
        texts.append(
            plt.text(x=ComboSplit.S[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# Trying the following elements because they look promising
    # Mn
    # Cr
    # V
    # Cl
    # S
    # P
    # Al
# The following elements were already proven quite useful
    # Ca
    # Fe
    # K
    # Si
# P-Al
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='P', y='Al', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# P-Ca
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='P', y='Ca', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# P-Fe
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='P', y='Fe', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# P-K
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='P', y='K', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# P-Si
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='P', y='Si', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Trying the following elements because they look promising
    # Mn
    # Cr
    # V
    # Cl
    # S
    # P
    # Al
# The following elements were already proven quite useful
    # Ca
    # Fe
    # K
    # Si
# Al-Ca
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Al', y='Ca', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Al-Fe
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Al', y='Fe', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Al-K
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Al', y='K', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Al-Si
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Al', y='Si', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Trying the following elements because they look promising
    # Mn
    # Cr
    # V
    # Cl
    # S
    # P
    # Al
# The following elements were already proven quite useful
    # Ca
    # Fe
    # K
    # Si
# Ca-Fe
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Fe', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Ca-K
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='K', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Ca-Si
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Si', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Trying the following elements because they look promising
    # Mn
    # Cr
    # V
    # Cl
    # S
    # P
    # Al
# The following elements were already proven quite useful
    # Ca
    # Fe
    # K
    # Si
# Fe-K
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='K', data=ComboSplit, hue='Prov', edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
        texts.append(
            plt.text(x=ComboSplit.Fe[i],y=ComboSplit.K[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    if ComboSplit.Prov[i] == 'Other C':
        texts.append(
            plt.text(x=ComboSplit.Fe[i],y=ComboSplit.K[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.show()
# Fe-Si
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Si', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()
# Trying the following elements because they look promising
    # Mn
    # Cr
    # V
    # Cl
    # S
    # P
    # Al
# The following elements were already proven quite useful
    # Ca
    # Fe
    # K
    # Si
# K-Si
#  DONT WANT TO USE -------------------DONT WANT TO USE------------------------
plt.figure(dpi=200)
sns.scatterplot(x='K', y='Si', data=ComboSplit, hue='Prov', edgecolor=('black'))
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:31:14 2025

@author: maxle
"""

plt.figure(dpi=200)
sns.scatterplot(x='Ca in wt%', y='Fe in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Type[i] == 'Modeled Legs':
        texts.append(
            plt.text(x=ComboSplit.Ca[i],y=ComboSplit.Fe[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Ca in wt%', y='Si in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Type[i] == 'Modeled Legs':
        texts.append(
            plt.text(x=ComboSplit.Ca[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Mn in wt%', y='Al in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Type[i] == 'Modeled Legs':
        texts.append(
            plt.text(x=ComboSplit.Mn[i],y=ComboSplit.Al[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Cr in ppm', y='K in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Type[i] == 'Modeled Legs':
        texts.append(
            plt.text(x=ComboSplit.Cr_ppm[i],y=ComboSplit.K[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='S in wt%', y='Si in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Type[i] == 'Modeled Legs':
        texts.append(
            plt.text(x=ComboSplit.S[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Mn in wt%', y='Ca in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Type[i] == 'Modeled Legs':
        texts.append(
            plt.text(x=ComboSplit.Mn[i],y=ComboSplit.Ca[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='V in ppm', y='Si in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Type[i] == 'Modeled Legs':
        texts.append(
            plt.text(x=ComboSplit.V_ppm[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='P in wt%', y='Al in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Type[i] == 'Modeled Legs':
        texts.append(
            plt.text(x=ComboSplit.P[i],y=ComboSplit.Al[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Cr in ppm', y='Al in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Type[i] == 'Modeled Legs':
        texts.append(
            plt.text(x=ComboSplit.Cr_ppm[i],y=ComboSplit.Al[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='P in wt%', y='Si in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Type[i] == 'Modeled Legs':
        texts.append(
            plt.text(x=ComboSplit.P[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()




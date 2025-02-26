# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:48:58 2025

@author: maxle
"""

# Making an order for the hue/legend
OrderSLKnOther = ['SLK', 'Other']
texts = []

plt.figure(dpi=200)
sns.scatterplot(x='Ca in wt%', y='Si in wt%', data=SLKnOther, hue='Prov', hue_order=OrderSLKnOther, edgecolor=('black'))
# for i in range(ComboSplit.shape[0]):
#     if ComboSplit.Prov[i] == 'Other A':
#         texts.append(
#             plt.text(x=ComboSplit.Fe[i],y=ComboSplit.Si[i],
#                   s=ComboSplit.Sample[i], 
#                   fontdict=dict(color='black',size=5),
#                   bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
#             )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()

# Other A & C labeled Si - Ca
plt.figure(dpi=200)
sns.scatterplot(x='Ca in wt%', y='Si in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
        texts.append(
            plt.text(x=ComboSplit.Ca[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    if ComboSplit.Prov[i] == 'Other C':
        texts.append(
            plt.text(x=ComboSplit.Ca[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()


# Location order for hue
LocationOrder = ['S25','U21','V23','W20','W21','W24','X20','X21','X22','X23','X24','X45']
# Fragment order for hue
FragmentOrder = ['Head','Upper body + head','Upper body','Base']
# Typology order for hue
TypeOrder = ['Head','Head w pellet hairdo','Arms folded','Arms folded up','Arms forward','Arms outwards','Arms missing','Base']

#Location
    # for Ca & Fe
plt.figure(dpi=200)
sns.scatterplot(x='Ca in wt%', y='Fe in wt%', data=SLKonlySquares, hue='Square', hue_order=LocationOrder)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Location")
plt.show() 

# Typology
    # for Ca & Fe
plt.figure(dpi=200)
sns.scatterplot(x='Ca in wt%', y='Fe in wt%', data=SLKonlySquares, hue='Type', hue_order=TypeOrder)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()

# Fragment type
    # for Ca & Fe
plt.figure(dpi=200)
sns.scatterplot(x='Ca in wt%', y='Fe in wt%', data=SLKonlySquares, hue='Fragment', hue_order=FragmentOrder)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Fragment type")
plt.show()


#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='V in ppm', y='Si in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
        texts.append(
            plt.text(x=ComboSplit.V[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    if ComboSplit.Prov[i] == 'Other C':
        texts.append(
            plt.text(x=ComboSplit.'V in ppm'[i],y=ComboSplit.'Si in wt%'[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:40:21 2024

@author: maxle
"""

#Importing packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# import scipy as scp
#PCA plots
# from sklearn.decomposition import PCA
#for adjusting labels
from adjustText import adjust_text
#for exploring dataset with many scatterplots
# from pandas.plotting import scatter_matrix

custom_order = ['SLK', 'Other A', 'Other B', 'Other C']

#Importing CSV
XRFdata = pd.read_csv('C:/Python/Thesis/All XRF Data CSV.csv')


#Changing '< LOD' to 0
XRFdataZero = XRFdata.replace({'< LOD': 0.0})
ToConvert = ['Na', 'Al', 'Cl', 'V', 'Co', 'Ga', 'As', 'Se', 'Rb', 'Y', 'Zr', 
             'Nb', 'Mo', 'Ba', 'Pb', 'Th']
XRFdataZero[ToConvert] = XRFdataZero[ToConvert].astype(float)

#With Arms "typology"
XRFdata_Arms = pd.read_csv('C:/Python/Thesis/All XRF Data CSV - with Arms type.csv')
XRFdata_ArmsZero = XRFdata_Arms.replace({'< LOD': 0.0})
XRFdata_ArmsZero[ToConvert] = XRFdata_ArmsZero[ToConvert].astype(float)


#Removing samples I don't want to include
DroppedSamples = XRFdata_ArmsZero.copy()
DroppedSamples.set_index('Type', inplace=True)  
DroppedSamples = DroppedSamples.drop('DROP')


#Removing two samples with outliers in Sr
XRFdata_NoSr = DroppedSamples.copy()
XRFdata_NoSr.set_index('Sample', inplace=True)
XRFdata_NoSr = XRFdata_NoSr.drop(['MW_22.1', 'MW_22.2a'])


#Making a new dataframe with means of each sample
XRFmeans = XRFdataZero.copy()
XRFmeans.set_index('Sample', inplace=True)
XRFmeans.drop(columns=['DateTime', 'Operator', 'Material','Project', 
                        'User', 'Application', 'Method', 
                        'ElapsedTime', 'U', 'Multiplier', 'Cal Check', 
                        'File #', 'Prov', 'Type'], inplace=True)

#MW_1
MW1rows = XRFmeans.loc[['MW_1.1', 'MW_1.2']]
MW1_Av = MW1rows.mean()
XRFmeans.loc['MW_1 Mean'] = MW1_Av
#MW_2
MW2rows = XRFmeans.loc[['MW_2.1', 'MW_2.2', 'MW_2.3']]
MW2_Av = MW2rows.mean()
XRFmeans.loc['MW_2 Mean'] = MW2_Av
#MW_3
MW3rows = XRFmeans.loc[['MW_3.1', 'MW_3.1A', 'MW_3.2A', 'MW_3.3']]
MW3_Av = MW3rows.mean()
XRFmeans.loc['MW_3 Mean'] = MW3_Av
#MW_4
MW4rows = XRFmeans.loc[['MW_4.1', 'MW_4.2', 'MW_4.3']]
MW4_Av = MW4rows.mean()
XRFmeans.loc['MW_4 Mean'] = MW4_Av
#MW_5
MW5rows = XRFmeans.loc[['MW_5.1', 'MW_5.2', 'MW_5.3']]
MW5_Av = MW5rows.mean()
XRFmeans.loc['MW_5 Mean'] = MW5_Av
#MW_6a
MW6arows = XRFmeans.loc[['MW_6a.1', 'MW_6a.2', 'MW_6a.3', 'MW_6a.4']]
MW6a_Av = MW6arows.mean()
XRFmeans.loc['MW_6a Mean'] = MW6a_Av
#MW_6b
MW6brows = XRFmeans.loc[['MW_6b.1', 'MW_6b.1']]
MW6b_Av = MW6brows.mean()
XRFmeans.loc['MW_6b Mean'] = MW6b_Av

# !!! ATTENTIONE !!!
#MW_7 Torso
MW7rows_torso = XRFmeans.loc[['MW_7.1', 'MW_7.5']]
MW7_AvTorso = MW7rows_torso.mean()
XRFmeans.loc['MW_7 Torso Mean'] = MW7_AvTorso
#MW_7 Base
MW7rows_base = XRFmeans.loc[['MW_7.2', 'MW_7.4']]
MW7_AvBase = MW7rows_base.mean()
XRFmeans.loc['MW_7 Base Mean'] = MW7_AvBase
# MW_7 Head
XRFmeans = XRFmeans.rename(index={'MW_7.3':'MW_7 Head'})
# MW_7 Shoulder
XRFmeans = XRFmeans.rename(index={'MW_7.6':'MW_7 Shoulder'})
# !!! ATTENTIONE !!!

#8
MW8rows = XRFmeans.loc[['MW_8.1', 'MW_8.2']]
MW8_Av = MW8rows.mean()
XRFmeans.loc['MW_8 Mean'] = MW8_Av
#9
MW9rows = XRFmeans.loc[['MW_9.1', 'MW_9.2']]
MW9_Av = MW9rows.mean()
XRFmeans.loc['MW_9 Mean'] = MW9_Av
#10
MW10rows = XRFmeans.loc[['MW_10.1', 'MW_10.2']]
MW10_Av = MW10rows.mean()
XRFmeans.loc['MW_10 Mean'] = MW10_Av
#11a
MW11arows = XRFmeans.loc[['MW_11a.1', 'MW_11a.2', 'MW_11a.3']]
MW11a_Av = MW11arows.mean()
XRFmeans.loc['MW_11a Mean'] = MW11a_Av
#11b
MW11brows = XRFmeans.loc[['MW_11b.1']]
MW11b_Av = MW11brows.mean()
XRFmeans.loc['MW_11b Mean'] = MW11b_Av

# !!! ATTENTIONE !!!
# 12
# MW_12 Head
XRFmeans = XRFmeans.rename(index={'MW_12.3':'MW_12 Head'})
# MW_12 Necklace
XRFmeans = XRFmeans.rename(index={'MW_12.4':'MW_12 Necklace'})
# MW_12 Torso
XRFmeans = XRFmeans.rename(index={'MW_12.2':'MW_12 Torso'})
#MW_12 Base
XRFmeans = XRFmeans.rename(index={'MW_12.1':'MW_12 Base'})
# !!! ATTENTIONE !!!

#MW_13
MW13rows = XRFmeans.loc[['MW_13.1', 'MW_13.2']]
MW13_Av = MW13rows.mean()
XRFmeans.loc['MW_13 Mean'] = MW13_Av
#MW_14
MW14rows = XRFmeans.loc[['MW_14.1', 'MW_14.2']]
MW14_Av = MW14rows.mean()
XRFmeans.loc['MW_14 Mean'] = MW14_Av
#MW_15
MW15rows = XRFmeans.loc[['MW_15.1', 'MW_15.2']]
MW15_Av = MW15rows.mean()
XRFmeans.loc['MW_15 Mean'] = MW15_Av
#MW_16
MW16rows = XRFmeans.loc[['MW_16.2']]
MW16_Av = MW16rows.mean()
XRFmeans.loc['MW_16 Mean'] = MW16_Av
#MW_17
MW17rows = XRFmeans.loc[['MW_17.1']]
MW17_Av = MW17rows.mean()
XRFmeans.loc['MW_17 Mean'] = MW17_Av

# !!! ATTENTIONE !!!
# MW_18
# MW_12 Head
XRFmeans = XRFmeans.rename(index={'MW_18.3':'MW_18 Head'})
# MW_12 Torso
XRFmeans = XRFmeans.rename(index={'MW_18.2':'MW_18 Torso'})
#MW_12 Base
XRFmeans = XRFmeans.rename(index={'MW_18.1':'MW_18 Base'})
# !!! ATTENTIONE !!!

#MW_19
MW19rows = XRFmeans.loc[['MW_19.1', 'MW_19.2']]
MW19_Av = MW19rows.mean()
XRFmeans.loc['MW_19 Mean'] = MW19_Av
#MW_20
MW20rows = XRFmeans.loc[['MW_20.1', 'MW_20.2']]
MW20_Av = MW20rows.mean()
XRFmeans.loc['MW_20 Mean'] = MW20_Av
#MW_20
MW20rows = XRFmeans.loc[['MW_20.1', 'MW_20.2']]
MW20_Av = MW20rows.mean()
XRFmeans.loc['MW_20 Mean'] = MW20_Av
#MW_21
MW21rows = XRFmeans.loc[['MW_21.1']]
MW21_Av = MW21rows.mean()
XRFmeans.loc['MW_21 Mean'] = MW21_Av
#MW_22
MW22rows = XRFmeans.loc[['MW_22.1', 'MW_22.2a', 'MW_22.3']]
MW22_Av = MW22rows.mean()
XRFmeans.loc['MW_22 Mean'] = MW22_Av
#MW_23
MW23rows = XRFmeans.loc[['MW_23.1', 'MW_23.2']]
MW23_Av = MW23rows.mean()
XRFmeans.loc['MW_23 Mean'] = MW23_Av
#MW_24
MW24rows = XRFmeans.loc[['MW_24.1']]
MW24_Av = MW24rows.mean()
XRFmeans.loc['MW_24 Mean'] = MW24_Av
#MW_25
MW25rows = XRFmeans.loc[['MW_25.1']]
MW25_Av = MW25rows.mean()
XRFmeans.loc['MW_25 Mean'] = MW25_Av
#MW_26
MW26rows = XRFmeans.loc[['MW_26.1', 'MW_26.2', 'MW_26.3', 'MW_26.4', 'MW_26.5']]
MW26_Av = MW26rows.mean()
XRFmeans.loc['MW_26 Mean'] = MW26_Av
#MW_27
MW27rows = XRFmeans.loc[['MW_27.1', 'MW_27.2']]
MW27_Av = MW27rows.mean()
XRFmeans.loc['MW_27 Mean'] = MW27_Av
#MW_28
MW28rows = XRFmeans.loc[['MW_28.1', 'MW_28.2']]
MW28_Av = MW28rows.mean()
XRFmeans.loc['MW_28 Mean'] = MW28_Av
#MW_29
MW29rows = XRFmeans.loc[['MW_29.1', 'MW_29.2']]
MW29_Av = MW29rows.mean()
XRFmeans.loc['MW_29 Mean'] = MW29_Av
#MW_30
MW30rows = XRFmeans.loc[['MW_30.1', 'MW_30.2']]
MW30_Av = MW30rows.mean()
XRFmeans.loc['MW_30 Mean'] = MW30_Av
#MW_31
MW31rows = XRFmeans.loc[['MW_31.1', 'MW_31.2']]
MW31_Av = MW31rows.mean()
XRFmeans.loc['MW_31 Mean'] = MW31_Av
#MW_32
MW32rows = XRFmeans.loc[['MW_32.1', 'MW_32.2']]
MW32_Av = MW32rows.mean()
XRFmeans.loc['MW_32 Mean'] = MW32_Av
#MW_33
MW33rows = XRFmeans.loc[['MW_33.1', 'MW_33.2', 'MW_33.3']]
MW33_Av = MW33rows.mean()
XRFmeans.loc['MW_33 Mean'] = MW33_Av
#MW_34
MW34rows = XRFmeans.loc[['MW_34.1', 'MW_34.2']]
MW34_Av = MW34rows.mean()
XRFmeans.loc['MW_34 Mean'] = MW34_Av
#MW_35
MW35rows = XRFmeans.loc[['MW_35.1', 'MW_35.2', 'MW_35.2', 'MW_35.2a']]
MW35_Av = MW35rows.mean()
XRFmeans.loc['MW_35 Mean'] = MW35_Av
#MW_36
MW36rows = XRFmeans.loc[['MW_36.1', 'MW_36.2', 'MW_36.3']]
MW36_Av = MW34rows.mean()
XRFmeans.loc['MW_36 Mean'] = MW36_Av
#MW_37
MW37rows = XRFmeans.loc[['MW_37.1', 'MW_37.2', 'MW_37.3']]
MW37_Av = MW37rows.mean()
XRFmeans.loc['MW_37 Mean'] = MW37_Av
#MW_38
MW38rows = XRFmeans.loc[['MW_38.1', 'MW_38.2']]
MW38_Av = MW38rows.mean()
XRFmeans.loc['MW_38 Mean'] = MW38_Av
#MW_39
MW39rows = XRFmeans.loc[['MW_39.1']]
MW39_Av = MW39rows.mean()
XRFmeans.loc['MW_39 Mean'] = MW39_Av
#MW_40
MW40rows = XRFmeans.loc[['MW_40.1', 'MW_40.2', 'MW_40.3']]
MW40_Av = MW40rows.mean()
XRFmeans.loc['MW_40 Mean'] = MW40_Av
#MW_41
MW41rows = XRFmeans.loc[['MW_41.1', 'MW_41.2']]
MW41_Av = MW41rows.mean()
XRFmeans.loc['MW_41 Mean'] = MW41_Av
#MW_42
MW42rows = XRFmeans.loc[['MW_42.1', 'MW_42.2']]
MW42_Av = MW42rows.mean()
XRFmeans.loc['MW_42 Mean'] = MW42_Av
#MW_43
MW43rows = XRFmeans.loc[['MW_43.1', 'MW_43.2']]
MW43_Av = MW43rows.mean()
XRFmeans.loc['MW_43 Mean'] = MW43_Av
#MW_44
MW44rows = XRFmeans.loc[['MW_44.1', 'MW_44.2']]
MW44_Av = MW44rows.mean()
XRFmeans.loc['MW_44 Mean'] = MW44_Av
#MW_45
MW45rows = XRFmeans.loc[['MW_45.1', 'MW_45.2']]
MW45_Av = MW45rows.mean()
XRFmeans.loc['MW_45 Mean'] = MW45_Av
#MW_46
MW46rows = XRFmeans.loc[['MW_46.1', 'MW_46.2', 'MW_46.3']]
MW46_Av = MW46rows.mean()
XRFmeans.loc['MW_46 Mean'] = MW46_Av
#MW_47
MW47rows = XRFmeans.loc[['MW_47.1', 'MW_47.2']]
MW47_Av = MW47rows.mean()
XRFmeans.loc['MW_47 Mean'] = MW47_Av





#Selecting only the means  !!!BUT NOW THERES NO TYPE FOR ALL THE MEANS!!!
MeansOnly = XRFmeans.loc[['MW_1 Mean', 'MW_2 Mean', 'MW_3 Mean', 'MW_4 Mean', 'MW_5 Mean', 
             'MW_6a Mean', 'MW_6b Mean', 'MW_7 Head', 'MW_7 Shoulder', 'MW_7 Torso Mean', 
             'MW_7 Base Mean', 'MW_8 Mean', 'MW_9 Mean', 'MW_10 Mean', 'MW_11a Mean', 
             'MW_11b Mean', 'MW_12 Head', 'MW_12 Necklace', 'MW_12 Torso', 'MW_12 Base',
             'MW_13 Mean', 'MW_14 Mean', 'MW_15 Mean', 'MW_16 Mean', 'MW_17 Mean', 
             'MW_18 Head', 'MW_18 Torso', 'MW_18 Base','MW_19 Mean', 'MW_20 Mean', 
             'MW_21 Mean', 'MW_22 Mean', 'MW_23 Mean', 'MW_24 Mean', 'MW_25 Mean', 
             'MW_26 Mean', 'MW_27 Mean', 'MW_28 Mean', 'MW_29 Mean', 'MW_30 Mean', 
             'MW_31 Mean', 'MW_32 Mean', 'MW_33 Mean', 'MW_34 Mean', 'MW_35 Mean', 
             'MW_36 Mean', 'MW_37 Mean', 'MW_38 Mean', 'MW_39 Mean', 'MW_40 Mean', 
             'MW_41 Mean', 'MW_42 Mean', 'MW_43 Mean', 'MW_44 Mean', 'MW_45 Mean', 
             'MW_46 Mean', 'MW_47 Mean']]
MeansOnly[ToConvert] = MeansOnly[ToConvert].astype(float)

MeansOnly.to_csv('MeansOnly.csv', float_format='%.4f', index=True)
MeansType = pd.read_csv('C:/Python/Thesis/MeansOnlyTypes.csv')
MeansType.set_index('Sample', inplace=True)
MeansTypeProv = pd.read_csv('C:/Python/Thesis/MeansOnlyTypesProv.csv')
MeansTypeProv.set_index('Sample', inplace=True)

## Filtering on only SLK
SLK_Only = XRFdata_ArmsZero.copy()
SLK_Only.set_index('Prov', inplace=True)
SLK_Only = SLK_Only.drop('Unkown')
#-------------------------------------------
SLKmeans_Only = MeansTypeProv.copy()
SLKmeans_Only.set_index('Prov', inplace=True)
SLKmeans_Only = SLKmeans_Only.drop('Other')

## Filtering on only Unknown
Unknown_Only = XRFdata_ArmsZero.copy()
Unknown_Only.set_index('Prov', inplace=True)
Unknown_Only = Unknown_Only.drop('SLK')
#-------------------------------------------
UnknownMeans_Only = MeansTypeProv.copy()
UnknownMeans_Only.set_index('Prov', inplace=True)
UnknownMeans_Only = UnknownMeans_Only.drop('SLK')





##############################################################
## Sedimentary/Limestone markers vs Volcanic/Basalt markers ##
## Ca, Sr, Ba, Rb - Sedimentary                             ##
## K, Nb, Y - Volcanic (I also used Si for Basalt marker)   ##
##############################################################

# Calcium (Ca) vs Silicon (Si) with all samples
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Si', data=XRFdata_ArmsZero, hue='Prov')
plt.title('Bivariate plot Ca & Si - Limestone/sedimentary vs Basalt/Volcanic')
plt.show()
# Calcium (Ca) vs Silicon (Si) with only means
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Si', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Ca & Si - Based on means')
plt.show()

# Calcium (Ca) vs Potassium (K) with all samples
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='K', data=XRFdata_ArmsZero, hue='Prov')
plt.title('Bivariate plot Ca & K - Limestone/sedimentary vs Basalt/Volcanic')
plt.show()
# Calcium (Ca) vs Potassium (K) with only means
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='K', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Ca & K - Based on means')
plt.show()

# Calcium (Ca) vs Iron (Fe) with all samples
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Fe', data=XRFdata_ArmsZero, hue='Prov')
plt.title('Bivariate plot Ca & Fe - Limestone/sedimentary vs Basalt/Volcanic')
plt.show()
# Calcium (Ca) vs Iron (Fe) with only means
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Fe', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Ca & Fe - Based on means')
plt.show()

# Calcium (Ca) vs Magnesium (Mg) with all samples
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Mg', data=XRFdata_ArmsZero, hue='Prov')
plt.title('Bivariate plot Ca & Mg - Limestone/sedimentary vs Basalt/Volcanic')
plt.show()
# Calcium (Ca) vs Magnesium (Mg) with only means
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Mg', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Ca & Mg - Based on means')
plt.show()

# Calcium (Ca) vs Zirkonium (Zr) with all samples
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Zr', data=XRFdata_ArmsZero, hue='Prov')
plt.title('Bivariate plot Ca & Zr - Limestone/sedimentary vs Basalt/Volcanic')
plt.show()
# Calcium (Ca) vs Zirkonium (Zr) with only means
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Zr', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Ca & Zr - Based on means')
plt.show()



## For Selenkahiye only

# Calcium (Ca) vs Silicon (Si) with all samples
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='K', data=SLK_Only, hue='Arms')
plt.title('Bivariate plot Ca & K - Only Selenkahiye figurines')
plt.show()
## Calcium (Ca) vs Silicon (Si) with only means
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='K', data=SLKmeans_Only, hue='Arms')
plt.title('Bivariate plot Ca & K - Only Selenkahiye figurines (means)')
plt.show()


## For Unkown provenance only

# Calcium (Ca) vs Silicon (Si) with all samples
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='K', data=Unknown_Only, hue='Arms')
plt.title('Bivariate plot Ca & K - Only unknown provenance')
plt.show()
## Calcium (Ca) vs Silicon (Si) with only means
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='K', data=UnknownMeans_Only, hue='Arms')
plt.title('Bivariate plot Ca & K - Only unknown provenance (means)')
plt.show()



##Trying to label the points


MeansNoMean1 = pd.read_csv('C:/Python/Thesis/MeansTypesProv_NoMeans.csv')
texts = []

plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Fe', data=MeansNoMean1, hue='Prov')
for i in range(MeansNoMean1.shape[0]):
    if MeansNoMean1.Prov[i] == 'Other':
        texts.append(
            plt.text(x=MeansNoMean1.Ca[i],y=MeansNoMean1.Fe[i],
                 s=MeansNoMean1.Sample[i], 
                 fontdict=dict(color='black',size=5),
                 bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
adjust_text(texts, arrowprops=dict(arrowstyle='simple', color='gray', alpha=0))
plt.title('Bivariate plot Ca & Fe - Means - Labels')
plt.show()






# for i in range(data=MeansTypeProv.shape[0]):
    # plt.text(x=MeansTypeProv.Ca[i]+0.3, y=MeansTypeProv.Fe[i]+0.3, 
             # s=MeansTypeProv.Sample[i], fontdict=dict(color='red', size=10),
             # bbox=dict(facecolor='yellow', alpha=0.5))
    

#for i in range(len(MeansTypeProv)):
 #   plt.text(
  #      x=MeansTypeProv['Ca'].iloc[i],  # X-coordinate
   #     y=MeansTypeProv['Fe'].iloc[i],  # Y-coordinate
    #    s=str(MeansTypeProv['Sample'].iloc[i]),  # Text (Sample number)
     #   fontsize=8, color='black', ha='right', va='bottom'
    #)

ComboSplit = pd.read_csv('C:/Python/Thesis/Means - Combo Split.csv')
ComboSplitIndex = ComboSplit.copy()
ComboSplitIndex.set_index('Sample', inplace=True)

# Trying this figure with the new dataframe with the combos split
# plt.figure(dpi=200)
# sns.scatterplot(x='Ca', y='Fe', data=ComboSplit, hue='Prov')
# for i in range(ComboSplit.shape[0]):
#     if ComboSplit.Prov[i] == 'Other C':
#         texts.append(
#             plt.text(x=ComboSplit.Ca[i],y=ComboSplit.Fe[i],
#                  s=ComboSplit.Sample[i], 
#                  fontdict=dict(color='black',size=5),
#                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
#             )
# adjust_text(texts, arrowprops=dict(arrowstyle='simple', color='gray', alpha=0))
# plt.title('Bivariate plot Ca & Fe - Means - Labels')
# plt.show()




###############################################################################
# Line of code to make the dots transparent and change the outline color!
# Useful because MW 34 and 36 are on top of each other and one is invisible...
# , edgecolor='black', alpha=0.5
###############################################################################


plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Fe', data=MeansNoMean1, hue='Prov')
for i in range(MeansNoMean1.shape[0]):
    if MeansNoMean1.Prov[i] == 'Other A':
        texts.append(
            plt.text(x=MeansNoMean1.Ca[i]+0.1,y=MeansNoMean1.Fe[i]+0.1,
                 s=MeansNoMean1.Sample[i], 
                 fontdict=dict(color='black',size=5),
                 bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    if MeansNoMean1.Prov[i] == 'Other B':
        texts.append(
            plt.text(x=MeansNoMean1.Ca[i]+0.1,y=MeansNoMean1.Fe[i]+0.1,
                s=MeansNoMean1.Sample[i], 
                fontdict=dict(color='black',size=5),
                bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    if MeansNoMean1.Prov[i] == 'SLK':
        texts.append(
            plt.text(x=MeansNoMean1.Ca[i]+0.1,y=MeansNoMean1.Fe[i]+0.1,
                s=MeansNoMean1.Sample[i], 
                fontdict=dict(color='black',size=5),
                bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
adjust_text(texts, arrowprops=dict(arrowstyle='-', color='black', alpha=0, lw=1.5))
plt.title('Bivariate plot Ca & Fe - Means - Labels')
plt.show()



# Test copy of the one with the working labels but for different dataframe
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Fe', data=ComboSplit, hue='Prov')
for i in range(ComboSplit.shape[0]):
    # if ComboSplit.Prov[i] == 'Other A':
    #     texts.append(
    #         plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
    #              s=ComboSplit.Sample[i], 
    #              fontdict=dict(color='black',size=5),
    #              bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
    #         )
    # if ComboSplit.Prov[i] == 'Other B':
    #     texts.append(
    #         plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
    #             s=ComboSplit.Sample[i], 
    #             fontdict=dict(color='black',size=5),
    #             bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
    #         )
    if ComboSplit.Prov[i] == 'Other C':
        texts.append(
            plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
                s=ComboSplit.Sample[i], 
                fontdict=dict(color='black',size=5),
                bbox=dict(facecolor='white',alpha=0, pad=0.5, edgecolor='none'))
            )
    # if ComboSplit.Prov[i] == 'SLK':
    #     texts.append(
    #         plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
    #             s=ComboSplit.Sample[i], 
    #             fontdict=dict(color='black',size=5),
    #             bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
    #         )
# !!! THIS WAS THE BITCH THAT RUINED THE LABELS !!!
# !!! adjust_text(texts, arrowprops=dict(arrowstyle='-', color='black', alpha=0, lw=1.5))
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.title('Bivariate plot Ca & Fe - Means - Labels')
plt.show()




# MW_12 labeled
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Fe', data=ComboSplit, hue='Prov')
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Sample[i] == 'MW_12 Head':
        texts.append(
            plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    if ComboSplit.Sample[i] == 'MW_12 Necklace':
        texts.append(
            plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
                s=ComboSplit.Sample[i], 
                fontdict=dict(color='black',size=5),
                bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    if ComboSplit.Sample[i] == 'MW_12 Torso':
        texts.append(
            plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
                s=ComboSplit.Sample[i], 
                fontdict=dict(color='black',size=5),
                bbox=dict(facecolor='white',alpha=0, pad=0.5, edgecolor='none'))
            )
    if ComboSplit.Sample[i] == 'MW_12 Base':
        texts.append(
            plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
                s=ComboSplit.Sample[i], 
                fontdict=dict(color='black',size=5),
                bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
# !!! THIS WAS THE BITCH THAT RUINED THE LABELS !!!
# !!! adjust_text(texts, arrowprops=dict(arrowstyle='-', color='black', alpha=0, lw=1.5))
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.title('Bivariate plot Ca & Fe - Means - Labels')
plt.show()

# MW_18 labeled
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Fe', data=ComboSplit, hue='Prov')
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Sample[i] == 'MW_18 Head':
        texts.append(
            plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    if ComboSplit.Sample[i] == 'MW_18 Torso':
        texts.append(
            plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
                s=ComboSplit.Sample[i], 
                fontdict=dict(color='black',size=5),
                bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )

    if ComboSplit.Sample[i] == 'MW_18 Base':
        texts.append(
            plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
                s=ComboSplit.Sample[i], 
                fontdict=dict(color='black',size=5),
                bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
# !!! THIS WAS THE BITCH THAT RUINED THE LABELS !!!
# !!! adjust_text(texts, arrowprops=dict(arrowstyle='-', color='black', alpha=0, lw=1.5))
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.title('Bivariate plot Ca & Fe - Means - Labels - Other A = EBA, Other B = Different, Other C = Combo')
plt.show()



# plt.figure(dpi=200)
# sns.scatterplot(x='Zr', y='Cr', data=MeansNoMean1, hue='Prov')
# for i in range(MeansNoMean1.shape[0]):
#     if MeansNoMean1.Prov[i] == 'Other A':
#         texts.append(
#             plt.text(x=MeansNoMean1.Zr[i],y=MeansNoMean1.Cr[i],
#                   s=MeansNoMean1.Sample[i], 
#                   fontdict=dict(color='black',size=5),
#                   bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
#             )
# adjust_text(texts, arrowprops=dict(arrowstyle='-', color='black', alpha=0, lw=1.5))
# plt.title('Bivariate plot Zr & Cr - Limestone/sedimentary vs Basalt/Volcanic')
# plt.show()


# plt.figure(dpi=200)
# sns.scatterplot(x='Zr', y='Cr', data=MeansNoMean1, hue='Prov')
# for i in range(MeansNoMean1.shape[0]):
    # if MeansNoMean1.Prov[i] == 'Other A':
        # texts.append(
            # plt.text(x=MeansNoMean1.Ca[i]+0.1,y=MeansNoMean1.Fe[i]+0.1,
                 # s=MeansNoMean1.Sample[i], 
                 # fontdict=dict(color='black',size=5),
                 # bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            # )
# adjust_text(texts, arrowprops=dict(arrowstyle='-', color='black', alpha=0, lw=1.5))
# plt.title('Bivariate plot Zr & Cr - Means - Labels')
# plt.show()

#using the new csv file with only SLK samples
    # This file also has a "Square" column that indicates the location at SLK
    # This file also has the type of fragment indicated
SLKonlySquares = pd.read_csv('Means - SLK Only.csv')
SLKonlySquares.set_index('Sample', inplace=True)

# Exploring intra-site compositional variation through different variables

#Location
    # for Ca & Fe
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Fe', data=SLKonlySquares, hue='Square')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Location")
plt.title('Ca & Fe - SLK only - hue=location')
plt.show()
    # for Ca & K
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='K', data=SLKonlySquares, hue='Square')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Location")
plt.title('Ca & K - SLK only - hue=location')
plt.show()
    # for Ca & Si
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Si', data=SLKonlySquares, hue='Square')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Location")
plt.title('Ca & Si - SLK only - hue=location')
plt.show()
    # for Fe & Sr
plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Sr', data=SLKonlySquares, hue='Square')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Location")
plt.title('Fe & Sr - SLK only - hue=location')
plt.show()
    # for Si & Mg
plt.figure(dpi=200)
sns.scatterplot(x='Si', y='Mg', data=SLKonlySquares, hue='Square')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Location")
plt.title('Si & Mg - SLK only - hue=location')
plt.show()
    # for Zr & Cr
plt.figure(dpi=200)
sns.scatterplot(x='Zr', y='Cr', data=SLKonlySquares, hue='Square')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Location")
plt.title('Zr & Cr - SLK only - hue=location')
plt.show()



# Typology
    # for Ca & Fe
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Fe', data=SLKonlySquares, hue='Type')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.title('Ca & Fe - SLK only - hue=Type')
plt.show()
    # for Ca & K
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='K', data=SLKonlySquares, hue='Type')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Location")
plt.title('Ca & K - SLK only - hue=Type')
plt.show()
    # for Ca & Si
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Si', data=SLKonlySquares, hue='Type')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Location")
plt.title('Ca & Si - SLK only - hue=Type')
plt.show()
    # for Fe & Sr
plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Sr', data=SLKonlySquares, hue='Type')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.title('Fe & Sr - SLK only - hue=Type')
plt.show()
    # for Si & Mg
plt.figure(dpi=200)
sns.scatterplot(x='Si', y='Mg', data=SLKonlySquares, hue='Type')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.title('Si & Mg - SLK only - hue=Type')
plt.show()
    # for Zr & Cr
plt.figure(dpi=200)
sns.scatterplot(x='Zr', y='Cr', data=SLKonlySquares, hue='Type')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.title('Zr & Cr - SLK only - hue=Type')
plt.show()


# Fragment type
    # for Ca & Fe
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Fe', data=SLKonlySquares, hue='Fragment')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Fragment")
plt.title('Ca & Fe - SLK only - hue=fragment')
plt.show()
    # for Ca & K
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='K', data=SLKonlySquares, hue='Fragment')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Fragment")
plt.title('Ca & K - SLK only - hue=Fragment')
plt.show()
    # for Ca & Si
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Si', data=SLKonlySquares, hue='Fragment')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Fragment")
plt.title('Ca & Si - SLK only - hue=Fragment')
plt.show()
    # for Fe & Sr
plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Sr', data=SLKonlySquares, hue='Fragment')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Fragment")
plt.title('Fe & Sr - SLK only - hue=Fragment')
plt.show()
    # for Si & Mg
plt.figure(dpi=200)
sns.scatterplot(x='Si', y='Mg', data=SLKonlySquares, hue='Fragment')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Fragment")
plt.title('Si & Mg - SLK only - hue=Fragment')
plt.show()
    # for Zr & Cr
plt.figure(dpi=200)
sns.scatterplot(x='Zr', y='Cr', data=SLKonlySquares, hue='Fragment')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Fragment")
plt.title('Zr & Cr - SLK only - hue=Fragment')
plt.show()


# pairplot shows all the possible scatterplots with this dataset in high resolution
# but takes very long to run so left as a comment here
# plt.figure(dpi=200)
# sns.pairplot(SLKonlySquares, diag_kind='hist')
# plt.show()




# !!! This is a copy paste for labels for all points in biplot!!!
# for i in range(len(SLKonlySquares)):
    # plt.text(
        # SLKonlySquares['Ca'].iloc[i], 
        # SLKonlySquares['Fe'].iloc[i], 
        # str(SLKonlySquares.index[i]),
    # )


# Way too late data exploration moment
# Actually seems to not be very useful given the number of variables...
    # And besides, the elements I compare must be justified geochemically so 
    # shouldn't just pick the nice looking graphs
# scatter_matrix(SLKonlySquares, figsize=(8, 8), diagonal='hist')
# plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Fe', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor='black')
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
        texts.append(
            plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    # if ComboSplit.Prov[i] == 'Other B':
    #     texts.append(
    #         plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
    #             s=ComboSplit.Sample[i], 
    #             fontdict=dict(color='black',size=5),
    #             bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            # )
    if ComboSplit.Prov[i] == 'Other C':
        texts.append(
            plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
                s=ComboSplit.Sample[i], 
                fontdict=dict(color='black',size=5),
                bbox=dict(facecolor='white',alpha=0, pad=0.5, edgecolor='none'))
            )
    # if ComboSplit.Prov[i] == 'SLK':
    #     texts.append(
    #         plt.text(x=ComboSplit.Ca[i]+0.1,y=ComboSplit.Fe[i]+0.1,
    #             s=ComboSplit.Sample[i], 
    #             fontdict=dict(color='black',size=5),
    #             bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
    #         )
# !!! THIS WAS THE BITCH THAT RUINED THE LABELS !!!
# !!! adjust_text(texts, arrowprops=dict(arrowstyle='-', color='black', alpha=0, lw=1.5))
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()




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

# ##############
# Adding wt% and ppm columns
# ##############
# converting some trace elements from wt% to ppm
ComboSplit['Cr in ppm'] = ComboSplit['Cr'] * 10000
ComboSplit['V in ppm'] = ComboSplit['V'] * 10000
ComboSplit['Sr in ppm'] = ComboSplit['Sr'] * 10000
ComboSplit['Nb in ppm'] = ComboSplit['Nb'] * 10000
ComboSplit['Zr in ppm'] = ComboSplit['Zr'] * 10000
ComboSplit['Cr_ppm'] = ComboSplit['Cr'] * 10000
ComboSplit['Rb in ppm'] = ComboSplit['Rb'] * 10000
ComboSplit['V_ppm'] = ComboSplit['V'] * 10000




# adding "in wt%" columns to ComboSplit
ComboSplit['Ca in wt%'] = ComboSplit['Ca']
ComboSplit['Si in wt%'] = ComboSplit['Si']
ComboSplit['Fe in wt%'] = ComboSplit['Fe']
ComboSplit['K in wt%'] = ComboSplit['K']
ComboSplit['Al in wt%'] = ComboSplit['Al']
ComboSplit['S in wt%'] = ComboSplit['S']
ComboSplit['P in wt%'] = ComboSplit['P']
ComboSplit['Mg in wt%'] = ComboSplit['Mg']
ComboSplit['Mn in wt%'] = ComboSplit['Mn']

# Creating a new dataframe with means with only SLK & Other as prov
SLKnOther = pd.read_csv('C:/Python/Thesis/Means - SLKnOther.csv')

# converting some trace elements from wt% to ppm - in SLKnOther
SLKnOther['Cr in ppm'] = SLKnOther['Cr'] * 10000
SLKnOther['V in ppm'] = SLKnOther['V'] * 10000
SLKnOther['Sr in ppm'] = SLKnOther['Sr'] * 10000
SLKnOther['Nb in ppm'] = SLKnOther['Nb'] * 10000
SLKnOther['Zr in ppm'] = SLKnOther['Zr'] * 10000

# adding "in wt%" columns to ComboSplit - in SLKnOther
SLKnOther['Ca in wt%'] = SLKnOther['Ca']
SLKnOther['Si in wt%'] = SLKnOther['Si']
SLKnOther['Fe in wt%'] = SLKnOther['Fe']
SLKnOther['K in wt%'] = SLKnOther['K']
SLKnOther['Al in wt%'] = SLKnOther['Al']
SLKnOther['S in wt%'] = SLKnOther['S']
SLKnOther['P in wt%'] = SLKnOther['P']
SLKnOther['Mg in wt%'] = SLKnOther['Mg']
SLKnOther['Mn in wt%'] = SLKnOther['Mn']

SLKonlySquares

# converting some trace elements from wt% to ppm - in SLKnOther
SLKonlySquares['Cr in ppm'] = SLKonlySquares['Cr'] * 10000
SLKonlySquares['V in ppm'] = SLKonlySquares['V'] * 10000
SLKonlySquares['Sr in ppm'] = SLKonlySquares['Sr'] * 10000
SLKonlySquares['Nb in ppm'] = SLKonlySquares['Nb'] * 10000
SLKonlySquares['Zr in ppm'] = SLKonlySquares['Zr'] * 10000
SLKonlySquares['Cr_ppm'] = SLKonlySquares['Cr'] * 10000

# adding "in wt%" columns to ComboSplit - in SLKnOther
SLKonlySquares['Ca in wt%'] = SLKonlySquares['Ca']
SLKonlySquares['Si in wt%'] = SLKonlySquares['Si']
SLKonlySquares['Fe in wt%'] = SLKonlySquares['Fe']
SLKonlySquares['K in wt%'] = SLKonlySquares['K']
SLKonlySquares['Al in wt%'] = SLKonlySquares['Al']
SLKonlySquares['S in wt%'] = SLKonlySquares['S']
SLKonlySquares['P in wt%'] = SLKonlySquares['P']
SLKonlySquares['Mg in wt%'] = SLKonlySquares['Mg']




###############################################################################
# 
# The following are all the plots that looked good from the exploration above this 
# With Labels
# 
###############################################################################

# Mn-Al
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Mn', y='Al', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
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
sns.scatterplot(x='Mn', y='Ca', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
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
sns.scatterplot(x='Cr in ppm', y='Al in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
        texts.append(
            plt.text(x=ComboSplit.Cr_ppm[i],y=ComboSplit.Al[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    if ComboSplit.Prov[i] == 'Other C':
        texts.append(
            plt.text(x=ComboSplit.Cr_ppm[i],y=ComboSplit.Al[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# Cr-K
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='Cr in ppm', y='K in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
        texts.append(
            plt.text(x=ComboSplit.Cr_ppm[i],y=ComboSplit.K[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    if ComboSplit.Prov[i] == 'Other C':
        texts.append(
            plt.text(x=ComboSplit.Cr_ppm[i],y=ComboSplit.K[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# V-Si
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='V in ppm', y='Si in wt%', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
        texts.append(
            plt.text(x=ComboSplit.V_ppm[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    # if ComboSplit.Prov[i] == 'Other C':
    #     texts.append(
    #         plt.text(x=ComboSplit.'V in ppm'[i],y=ComboSplit.'Si in wt%'[i],
    #               s=ComboSplit.Sample[i], 
    #               fontdict=dict(color='black',size=5),
    #               bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
    #         )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()
# S-Fe
#  COULD USE++++++++++++++++++++COULD USE+++++++++++++++++++COULD USE++++++++++
plt.figure(dpi=200)
sns.scatterplot(x='S', y='Fe', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
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
sns.scatterplot(x='S', y='Si', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
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
sns.scatterplot(x='P', y='Al', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
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
sns.scatterplot(x='P', y='Si', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
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
sns.scatterplot(x='Al', y='Fe', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
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
sns.scatterplot(x='Ca', y='Si', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
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
sns.scatterplot(x='Fe', y='K', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
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
sns.scatterplot(x='Fe', y='Si', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
for i in range(ComboSplit.shape[0]):
    if ComboSplit.Prov[i] == 'Other A':
        texts.append(
            plt.text(x=ComboSplit.Fe[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
    if ComboSplit.Prov[i] == 'Other C':
        texts.append(
            plt.text(x=ComboSplit.Fe[i],y=ComboSplit.Si[i],
                  s=ComboSplit.Sample[i], 
                  fontdict=dict(color='black',size=5),
                  bbox=dict(facecolor='white',alpha=0, pad=0.2, edgecolor='none'))
            )
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Type")
plt.show()





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
sns.scatterplot(x='Zr in ppm', y='Rb in ppm', data=ComboSplit, hue='Prov', hue_order=custom_order, edgecolor=('black'))
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Provenance")
plt.show()








# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 18:00:24 2024

@author: maxle
"""
#Importing packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as scp
#PCA plots
from sklearn.decomposition import PCA



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
#MW_7
MW7rows = XRFmeans.loc[['MW_7.1', 'MW_7.2', 'MW_7.3', 'MW_7.4', 'MW_7.5']]
MW7_Av = MW7rows.mean()
XRFmeans.loc['MW_7 Mean'] = MW7_Av
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
#MW_12
MW12rows = XRFmeans.loc[['MW_12.1', 'MW_12.2', 'MW_12.3', 'MW_12.4']]
MW12_Av = MW12rows.mean()
XRFmeans.loc['MW_12 Mean'] = MW12_Av
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
#MW_18
MW18rows = XRFmeans.loc[['MW_18.1', 'MW_18.2', 'MW_18.3', 'MW_18.4']]
MW18_Av = MW18rows.mean()
XRFmeans.loc['MW_18 Mean'] = MW18_Av
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
             'MW_6a Mean', 'MW_6b Mean', 'MW_7 Mean', 'MW_8 Mean', 'MW_9 Mean',
             'MW_10 Mean', 'MW_11a Mean', 'MW_11b Mean', 'MW_12 Mean', 'MW_13 Mean', 
             'MW_14 Mean', 'MW_15 Mean', 'MW_16 Mean', 'MW_17 Mean', 'MW_18 Mean', 
             'MW_19 Mean', 'MW_20 Mean', 'MW_21 Mean', 'MW_22 Mean', 'MW_23 Mean', 
             'MW_24 Mean', 'MW_25 Mean', 'MW_26 Mean', 'MW_27 Mean', 'MW_28 Mean', 
             'MW_29 Mean', 'MW_30 Mean', 'MW_31 Mean', 'MW_32 Mean', 'MW_33 Mean',
             'MW_34 Mean', 'MW_35 Mean', 'MW_36 Mean', 'MW_37 Mean', 'MW_38 Mean',
             'MW_39 Mean', 'MW_40 Mean', 'MW_41 Mean', 'MW_42 Mean', 'MW_43 Mean',
             'MW_44 Mean', 'MW_45 Mean', 'MW_46 Mean', 'MW_47 Mean']]
MeansOnly[ToConvert] = MeansOnly[ToConvert].astype(float)

MeansOnly.to_csv('MeansOnly.csv', float_format='%.4f', index=True)
MeansType = pd.read_csv('C:/Python/Thesis/MeansOnlyTypes.csv')
MeansType.set_index('Sample', inplace=True)
MeansTypeProv = pd.read_csv('C:/Python/Thesis/MeansOnlyTypesProv.csv')
MeansTypeProv.set_index('Sample', inplace=True)




#Bivariate plot for Sedimentair/Vulkanisch - Ca & K/Y/Nb
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='K', data=XRFdata, hue='Prov')
plt.title('Bivariate plot Ca & K - Sedimentair/Vulkanisch')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Y', data=XRFdataZero, hue='Prov')
plt.title('Bivariate plot Ca & Y - Sedimentair/Vulkanisch')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Nb', data=XRFdataZero, hue='Prov')
plt.title('Bivariate plot Ca & Nb - Sedimentair/Vulkanisch')
plt.show()
#Same plots but means instead of all samples
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='K', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Ca & K - Sedimentair/Vulkanisch - Means')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Y', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Ca & Y - Sedimentair/Vulkanisch - Means')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Nb', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Ca & Nb - Sedimentair/Vulkanisch - Means')
plt.show()

#Bivariate plot for Kalkrijk/Vulkanisch - Sr & K/Y/Nb
plt.figure(dpi=200)
sns.scatterplot(x='Sr', y='K', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Ca & K - Sedimentair/Vulkanisch')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='Sr', y='Y', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Ca & Y - Sedimentair/Vulkanisch')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='Sr', y='Nb', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Ca & Nb - Sedimentair/Vulkanisch')
plt.show()
#Same plots but means instead of all samples
plt.figure(dpi=200)
sns.scatterplot(x='Sr', y='K', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Ca & K - Sedimentair/Vulkanisch')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='Sr', y='Y', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Ca & Y - Sedimentair/Vulkanisch')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='Sr', y='Nb', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Ca & Nb - Sedimentair/Vulkanisch')
plt.show()







#Bivariate plot for Ca & Sr (Sr outliers removed)
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Sr', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Ca & Sr')
plt.show()


plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Y', data=XRFdataZero, hue='Prov')
plt.title('Bivariate plot Ca & Y')
plt.show()


#Calcium, itrium, kalium, ijzer, zirkoon, niobium, rubidium 
#Vooral calcium-kalium












plt.figure(dpi=200)
sns.scatterplot(x='Si', y='Fe', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Si & Fe')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='Si', y='Al', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Si & Al')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='Si', y='Ca', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Si & Al')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='Fe', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Si & Al')
plt.show()



### Trying to make a dendrogram
from scipy.cluster.hierarchy import linkage, dendrogram

XRFdendro = XRFdataZero.copy()
XRFdendro.set_index('Sample', inplace=True)
XRFdendro.drop(columns=['DateTime', 'Operator', 'Material','Project', 
                        'User', 'Type', 'Application', 'Method', 
                        'ElapsedTime', 'U', 'Multiplier', 'Cal Check', 'Prov', 
                        'File #'], inplace=True)

linked = linkage(XRFdendro, method='ward')

plt.figure(figsize=(14, 8), dpi=200)
dendrogram(linked, labels=XRFdendro.index.tolist(), leaf_rotation=90, 
           leaf_font_size=6)
plt.title("Dendrogram: Linkage Method='ward'")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
plt.show()

#-----------------------------------------------

linkedSingle1 = linkage(XRFdendro, method='single')

plt.figure(figsize=(14, 8), dpi=200)
dendrogram(linkedSingle1, labels=XRFdendro.index.tolist(), leaf_rotation=90, 
           leaf_font_size=6)
plt.title("Dendrogram: Linkage Method='single'")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
plt.show()

#-----------------------------------------------

linkedComplete1 = linkage(XRFdendro, method='complete')

plt.figure(figsize=(14, 8), dpi=200)
dendrogram(linkedComplete1, labels=XRFdendro.index.tolist(), leaf_rotation=90, 
           leaf_font_size=6)
plt.title("Dendrogram: Linkage Method='complete'")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
plt.show()

#-----------------------------------------------

linkedAverage1 = linkage(XRFdendro, method='average')

plt.figure(figsize=(14, 8), dpi=200)
dendrogram(linkedAverage1, labels=XRFdendro.index.tolist(), leaf_rotation=90, 
           leaf_font_size=6)
plt.title("Dendrogram: Linkage Method='average'")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
plt.show()






###############################################################################
#DendroSamples = XRFdendro['Sample'].valuesXRFdendro.drop(columns=['DateTime', 'Operator', 'Sample', 'Material','Project', 
#                        'User', 'Type', 'Date', 'Application', 'Method', 
#                        'ElapsedTime', 'U', 'Multiplier', 'Cal Check', 'Prov', 
#                        'File #'], 
#               inplace=True)
#
#linked = linkage(XRFdendro, method='ward')
#
#plt.figure(figsize=(14, 8), dpi=200)
#dendrogram(linked, labels=XRFdendro.index.tolist(), leaf_rotation=90, 
#           leaf_font_size=6)
#plt.title("Dendrogram Test 1")
#plt.xlabel("Sample Index")
#plt.ylabel("Distance")
#plt.show()
###############################################################################


XRFdendro2 = XRFdataZero.copy()
XRFdendro2.set_index('Prov', inplace=True)
XRFdendro2.drop(columns=['DateTime', 'Operator', 'Material','Project', 
                        'User', 'Type', 'Application', 'Method', 
                        'ElapsedTime', 'U', 'Multiplier', 'Cal Check', 'Sample', 
                        'File #'], inplace=True)

linkedWard = linkage(XRFdendro2, method='ward')

plt.figure(figsize=(14, 8), dpi=200)
dendrogram(linkedWard, labels=XRFdendro2.index.tolist(), leaf_rotation=90, 
           leaf_font_size=6)
plt.title("Dendrogram: Linkage Method='ward'")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
plt.show()

#-----------------------------------------------

linkedSingle = linkage(XRFdendro2, method='single')

plt.figure(figsize=(14, 8), dpi=200)
dendrogram(linkedSingle, labels=XRFdendro2.index.tolist(), leaf_rotation=90, 
           leaf_font_size=6)
plt.title("Dendrogram: Linkage Method='single'")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
plt.show()

#-----------------------------------------------

linkedComplete = linkage(XRFdendro2, method='complete')

plt.figure(figsize=(14, 8), dpi=200)
dendrogram(linkedComplete, labels=XRFdendro2.index.tolist(), leaf_rotation=90, 
           leaf_font_size=6)
plt.title("Dendrogram: Linkage Method='complete'")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
plt.show()

#-----------------------------------------------

linkedAverage = linkage(XRFdendro2, method='average')

plt.figure(figsize=(14, 8), dpi=200)
dendrogram(linkedAverage, labels=XRFdendro2.index.tolist(), leaf_rotation=90, 
           leaf_font_size=6)
plt.title("Dendrogram: Linkage Method='average'")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
plt.show()

#-----------------------------------------------

###############################################################################
#
#
#      Choosing the Linkage Method: You can experiment with different linkage
#      methods like 'single', 'complete', or 'average' to see how they affect
#      the dendrogram.
#
#
###############################################################################



#MeansOnly - Average
linkedMeansAverage = linkage(MeansOnly, method='average')
plt.figure(figsize=(14, 8), dpi=200)
dendrogram(linkedMeansAverage, labels=MeansOnly.index.tolist(), leaf_rotation=90, 
           leaf_font_size=6)
plt.title("Dendrogram: Linkage Method='average' - Means")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
plt.show()

#MeansOnly - Complete
linkedMeansComplete = linkage(MeansOnly, method='complete')
plt.figure(figsize=(14, 8), dpi=200)
dendrogram(linkedMeansComplete, labels=MeansOnly.index.tolist(), leaf_rotation=90, 
           leaf_font_size=6)
plt.title("Dendrogram: Linkage Method='Complete' - Means")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
plt.show()

#MeansOnly - Ward
linkedMeansWard = linkage(MeansOnly, method='ward')
plt.figure(figsize=(14, 8), dpi=200)
dendrogram(linkedMeansWard, labels=MeansOnly.index.tolist(), leaf_rotation=90, 
           leaf_font_size=6)
plt.title("Dendrogram: Linkage Method='Complete' - Ward")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
plt.show()











#### TEST TEST \/\/\/\/ This should normalize the data!! -> ternary?
#ToNorm = ['Na', 'Al', 'Cl', 'V', 'Co', 'Ga', 'As', 'Se', 'Rb', 'Y', 'Zr', 
#             'Nb', 'Mo', 'Ba', 'Pb', 'Th']
#XRFdataZero_Norm=XRFdataZero.copy()
#XRFdataZero_RowSums = XRFdataZero_Norm[ToNorm].sum(axis=1)
#XRFdataZero_Norm[ToNorm] = XRFdataZero[ToNorm].div(XRFdataZero_RowSums, axis=0)
### This did not actually normalize the data at all!!!!!


### SHITTY ATTEMPTS AT TERNARY PLOT BUT THE DATA ISNT NORMALIZED...
#figure, tax = ternary.figure(scale=1.0)  # Scale is 1 for normalized data
#tax.set_title("Ternary Plot Test")
#
#tax.scatter(XRFdataZero_Norm[['Ca', 'Sr', 'K']].values, marker='o', color='b', 
#            label='Data Points')
#
#tax.left_axis_label("Ca", fontsize=12)
#tax.right_axis_label("Sr", fontsize=12)
#tax.bottom_axis_label("K", fontsize=12)
#
#tax.boundary
#
#plt.show()
### SOAJDBAKSJDBAKSJDBASKDJBASDASFDASDLFJSDFLKGJBSLDGKJBDSFG ###






#MW_6 = XRFdataZero['MW_6a.1', 'MW_6a.2', 'MW_6a.3', 'MW_6a.4', 'MW_6b.1']









###########Thorium Jail##############################################
## plt.figure(dpi=200)                                             ##
## sns.scatterplot(x='Fe', y='Th', data=XRFdataZero, hue='Prov')   ##
## plt.title('Bivariate plot Fe & Th')                             ##
## plt.show()                                                      ##
#####################################################################


plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Rb', data=XRFdataZero, hue='Prov')
plt.title('Bivariate plot Fe & Rb')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Sr', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Fe & Sr')
plt.show()




plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Y', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Fe & Y')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Zr', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Fe & Zr')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Nb', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Fe & Nb')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='K', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Fe & K')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Ti', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Fe & Ti')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Si', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Fe & Si')
plt.show()



#Same plots but with the means

############Thorium Jail#############################################
## plt.figure(dpi=200)                                             ##
## sns.scatterplot(x='Fe', y='Th', data=MeansTypeProv, hue='Prov') ##
## plt.title('Bivariate plot Fe & Th - Means'                      ##
## plt.show()                                                      ##
#####################################################################


plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Rb', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Fe & Rb - Means')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Sr', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Fe & Sr - Means')
plt.show()




plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Y', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Fe & Y - Means')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Zr', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Fe & Zr - Means')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Nb', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Fe & Nb - Means')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='K', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Fe & K - Means')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Ti', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Fe & Ti - Means')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Si', data=MeansTypeProv, hue='Type')
plt.subplots_adjust(right=0.8)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.title('Bivariate plot Fe & Si - Means - Type Types')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Si', data=MeansTypeProv, hue='Type')
plt.subplots_adjust(right=0.8)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.title('Bivariate plot Fe & Si - Means - Arm Types')
plt.show()







##########
## Arms instead of Prov
##########

plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Si', data=MeansTypeProv, hue='Arms')
plt.subplots_adjust(right=0.8)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.title('Bivariate plot Fe & Si - Means - Arm Types')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Th', data=MeansTypeProv, hue='Arms')
plt.title('Bivariate plot Fe & Th - Means')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Rb', data=MeansTypeProv, hue='Arms')
plt.title('Bivariate plot Fe & Rb - Means')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Sr', data=MeansTypeProv, hue='Arms')
plt.title('Bivariate plot Fe & Sr - Means')
plt.show()




plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Y', data=MeansTypeProv, hue='Arms')
plt.title('Bivariate plot Fe & Y - Means')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Zr', data=MeansTypeProv, hue='Arms')
plt.title('Bivariate plot Fe & Zr - Means')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Nb', data=MeansTypeProv, hue='Arms')
plt.title('Bivariate plot Fe & Nb - Means')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='K', data=MeansTypeProv, hue='Arms')
plt.title('Bivariate plot Fe & K - Means')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Ti', data=MeansTypeProv, hue='Arms')
plt.title('Bivariate plot Fe & Ti - Means')
plt.show()



##########
## All samples with Arms types
##########

plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Si', data=XRFdata_ArmsZero, hue='Arms')
plt.subplots_adjust(right=0.8)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
plt.title('Bivariate plot Fe & Si')
plt.show()


###########Thorium Jail###################################################
## plt.figure(dpi=200)                                                  ##
## sns.scatterplot(x='Fe', y='Th', data=XRFdata_ArmsZero, hue='Arms')   ##
## plt.title('Bivariate plot Fe & Th - Means')                          ##
## plt.show()                                                           ##
##########################################################################


plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Rb', data=XRFdata_ArmsZero, hue='Arms')
plt.title('Bivariate plot Fe & Rb')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Sr', data=XRFdata_NoSr, hue='Arms')
plt.title('Bivariate plot Fe & Sr')
plt.show()




plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Y', data=XRFdata_ArmsZero, hue='Arms')
plt.title('Bivariate plot Fe & Y')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Zr', data=XRFdata_ArmsZero, hue='Arms')
plt.title('Bivariate plot Fe & Zr')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Nb', data=XRFdata_ArmsZero, hue='Arms')
plt.title('Bivariate plot Fe & Nb')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='K', data=XRFdata_ArmsZero, hue='Arms')
plt.title('Bivariate plot Fe & K')
plt.show()



plt.figure(dpi=200)
sns.scatterplot(x='Fe', y='Ti', data=XRFdata_ArmsZero, hue='Arms')
plt.title('Bivariate plot Fe & Ti')
plt.show()






## Looking to see if there is a relationship to be found when looking only at
## proxies for volcanic material

# First with all samples
plt.figure(dpi=200)
sns.scatterplot(x='K', y='Nb', data=XRFdata_ArmsZero, hue='Prov')
plt.title('Bivariate plot K & Nb')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='K', y='Y', data=XRFdata_ArmsZero, hue='Prov')
plt.title('Bivariate plot K & Y')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='Y', y='Nb', data=XRFdata_ArmsZero, hue='Prov')
plt.title('Bivariate plot Y & Nb')
plt.show()

# Then with the means only
plt.figure(dpi=200)
sns.scatterplot(x='K', y='Nb', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot K & Nb - Means')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='K', y='Y', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot K & Y - Means')
plt.show()

plt.figure(dpi=200)
sns.scatterplot(x='Y', y='Nb', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Y & Nb - Means')
plt.show()


## Looking at the relationship between volcanic marker (K) and
## sedimentary marker (Ca)

# First with all samples
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='K', data=XRFdata_ArmsZero, hue='Prov')
plt.title('Bivariate plot Ca & K')
plt.show()
# Then with means only
plt.figure(dpi=200)
sns.scatterplot(x='Ca', y='K', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Ca & K - Means')
plt.show()


## Looking at the relationship between volcanic marker (Sr) and
## sedimentary marker (Nb)

# First with all samples
plt.figure(dpi=200)
sns.scatterplot(x='Sr', y='Nb', data=XRFdata_NoSr, hue='Prov')
plt.title('Bivariate plot Sr & Nb')
plt.show()
# Then with means only
Means_NoSr = MeansTypeProv.drop(['MW_22 Mean'])
plt.figure(dpi=200)
sns.scatterplot(x='Sr', y='Nb', data=Means_NoSr, hue='Prov')
plt.title('Bivariate plot Sr & Nb - Means')
plt.show()


## Looking at the relationship between volcanic marker (Ba) and
## sedimentary marker (Y)

# First with all samples
plt.figure(dpi=200)
sns.scatterplot(x='Ba', y='Y', data=XRFdata_ArmsZero, hue='Prov')
plt.title('Bivariate plot Ba & Y')
plt.show()
# Then with means only
plt.figure(dpi=200)
sns.scatterplot(x='Ba', y='Y', data=MeansTypeProv, hue='Prov')
plt.title('Bivariate plot Ba & Y - Means')
plt.show()













# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 20:01:22 2020

@author: CC
混淆矩阵和热力图
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
sns.set()

def heatmap():    
    df1 = pd.read_csv('1.csv',header=None)
    df1 = df1.loc[:12,:12].astype('int32')
    print(df1)
    # Draw a heatmap with the numeric values in each cell
    f, ax = plt.subplots(figsize=(12,8 ))
    sns.heatmap(df1, annot=True, fmt="d", ax=ax,cmap='gray_r')
    ax.set_xlabel('predict') #x轴
    ax.set_ylabel('true') #y轴

def confuse():
    sns.set()
    f,ax=plt.subplots()
    
    y_true = [1,0,1,0]
    y_pred = [1,1,0,1]
    C2= confusion_matrix(y_true, y_pred, labels=list(range(2)))
    print(C2) #打印出来看看
    
    plt.figure(figsize=(12,8),dpi=400)
    sns.heatmap(C2,annot=True,annot_kws={'size':10},ax=ax) #画热力图
    
    ax.set_title('confusion matrix') #标题
    ax.set_xlabel('predict') #x轴
    ax.set_ylabel('true') #y轴

#confuse()
heatmap()    


'''
1.csv:
13287	41	287	145	91	23	12	657	13	317	34	9	5135
78942	114983	1129	53	432	9	3	3249	132	704	535	735	4524
423	3013	132075	27	98	12	8	14242	6244	579	715	4531	432
20128	7122	7813	78246	96	32	15	19790	4252	6243	252	8747	87
23732	2134	65	64234	125711	82	23	14096	3214	5913	931	12843	345
488	890	981	87	10321	22581	34	4567	9758	26536	562	36554	64
3712	792	129	16	10512	38012	142689	4758	4845	24529	8256	4345	1324
53	1728	732	3	423	31832	3313	31285	9234	30513	45256	9587	64321
2344	82	402	151	345	41289	2109	20978	91227	18347	36135	4326	32713
3414	6341	1183	783	326	10830	542	28906	4398	27843	24523	9857	10343
277	7318	2983	1167	144	4712	646	4766	7123	5243	20807	10942	20142
896	2012	2067	4673	876	320	341	1780	7917	1823	11635	44382	636
2304	3544	154	415	625	266	265	926	1643	1410	359	3142	9934

cmap:
    Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r,
    CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, 
    Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, 
    Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r,
    PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy,
    RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1,
    Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, 
    YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, 
    afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr,
    bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r,
    cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, 
    gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow,
    gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot,
    gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r,
    icefire, icefire_r, inferno, inferno_r, jet, jet_r, magma, magma_r, mako,
    mako_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma,
    plasma_r, prism, prism_r, rainbow, rainbow_r, rocket, rocket_r, seismic,
    seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, 
    tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, twilight, twilight_r,
    twilight_shifted, twilight_shifted_r, viridis, viridis_r, vlag, vlag_r,
    winter, winter_r


'''

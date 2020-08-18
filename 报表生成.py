# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:49:26 2020

@author: CC
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import uuid
import os
import shutil

class MonthAnalysis():
    def __init__(self,data):
        self.data = data
        self.shape = self.data.shape
        self.doneData = self.data[self.data['完成情况'] == '完成']
        self.undoData = self.data[self.data['完成情况'] == '未完成']
        
    def count(self):
        '''
        返回【总任务数】，即本月任务量
        '''
        return len(self.data)
    
    def doneAndUndo(self):
        '''
        返回【完成情况】,已做工作和未完成工作
        '''
        return self.data['完成情况'].value_counts().sort_values()
    
    def task(self):
        '''
        返回【每个人工作量】，包含完成和未完成
        '''
        return self.data['任务指派'].value_counts().sort_values()
    
    def done(self):
        '''
        返回【已完成任务的每人数量】
        '''
        return self.doneData['任务指派'].value_counts().sort_values()
    
    def undo(self):
        '''
        返回【未完成任务的每人数量】
        '''
        return self.undoData['任务指派'].value_counts().sort_values()
    
    def doneTop5(self):
        '''
        返回【前5花费时间的完成任务】
        '''
        return self.doneData[['任务名称','进度天数']].sort_values(by='进度天数').head()
    
    def doneEnd5(self):
        '''
        返回【后5花费时间的完成任务】
        '''
        return self.doneData[['任务名称','进度天数']].sort_values(by='进度天数').tail()
    
    def undoTop5(self):
        '''
        返回【前5花费时间的未完成任务】
        '''
        return self.undoData[['任务名称','进度天数']].sort_values(by='进度天数').head()
    
    def undoEnd5(self):
        '''
        返回【后5花费时间的未完成任务】
        '''
        return self.undoData[['任务名称','进度天数']].sort_values(by='进度天数').tail()

    def doneMaxTime(self):
        '''
        返回【已完成任务的最多次数的天数】
        '''
        doneMaxTime = self.doneData['进度天数'].value_counts()
        m = doneMaxTime.max()
        return doneMaxTime[doneMaxTime.values == m].index

    def doneDay(self):
        '''
        返回【已完成任务天数分布】
        '''
        return self.doneData['进度天数'].value_counts()

    def undoDay(self):
        '''
        返回【未完成任务天数分布】
        '''
        return self.undoData['进度天数'].value_counts()

# monthAnalysis = MonthAnalysis(Data)
# count = monthAnalysis.count()
# doneAndUndo = monthAnalysis.doneAndUndo()
# task = monthAnalysis.task()
# done = monthAnalysis.done()
# undo = monthAnalysis.undo()
# doneTop5 = monthAnalysis.doneTop5()
# doneEnd5 = monthAnalysis.doneEnd5()
# undoTop5 = monthAnalysis.undoTop5()
# undoEnd5 = monthAnalysis.undoEnd5()
# doneMaxTime = monthAnalysis.doneMaxTime()
# doneDay = monthAnalysis.doneDay()
# undoDay = monthAnalysis.undoDay()

sns.set_style('ticks',{'font.sans-serif':['simhei','Arial']})

def saveFig(func):
    def save():
        plt.cla()
        func()
        id = str(uuid.uuid1())
        imagelist.append(id+'.jpg')
        plt.savefig('image/'+ id +'.jpg',dpi=400,bbox_inches = 'tight')

        return func()
    return save

@saveFig
def plotSumDis():
    data = monthAnalysis.data
    sns.catplot(x="任务指派", y="进度天数", data=data)
    plt.title('总任务进度分布')

@saveFig
def plotDoneDis():
    data = monthAnalysis.doneData
    sns.catplot(x="任务指派", y="进度天数", data=data)
    plt.title('已完成任务进度分布')

@saveFig
def plotUndoDis():
    data = monthAnalysis.undoData
    sns.catplot(x="任务指派", y="进度天数", data=data)
    plt.title('未完成任务进度分布')

@saveFig
def plotPie():
    labels = ['已完成','未完成']
    sizes = [len(monthAnalysis.doneData),len(monthAnalysis.undoData)]
    explode = (0, 0.1)
    colors = ['#ffa23e', '#4B709A',]
    plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
            colors=colors, shadow=False, startangle=300,
            textprops= {'fontsize':16,'color':'black'})
    plt.title("完成情况")

@saveFig
def plotDoneAndUndo():
    data = monthAnalysis.doneAndUndo()
    data_array = pd.DataFrame(np.transpose(np.array([data.index.values,data.values])),columns=('完成类别','数量'))
    sns.barplot(x='完成类别', y='数量', palette="ch:.25",data=data_array)
    plt.title('完成情况')

@saveFig
def plotTask():
    data = monthAnalysis.task()
    data_array = pd.DataFrame(np.transpose(np.array([data.index.values, data.values])), columns=('任务人', '数量'))
    sns.barplot(x='任务人', y='数量', palette="ch:.25", data=data_array)
    plt.title('每人任务')

@saveFig
def plotDone():
    data = monthAnalysis.done()
    data_array = pd.DataFrame(np.transpose(np.array([data.index.values, data.values])), columns=('任务人', '数量'))
    sns.barplot(x='任务人', y='数量', palette="ch:.25", data=data_array)
    plt.title('每人已完成任务')

@saveFig
def plotUodo():
    data = monthAnalysis.undo()
    data_array = pd.DataFrame(np.transpose(np.array([data.index.values, data.values])), columns=('任务人', '数量'))
    sns.barplot(x='任务人', y='数量', palette="ch:.25", data=data_array)
    plt.title('每人未完成任务')

@saveFig
def plotDoneTop5():
    data = monthAnalysis.doneTop5()
    sns.barplot(x='任务名称', y='进度天数', palette="ch:.25", data=data).set_xticklabels(labels=data['任务名称'],
               rotation=45)
    plt.title('完成任务耗时最短TOP5')

@saveFig
def plotDoneEnd5():
    data = monthAnalysis.doneEnd5()
    sns.barplot(x='任务名称', y='进度天数', palette="ch:.25", data=data).set_xticklabels(labels=data['任务名称'], rotation=45)
    plt.title('完成任务耗时最长TOP5')

@saveFig
def plotUndoTop5():
    data = monthAnalysis.undoTop5()
    sns.barplot(x='任务名称', y='进度天数', palette="ch:.25", data=data).set_xticklabels(labels=data['任务名称'], rotation=45)
    plt.title('未完成任务耗时最短TOP5')

@saveFig
def plotUndoEnd5():
    data = monthAnalysis.undoEnd5()
    sns.barplot(x='任务名称', y='进度天数', palette="ch:.25", data=data).set_xticklabels(labels=data['任务名称'], rotation=45)
    plt.title('未完成任务耗时最长TOP5')

@saveFig
def plotDoneDay():
    data = monthAnalysis.doneDay()
    data_array = pd.DataFrame(np.transpose(np.array([data.index.values, data.values])),
                              columns=('天数', '数量')).sort_values(by='天数')
    sns.barplot(x='天数', y='数量', palette="ch:.25", data=data_array)
    plt.title('完成任务天数分布')

@saveFig
def plotUndoDay():
    data = monthAnalysis.undoDay()
    data_array = pd.DataFrame(np.transpose(np.array([data.index.values, data.values])),
                              columns=('天数', '数量')).sort_values(by='天数')
    sns.barplot(x='天数', y='数量', palette="ch:.25", data=data_array)
    plt.title('未完成任务天数分布')

# plotSumDis()
# plotDoneDis()
# plotUndoDis()
# plotPie()
# plotDoneAndUndo()
# plotTask()
# plotDone()
# plotUodo()
# plotDoneTop5()
# plotDoneEnd5()
# plotUndoTop5()
# plotUndoEnd5()
# plotDoneDay()
# plotUndoDay()


def markdown(MonthName,imagelist):
    markdown = '''
    <h1>{}工作情况分析报表</h1>
    <div align="center">
    '''.format(MonthName)

    for i,j in enumerate(imagelist):
        if i % 2 == 0:
            markdown += '<hr>\n'
        markdown += '<img src="image/{}" width=40% alt=""> \n'.format(j)
    markdown += '</div>'

    with open('{}工作报表.md'.format(MonthName),'a') as f:
        f.write(markdown)
    shutil.copyfile('{}工作报表.md'.format(MonthName),'{}工作报表.html'.format(MonthName))
    print('报表生成成功---MarkDown和HTML')

if __name__ == "__main__":
    FileName = '任务序号.xlsx'
    MonthName = '8月'
    try:
        os.mkdir('image')
    except:
        pass

    imagelist = []
    Data = pd.read_excel(FileName, sheet_name=MonthName, usecols='A:I')
    monthAnalysis = MonthAnalysis(Data)

    list = ['plotSumDis()',
            'plotDoneDis()',
            'plotUndoDis()',
            'plotPie()',
            'plotDoneAndUndo()',
            'plotTask()',
            'plotDone()',
            'plotUodo()',
            'plotDoneTop5()',
            'plotDoneEnd5()',
            'plotUndoTop5()',
            'plotUndoEnd5()',
            'plotDoneDay()',
            'plotUndoDay()',
            ]
    for i in list:
        exec(i)
    markdown(MonthName,imagelist)

import os
import numpy as np
import pandas as pd


def find_csv(find_path):
    filename_path_list = []
    for dirpaths ,dirnames ,filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.csv'):
                filename_path_list.append(dirpaths + '\\' + filename)
    return filename_path_list

def get_ass(path):
    data = pd.read_csv(path,encoding='gb18030')
    return data

def init_matrix(path):
    list_name = pd.Series()
    for file_path in find_csv(path):
        
        data = get_ass(file_path)
        list_name = list_name.append(data.drop_duplicates(['subject'])['subject'],ignore_index=True)
         
    list_name = list_name.drop_duplicates()
    Matrix_tmp = pd.DataFrame(0,columns=list_name,index=list_name)
    return Matrix_tmp
 

if __name__ == '__main__':
    #--------------------Configuration--Start--------------------------
    path = 'C:\\Users\\cc_lo\\Desktop\\result\\DedeCms_attack'
    file_name = 'DedeCms_attack.csv' #Resin_viewfile_attack/DedeCms_attack

    pd.set_option('display.max_columns',None) #df输出显示所有列
    #--------------------Configuration---End---------------------------

    Matrix_tmp = init_matrix(path) #初始化一个全为0的矩阵
    
    for file_path in find_csv(path):
        data = get_ass(file_path)
        for indexs in data.index[0:-1]:
            rows_f = data.loc[indexs].values[0:-1]
            fT = rows_f[30] #subject,30,告警类型
            rows_n = data.loc[indexs+1].values[0:-1]
            nT = rows_n[30]
            Matrix_tmp[nT][fT] = Matrix_tmp[nT][fT] + 1
    
    Matrix_P = Matrix_tmp.div((Matrix_tmp.apply(sum,axis=1)),axis=0).fillna(0)

    #Matrix_P.to_csv(file_name,index=True,header=True) #csv输出有误
    #np.savetxt(file_name,Matrix_P,fmt="%.2f",delimiter=",")
    print (Matrix_tmp)
    

    
    
        
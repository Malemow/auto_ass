import os
import shutil
import pathlib
from os import walk 
from os.path import join

#抓取目前根目錄所有檔案 與目前路徑是否有相同部分

int_error = 0
pt_Print =  '/Volumes/FileServer2/water box/'
for root,dirs,files in walk(pt_Print + '卡典集散區' ):
  for i in files:
    pt_fider  = join(root , i) #獲取檔案路徑
    pt_files  = pathlib.Path(pt_fider)
    pt_name   = pt_files.name  #獲取檔案名稱
    pt_suffix = pt_files.suffix #獲取檔案副檔名
    pt_name_  = pt_name[0: 6] #抓取檔案名稱前6位
    pt_chreck = pt_name[8] #檢查位
    dir_name  = '#' + pt_name_ + '00' #把抓取的檔案名稱 前方加上# 後面加上 00
    suffix    = ['.pdf' , '.PDF'  ,'.eps' , 'EPS' , '.ai' , '.AI']  #把副檔名 定義為suffix方便檢視

    #辨識副檔名

    if pt_suffix in suffix and pt_chreck in "-" :
      int_mon   = int(pt_name[2:4])
      dir_mon   = str(int_mon)
      int_yers  = int(pt_name[0:2]) +89
      dir_yers  = '#' + str(+ int_yers)

      if not os.path.exists(pt_Print + dir_yers + '年'): #辨識此目錄是否有此年份
        os.mkdir(pt_Print + dir_yers + '年')
      if not os.path.exists(pt_Print + dir_yers + '年/' + dir_mon + '月'): #辨識此目錄是否有此月份
        os.mkdir(pt_Print + dir_yers + '年/' + dir_mon + '月')     
      shutil.move(pt_fider,pt_Print + dir_yers + '年/' + dir_mon + '月/'  + pt_name )

      print ('成功將', pt_name , '移動至', dir_mon + '月資料夾')
             
    elif not pt_suffix in '.DS_Store' and not pt_name[0] in '#':
      int_error = int_error+1
print("有"+ str(int_error) +"個檔案需移除")
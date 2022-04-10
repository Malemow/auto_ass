import os
import shutil
import pathlib
from os import walk 
from os.path import join

#抓取目前根目錄所有檔案 與目前路徑是否有相同部分
int_path  = 0 #檢測已丟幾個檔案
int_error = 0 #檢測需幾個檔案移除ㄈ

Tg_dirs = str('##圖檔集散地')

Pt_Print  = pathlib.Path(__file__) #抓取執行檔檔案資料
Pt_fider  = Pt_Print.parent #抓取執行檔父資料夾
_Pt_fider = str(Pt_fider) + '/'  #讓他可使用在os函數
ck_dirs_lonth =len(str(Pt_fider)) - len(str(Tg_dirs)) 
_ck_dirs = str(Pt_fider)[ck_dirs_lonth:]

if Tg_dirs in _ck_dirs :
  for root,dirs,files in walk(Pt_fider): #執行此路徑內所有檔案
    for i in files:
      pt_fider  = join(root , i) #獲取檔案路徑
      pt_files  = pathlib.Path(pt_fider) #取得檔案資料
      pt_name   = pt_files.name  #獲取檔案名稱
      pt_suffix = pt_files.suffix #獲取檔案副檔名
      pt_name_  = pt_name[0: 6] #抓取檔案名稱前6位
      ck_fils   = pt_name[8] #檢查位
      dir_name  = '#' + pt_name_ + '00' #把抓取的檔案名稱 前方加上# 後面加上 00
      suffix    = ['.pdf' , '.PDF'  ,'.tiff' ,'.TIFF' , '.tif' , 'TIF']  #把副檔名 定義為suffix方便檢視

      if pt_suffix in suffix and ck_fils in "-" : #辨識副檔名 #檢查第9位是否為'-'符號
        #抓取年份,月份
        int_mon   = int(pt_name[2:4])
        dir_mon   = str(int_mon)
        int_yers  = int(pt_name[0:2]) +89
        dir_yers  = '#' + str(int_yers)

        if not os.path.exists(_Pt_fider + '../' + dir_yers + '年'): #辨識此目錄是否有此年份
          os.mkdir(_Pt_fider + '../' + dir_yers + '年')
        if not os.path.exists(_Pt_fider + '../' + dir_yers + '年/' + dir_mon + '月'): #辨識此目錄是否有此月份
          os.mkdir(_Pt_fider + '../' + dir_yers + '年/' + dir_mon + '月')     
        if not os.path.exists(_Pt_fider + dir_yers + '年/' + dir_mon + '月/' + dir_name): #辨識此目錄是否有此單號資料夾
          os.mkdir(_Pt_fider + '../' + dir_yers + '年/' + dir_mon + '月/' + dir_name)
          shutil.move(pt_fider,_Pt_fider + '../' + dir_yers + '年/' + dir_mon + '月/' + dir_name + '/' + pt_name ) #移動檔案到此單號資料夾

        print ('成功將', pt_name , '移動至', dir_yers , '年' ,dir_mon , '月資料夾')
        int_path = int_path + 1

        #排除.Ds_Store檔案 #排除第一位字串為'#'檔案
      elif not pt_suffix in '.DS_Store' and not pt_name[0] in '#':
        int_error = int_error+1  

  print("有"+ str(int_path)  +"個檔案已處理")
  print("有"+ str(int_error) +"個檔案需移除")
else:
  print('檔案錯誤,請丟進指定資料夾')
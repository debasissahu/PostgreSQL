import pandas as pd;
import json;
from glob import glob;
import os;
from shutil import copyfile;

#----Global Data Veriable
recipes_data=pd.DataFrame();
ingridiant_data=pd.DataFrame(columns=["rcp_id","label","qty"]);
#---Read All JSON Files;
json_file_array=glob('D:\\data_processing\\ritesh_bawri_app_data\\raw_files\\recipes\\*.json');

error_ffile_loc="D:\\data_processing\\ritesh_bawri_app_data\\error_files\\recipes";
processed_files="D:\\data_processing\\ritesh_bawri_app_data\\processed_files\\recipes";


#---Manipulate Data
for path in json_file_array:    
    try:
        #File Open
        file=open(path);
        json_data=json.load(file);  
        file.close();
        chk=True;
        try:
            #Ingridient Data
            temp_df=pd.DataFrame(columns=["rcp_id","label","qty"]);
            temp_df=temp_df.append(json_data["ingredientsSimplified"],ignore_index=True);
            temp_df["rcp_id"]=json_data["_id"];
            for zz in range(0,len(temp_df["selectedPortion"])):    
                temp_df['label'][zz]=(temp_df["selectedPortion"][zz])['label'];
                temp_df['qty'][zz]=(temp_df["selectedPortion"][zz])['qty'];
            
            ing_filed=['rcp_id', 'label', 'qty', '_id', 'alias','selectedMeasure', 'dataSource', 'nutriAdminId', 'group'];
            ingridiant_data=ingridiant_data.append(temp_df[ing_filed],ignore_index=True);
        except:
            print ("Ingridient:"+path); 
            chk=False;
        
        if(chk):
            try:
                #Reciepes Data
                rcp_column=['_type', '_id', 'updatedAt', 'createdAt', 'title', 'name', 'image', 'sourceUrl', 'instructions', 'servings', 'readyInMins', 'comments', 'dataSource', 'userId', '__v', 'category', 'oldRecipeId'];
                temp_df=pd.DataFrame(columns=rcp_column);
                temp_df=temp_df.append(json_data,ignore_index=True);            
                temp_df=temp_df[rcp_column];
                recipes_data=recipes_data.append(temp_df,ignore_index=True);
                os.system('move "'+path+'" "'+processed_files+'"');
            except:
                print ("Reciepes:"+path);
                os.system('move "'+path+'" "'+error_ffile_loc+'"');
        else:
            os.system('move "'+path+'" "'+error_ffile_loc+'"');
                        
    except:
        print ("File Open:"+path);  
        os.system('move "'+path+'" "'+error_ffile_loc+'"');
    
#--- Save File
save_location="D:\\data_processing\\ritesh_bawri_app_data\\final_output\\";
recipes_data.to_csv(save_location+'all_recipes.csv', sep=',', index=False,header=True);
ingridiant_data.to_csv(save_location+'all_ingridiants.csv', sep=',', index=False,header=True);

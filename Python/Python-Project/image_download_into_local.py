import pandas as pd;
import os;

#src="https://spoonacular.com/recipeImages/500624-556x370.jpg";
#dest="D:\\data_processing\\ritesh_bawri_app_data\\final_output\\recipes_images\\local-filename.jpg";


#os.system('curl.exe --output "'+dest+'" --url "'+src+'"');

file_path="D:\\data_processing\\ritesh_bawri_app_data\\final_output\\db_reciepe_master.csv";
save_data="D:\\data_processing\\ritesh_bawri_app_data\\final_output\\recipes_images\\";
data=pd.read_csv(file_path, sep=',', );
for i in range(0,len(data)):    
    file=data["rcp_image"][i];
    fname=(file.split('.')[-1]).strip();
    save=save_data+data["ba_rcpid"][i]+"."+fname;
    os.system('curl.exe --output "'+save+'" --url "'+file+'"');
    print(fname);

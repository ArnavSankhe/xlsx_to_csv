import pandas as pd
import os

input_path = r'x' #update inpur path
output_path = r'x' #update output path

files = os.listdir(input_path)

for file in files:
    if file.endswith('.xlsx'):
        excel_file_path = os.path.join(input_path, file)
        excel_file = pd.read_excel(excel_file_path, engine="openpyxl", sheet_name= None)

        for sheet_name, df in excel_file.items():
            file_to_save_xlsx = pd.read_excel(excel_file_path, sheet_name = sheet_name, index_col= None)
            
            output_file_name = f'final_{file}_{sheet_name}.csv'
            final_output_path = os.path.join(output_path, output_file_name)

            file_to_save_xlsx.to_csv(final_output_path, index= False)
            print(f'saved: {final_output_path}')
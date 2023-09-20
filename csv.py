def save_data(data):
    with open('data.csv', mode='a', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["URL",'Email Address','Telephone','Website'])
        writer.writerow(data)
### CSV to xL convert
import pandas as pd
csv_file = 'input.csv'
excel_file = 'output.xlsx'
df = pd.read_csv(csv_file)
df.to_excel(excel_file, index=False)
print(f"CSV file '{csv_file}' has been converted to Excel file '{excel_file}'.")

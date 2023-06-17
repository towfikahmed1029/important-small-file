import gspread
from google.oauth2.service_account import Credentials
scope = ['https://www.googleapis.com/auth/spreadsheets']
credentials = Credentials.from_service_account_file('key.json', scopes=scope)
client = gspread.authorize(credentials)
spreadsheet_id = '1oofCJasXutqRY_28Z_cIRiUpMD-V9tA8FRGHz3ekY_I'
sheet = client.open_by_key(spreadsheet_id).sheet1

### https://console.cloud.google.com/apis/credentials?project=gspython-390105
# Read data from a specific range
def read_data():
    data = sheet.get_all_values()
    for row in data:
        print(row)

# Write data to a specific cell
def write_data():
    new_data = ['New Data']
    sheet.append_row(new_data)

# Check if data exists in a specific column
def check_data():
    search_values = ['gg', 'gg', 'hth']  # List of values to search
    data = sheet.get_all_values()
    
    for row in data:
        if row == search_values:
            print('Data exists!')
            print('Row:', row)
            break
    else:
        print('Data does not exist.')

# Call the functions
read_data()
write_data()
check_data()

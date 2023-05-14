def save_data(data):
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["URL",'Email Address','Telephone','Website'])
        writer.writerow(data)

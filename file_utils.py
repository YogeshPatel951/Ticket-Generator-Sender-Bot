import csv

def csvwrite(data):
    with open('data.csv','w') as f:
        csv_writer = csv.writer(f,delimiter=',')
        csv_writer.writerows(data)
        print('file write success')

def csvread(data):
    with open('data.csv','r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        data=[]
        for row in csv_reader:
            data.append(row)
    print('file read success')
    return data
    
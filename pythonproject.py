import json
import csv
import requests
api_url="https://prod-bl.qp.akasaair.com//api/ibe/gst/invoice/view?pnr=K5SV8Z&lastName=Vaddo"
token=" https://s3.console.aws.amazon.com/s3/buckets/akasa-test?region=ap-south-1&tab=objects"
headers={
    'Authorisation': token,
    'Content-Type':'application/json;charecterset=utf-8',
}
with open(r'C:\Users\HP\Desktop\finkraftpython\Akasa_PNR_Consolidated.csv','w+') as csvFile:
    reader=csv.reader(csvFile)
    writer=csv.writer(csvFile)
    columns=next(reader)
    writer.writerow(columns)
    for pnr,lastName,Transaction_Date  in reader:
        data =json.dumps([{
        'pnr':pnr
        'lastName':lastName
        'Transaction_Date':Transaction_Date
        }])

        response= requests.post(
            f'{api_url}/api/match',
            headers=headers,
            data=data
            )
        
        if response.ok:
            match='yes'
        else:
            match='no'
        
        writer.writerrow((pnr,lastName,Transaction_Date,match))



      
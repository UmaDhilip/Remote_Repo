import pymongo
import json
import pandas as pd
import logging
import custlogger
import matplotlib.pyplot as plt

#Create log filename
split_file = __file__.split('\\')[-1]
log_fname = split_file.replace('py', 'log')
log = custlogger.create_logger(filename=log_fname,loglevel=logging.WARNING)


def open_connection():
    ''' Open the pymongo connection '''  

    clientObj = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    dbObj = clientObj["DemoGeneric"] # DB Name
    collObj = dbObj['gen_info'] # Collection name
    log.info("Successfully created the Collection Object")
    return(collObj)

def insert_records(collObj):

    with open("C:\\Users\\mahii\Project\\schoolinfo\\generic_info.json","r") as fileData:
        #records = json.load(fileData)
        records = json.loads(fileData.read())
        log.info("Read the json file successfully")
        log.info(records) # Testing purpose - Using the fewer records
       
        if isinstance(records, list):
            collObj.insert_many(records)
            log.info("Records are successfully inserted inside the Mongo DB")
            
    return records

def fetch_persons_age(collObj):
    ''' Fetch the person lastname , firstname and their age > 40 '''
    df = pd.DataFrame(list(collObj.find()))
    # retrieve the person whose age > 40
    df = df[df['age'] > 40 ]
    # Remove the duplicate records from the dataframe
    log.info("Filtering the records based on their age - here age > 40")
    ret_list = df[['firstName','lastName','age']].drop_duplicates()
    log.info(ret_list)

    #Plot the bar graph
    #ret_list.plot(x='lastName',y='age',kind='bar')
    #plt.show()

def find_person_state(records):
    ''' Retrieve the list of persons and group by their state '''
    log.info("Fetch the Persons list group by State ID")
    flat_arr = pd.json_normalize(records,max_level=1)
    ad_state = flat_arr['address.state'].unique()
    res = flat_arr['lastName'].groupby(flat_arr['address.state']).count()
    log.info(f'States : {res.index.values} Count : {res.values}')
    #Plot the bar graph   
    #res.plot(x=res.index.values,y=res.values,kind='line')
    #plt.show()

def main():

    collObj = open_connection()
    collObj.drop() # remove the records that are already stored - For testing
    
    recs = insert_records(collObj) 
    
    fetch_persons_age(collObj)
    
    find_person_state(recs)

if __name__ == '__main__':
    main()
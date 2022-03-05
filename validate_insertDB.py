import os
import re
import logging
import custlogger
import sqlite3

#Create log filename
split_file = __file__.split('\\')[-1]
log_fname = split_file.replace('py', 'log')
log = custlogger.create_logger(filename=log_fname,loglevel=logging.WARNING)

def chk_inFile_exists(my_file):
    try:
        if os.path.getsize(my_file) > 0:
            log.info(f'The File exists and its not empty {my_file}')
            return 0

        else:
            log.error(f'File {my_file} exists but its empty ')
            return 1

    except OSError as e:
        log.exception(f'Msg: {e}')
        return 1
    
def process_input(my_file):
    key_list = ['EmpName','EmpId','Job Description','Salary','email','contact num','Company Name','State']
    create_dict = {}

    with open(my_file,"r") as fHnd:
        in_list = fHnd.readlines()
        for each_line in in_list:
            extract_list = re.split(r',', each_line)
            (emp_name,emp_id,jd,sal,email,contactnum,company,state) = extract_list[::]           
            create_dict[emp_id] = [emp_name,jd,sal,email,contactnum,company,state]

    return create_dict


def validate_email(email):
    ret_value = True
    email_fmt = '^[A-Za-z0-9_]+[a-z0-9]+[@]\w+[.]\w{2,3}$'
    email = email.strip()
    if(re.search(email_fmt,email)):
        log.info(f'Email id {email} is in right format')
    else:
        log.error(f'Oops! Email id {email} is not in right format!')
        ret_value = False
    
    return ret_value


def validate_fields(conn, input_dict):
    ret_Val = True 
    task = ()
    # Validating the important fields that instructed
    (emp_name,jd,sal,email,contactnum,company,state) = ('','','','','','','')
    for key,val in input_dict.items():

        emp_name,jd,sal,email,contactnum,company,state = val[0],val[1],val[2],val[3],val[4],val[5],val[6]
        key = key.strip()
        emp_name = emp_name.strip()
        jd = jd.strip()
        sal = sal.strip()
        email = email.strip()
        contactnum = contactnum.strip()
        company = company.strip()
        state = state.strip()
        
        log.info("Check emp name is valid:")    
        if(len(emp_name) > 0 and re.match(r'[\w\s]+',emp_name)):
            log.info(f'Emp name {emp_name} is valid and can proceed further.') 
    
        log.info(f'Validate the Salary field:')
        sal = re.sub(r'[\$]','',sal)
        if(len(sal) > 3):
            log.info(f'Emp name {emp_name} \'s salaray field is valid and can proceed further.')
        else:
            ret_Val = False
            log.error(f'Emp name {emp_name} \'s is not valid .')
                
        log.info("Check email id is in correct format:")
        retVal = validate_email(email) 

        cnum_fmt = '^\+\d{1}\d{10}$'
        if(len(contactnum)>0 and re.match(cnum_fmt,contactnum)):
            log.info(f'Emp {emp_name} \'s phone number {contactnum} is valid')
        else:  
            ret_Val = False          
            log.error(f'Emp {emp_name} \'s phone number {contactnum} is not valid')

        task = emp_name,key,jd,sal,email,contactnum,company,state
        row_id = insert_table(conn, task)

    return ret_Val


def create_connection():
    sqlite_conn = None
    database = r"C:\Users\mahii\Downloads\sqlite-tools-win32-x86-3380000\sqlite-tools-win32-x86-3380000\sample.db"
    try:
        sqlite_conn = sqlite3.connect(database)
    except:
        log.error("Connection Failed")

    return sqlite_conn

def insert_table(sqlite_conn, task):
    qry = '''INSERT into employee(empname,empid,desig,salary,email,phnum,company,stateId) values(?,?,?,?,?,?,?,?)'''
    try:
        cursor = sqlite_conn.cursor()
        cursor.execute(qry, task)
        sqlite_conn.commit()
    except:
        log.error(f'Duplicate recs cannot be inserted')
        

    return cursor.lastrowid

def main():
    my_file = "C:\\Users\\mahii\\Project\\Proj_Python\\input_regexp.txt"
    
    conn = create_connection()      
    ret_val = chk_inFile_exists(my_file)

    if(ret_val == 0):
        input_dict = process_input(my_file)
        ret_Val = validate_fields(conn, input_dict)


if(__name__ == '__main__'):
    main()
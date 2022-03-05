import logging
import custlogger
import numpy as np

log = custlogger.create_logger(filename="work_numpy.log",loglevel=logging.WARNING)

#arrfull = np.full([2,2],101,dtype='int',order='C')
#arrempty = np.empty((2,3),dtype='int')
#arr1 = np.zeros([4,2])
#arr2 = np.ones((3,3))
    
Arr = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
lst = [2,4,6,7,9]

def check_list_exist():
    if lst in Arr: 
        log.info(f'list: {lst} existing inside the array : {Arr} ')
    else:
        log.info(f'list: {lst} not existing inside the array : {Arr} ')

def remove_non_numeric_values():
    #testarr= np.array([[1,2,3,4],[5,np.nan,6,np.nan]])
    testarr = np.array([1,2,3,4,5,np.nan,np.nan])
    #accessing the not a number elemens
    not_num = testarr[np.isnan(testarr)]    
    log.info(f'Accessing only the not a number elements: {not_num} from original array: {testarr}')
    
    modified_arr = testarr[~np.isnan(testarr)]
    log.info(f'Removing the not a number elements from the array, so the new array be {modified_arr}')
        
def remove_single_dim_entry():
    in_arr = np.array([[[2, 2, 2], [2, 2, 2]]])
    out_arr = np.squeeze(in_arr)
    log.info(f'Input Array : {in_arr} , Output Array : {out_arr}')

def find_sequence():
    in_arr = np.array([[1,2,9,5],
                       [9,5,2,3],
                       [7,9,5,3],
                       [9,5,1,2]]
                       )
    out_arr = repr(in_arr).count("9")
    log.info(f'Check the element : 9 from the input array {in_arr}')
    log.info(f'The sequence appeared {out_arr} times ')

def comparing_arrays():
    in_arr1 = np.array([[1,2,3],[3,2,1]])
    in_arr2 = np.array([[2,3,4],[3,2,1]])
    cmp = in_arr1 == in_arr2
    log.info(f'Comparing the arrays {in_arr1} and {in_arr2} ')
    #print(cmp)

def combine_arrays():
    in_arr1 = np.array([[1,2,3],[3,20,1]])
    in_arr2 = np.array([[29,3,4],[13,2,1]])   

    arr3 = np.concatenate((in_arr1,in_arr2))
    log.info(f'Concatenate the arrays: {arr3}')
    #stacking is done alone the axis
    arr4 = np.stack((in_arr1,in_arr2),axis=1)
    log.info(f'Stacking the arrays : {arr4}')

    arr5 = np.hstack((in_arr1,in_arr2))
    log.info(f'Stacking the arrays columnwise: {arr5}')

    arr6 = np.vstack((in_arr1,in_arr2))
    log.info(f'Stacking the arrays row wise: {arr6}')

    arr7 = np.dstack((in_arr1,in_arr2))
    log.info(f'Stcking the array depth wise: {arr7}')

def split_arrays():
    in_arr1 = np.array([[11,21,31],[33,20,13]])
    newarr = np.split(in_arr1,2)
    log.info(f'After splitting the arrays: {newarr}')

    newarr1 = np.array_split(in_arr1, 2)
    for arr in newarr1:
        log.info(f'Iterating over the arrays: {arr}')

    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
    newarr2 = np.array_split(arr, 2, axis=0)
    log.info(f'After the split using split_arr method: {newarr2}')

    newarr3 = np.hsplit(arr,3)
    log.info(f'Split the array using hsplit method: {newarr3}')


def search_arrays():
    # while we search the particular element , it resturns the index of the element
    arr = np.array([1, 2, 3, 4, 5, 4, 4])
    x = np.where(arr == 4)
    log.info(f'The element 4 is found in {x} indices')
    x1 = np.where(arr %2 == 0)
    log.info(f'The indices {x1} of the element can be divided by 2')


def insert_at_right_index():
    '''search sorted  method used to search the array for the right position and insert the element in the sorted order'''
    arr = np.array([6, 7, 8, 9])

    out_arr = np.searchsorted(arr, 11)
    np.insert(arr,out_arr,11)

    log.info(f'Sort the array {arr} and insert the element : 11 at the right position {out_arr}')

def sorting_arr():
    ''' Sorting the array elements '''
    arr = np.array([3, 2, 0, 1])
    sort_arr=np.sort(arr)
    log.info(f'Input array : {arr} and after sorting {sort_arr} ')

def filter_array():
    '''Filter and return only the even elements'''
    filter_arr = []
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    for elem in arr:
        if (elem%2 == 0):
            filter_arr.append(elem)
    log.info(f'Input array {arr} and filter the array and fetch only the even elements: {filter_arr}')
    

def main():
    
    check_list_exist()
    remove_non_numeric_values()
    remove_single_dim_entry()
    find_sequence()
    comparing_arrays()
    combine_arrays()
    split_arrays()
    search_arrays()
    insert_at_right_index()
    sorting_arr()
    filter_array()

if __name__ == '__main__':
    main()

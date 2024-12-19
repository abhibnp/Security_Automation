import csv

'''
File handler class
'''
class FileUtility():
    '''
    This class provide all file handling related functions
    '''
    @staticmethod
    def write_json_data_to_file(_input_data, _file_name, _mode, _logger):
        '''
        write any input data into a file
        '''
        try:
            outfile = open(_file_name, _mode, encoding='UTF-8')
            # Writing a string to file
            outfile.write(str(_input_data))
            # Closing file
            outfile.close()
        except Exception as _ex:
            _logger.exception("FileUtility.write_json_data_to_file: %s", str(_ex))

    @staticmethod
    def write_csv_data_to_file(_file_name, _input_data, _header):
        '''
        write any input data into a file
        '''
        try:
            with open(_file_name+'.csv', "wt", newline="") as csv_file:
                write = csv.writer(csv_file)
                write.writerow(_header)
                write.writerows(_input_data)
        except Exception as _ex:
            print("FileUtility.write_csv_data_to_file: ", str(_ex))
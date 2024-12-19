'''
Utility class exposing issue related functionalities
'''
class GeneralUtility():
    '''
    This class provide all issue handling related functions
    '''

    @staticmethod
    def get_iot_severity(level: str):
        '''
        get the severity from level
        '''
        if level.lower() == 'high':
            return '2. Critical'
        elif level.lower() == 'medium':
            return '3. Moderate'
        if level.lower() == 'audit' or level.lower() == 'low':
            return '4. Minor'

    @staticmethod
    def get_iot_priority(level: str):
        '''
        get the priority from level
        '''
        if level.lower() == 'high':
            return 'High'
        elif level.lower() == 'medium':
            return 'Medium'
        if level.lower() == 'audit' or level.lower() == 'low':
            return 'Low'

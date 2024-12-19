
"This is a data class for storing details of jira issue"

# importing enum for enumerations
import enum

# creating enumerations using class
class ProjectGroup(enum.Enum):
    '''
    Add more group if Jira project uses different custom fields
    '''
    GROUP_NONE = 0,
    GROUP_IOT = 1,
    GROUP_CODEDX = 2,
    GROUP_UNKNOWN = 3

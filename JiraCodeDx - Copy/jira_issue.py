
"This is a data class for storing details of jira issue"

from abc import ABC, abstractmethod

class JiraIssue(ABC):
    '''
    To represent Jira issue create items
    '''
    key : str
    summary : str
    description : str
    issuetype: str
    status: str

    @abstractmethod
    def __init__(self, _key: str, _summary: str, _description: str, _issue_type: str, _status: str):
        '''
        Initializes the object
        '''
        self.key = _key
        self.summary = _summary
        self.description = _description
        self.issuetype = _issue_type
        self.status = _status
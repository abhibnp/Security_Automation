"This is a data class for storing details of jira issue"

from jira_issue import JiraIssue
from general_utility import GeneralUtility

class CCB_CodeDx_Issue(JiraIssue):
    '''
    To represent Jira issue of type IOT project group
    '''
    logger = None
    code_dx_project_name: str
    tool: str
    testing_type: str
    cwe_severity: str
    url: str
    # Components
    components: str
    # Priority - name to be updated
    priority: str
    # Assignee
    assignee: str
    # Reporter
    reporter: str
    # Change Type
    change_type: str
    # Aplication Name
    _aplication_name: str

    def __init__(self, _logger, _project: str, _issue):
        '''
        Initializes the object
        '''
        self.logger = _logger

        # initialize the super class properties
        JiraIssue.__init__(self, _issue.key,
            _issue.fields.summary, _issue.fields.description,
            _issue.fields.issuetype.name, _issue.fields.status.name)
        self.code_dx_project_name = "Project-Governance"
        self.tool = "Jira"
        self.testing_type = "("+ _project + ") Change Control Board"
        self.cwe_severity = 0
        self.url = "https://<jira_url>/browse/"+_issue.key

        try:
            self.components = ""
            if _issue.fields.components is not None:
                for comp in _issue.fields.components:
                    self.components = comp.name  #_issue.fields.components[0].name
        except Exception as _ex:
            self.__logger.exception("CCB_CodeDx_Issue.construtor: components %s", str(_ex))

        self.priority = _issue.fields.priority.name
        self.change_type = _issue.fields.customfield_10005.value

        try:
            if _issue.fields.assignee is not None and _issue.fields.assignee.displayName is not None:
                self.assignee = _issue.fields.assignee.displayName
            if _issue.fields.reporter is not None and _issue.fields.reporter.displayName is not None:
                self.reporter = _issue.fields.reporter.displayName
        except Exception as _ex:
            self.__logger.exception("CCB_CodeDx_Issue.construtor: displayName %s", str(_ex))

    def to_dict(self):
        '''
        Converts the class object to dictionary object
        '''
        jc_object = {
            "Project Name": self.code_dx_project_name,
            "Tool": self.tool,
            "Testing Type": self.testing_type,
            "Issue Title":self.summary,
            "CWE": self.cwe_severity,
            "Severity": "Low",
            "Status": self.status,
            "URL": self.url,
            "Description": self.description
        }
        return jc_object
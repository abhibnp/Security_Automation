"This is a data class for storing details of jira issue"

from jira_issue import JiraIssue
from general_utility import GeneralUtility

class IoTJiraIssue(JiraIssue):
    '''
    To represent Jira issue of type IOT project group
    '''
    # Epic Link
    customfield_10013: str
    # severity
    customfield_10027: dict
    # Envrmnt - Dev
    customfield_10028: dict
    # found_during
    customfield_10031: dict
    # found_by
    customfield_10032: dict
    # category
    customfield_10048: dict
    # identified_during
    customfield_10113: dict
    # Components
    components: list
    # Priority - name to be updated
    priority: dict
    # Assignee
    assignee: str
    # Reporter
    reporter: dict
    # level will be used to find severity and priority
    level: str

    def __init__(self, _project: str, _summary: str, _description: str, _components: list, _level: str = None):
        '''
        Initializes the object
        '''
        # initialize the super class properties
        JiraIssue.__init__(self, _project, _summary, _description, _components)
        # Epic Link
        self.customfield_10013 = ""
        # Severity
        self.level = _level
        # # self.customfield_10027 = dict({"id": '10022'})
        if _level is not None:
            self.customfield_10027 = dict({"value": GeneralUtility.get_iot_severity(_level)})
        else:
            self.customfield_10027 = dict({"value": ""})
        self.customfield_10028 = dict({"value": ''})
        # # found_during: 10043 - Automation
        # #self.customfield_10031 = dict({"id": '10043'})
        self.customfield_10031 = dict({"value": ''})
        # # 100047 - Internal
        # # self.customfield_10032 = dict({"id": '10047'})
        self.customfield_10032 = dict({"value": ''})
        # # 10070 - Testing
        # # self.customfield_10048 = dict({"id": '10070'})
        self.customfield_10048 = dict({"value": ''})
        # # 10209 - Automation / Manual
        # # self.customfield_10113 = dict({"id": '10209'})
        self.customfield_10113 = dict({"value": ''})
        comp = []
        # # 10698 - Test/
        # # comp_dict = dict({"id": '10698'})
        comp_dict = dict({"name": ''})
        comp.append(comp_dict)
        self.components = comp
        if _level is not None:
            self.priority = dict({"name": GeneralUtility.get_iot_priority(_level)})
        else:
            self.priority = dict({"value": ""})
        self.assignee = dict({"accountId": ""})
        self.reporter = dict({"accountId": ""})

    def to_dict(self):
        '''
        Converts the class object to dictionary object
        '''
        jc_object = {
            "project": self.project,
            "summary": self.summary,
            "description": self.description,
            "issuetype": self.issuetype,
            "labels": self.labels,
            "customfield_10013": self.customfield_10013,
            "customfield_10027": self.customfield_10027,
            "customfield_10028": self.customfield_10028,
            "customfield_10031": self.customfield_10031,
            "customfield_10032": self.customfield_10032,
            "customfield_10048": self.customfield_10048,
            "customfield_10113": self.customfield_10113,
            "components": self.components,
            "priority": self.priority,
            "assignee": self.assignee,
            "reporter": self.reporter
        }
        return jc_object

    # create separate custom field mapper based of separate project group
    @staticmethod
    def update_iot_custom_field(_issue,
    _unique_issue_id: str,_tool_name: str, _stream_name: str, _bd_project_name: str,
    _branch_name: str, _epic_link: str,
    _unique_lable_name: str, _found_during: str, _found_by: str, _scan_type: str, _envrmnt: str, _category: str,
    _assignee: str, _reporter: str, _component: str):
        '''
        update jira issue custom field
        '''
        labels = []
        labels.append('tool:' + _tool_name)
        # proj_stream = 'stream:' if _tool_name.lower() == 'coverity' else 'bd-project:'
        # proj_stream += _stream_name if _tool_name.lower() == 'coverity' else _bd_project_name
        if _tool_name.lower() == 'coverity':
            proj_stream = 'stream:'+_stream_name
        if _tool_name.lower() == 'blackduck':
            proj_stream = 'bd-project:'+_bd_project_name
        labels.append(proj_stream)
        labels.append('branch:' + _branch_name)
        labels.append(_unique_lable_name+":"+ _unique_issue_id)
        _issue['labels'] = labels
        # update custom field epic link
        _issue['customfield_10013'] = _epic_link
        # update custom field envrmnt
        _issue['customfield_10028'] = dict({"value": _envrmnt})
        # update custom field found_during
        _issue['customfield_10031'] = dict({"value": _found_during})
        # update custom field found_by
        _issue['customfield_10032'] = dict({"value": _found_by})
        # update custom field category
        _issue['customfield_10048'] = dict({"value": _category})
        # update custom field identified_during
        _issue['customfield_10113'] = dict({"value": _scan_type})
        comp = []
        comp_dict = dict({"name": _component})
        comp.append(comp_dict)
        # update custom field components
        _issue['components'] = comp
        _issue['assignee'] = dict({"accountId": _assignee})
        _issue['reporter'] = dict({"accountId": _reporter})
        return _issue

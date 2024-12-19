
"This is a data class for storing details of jira issue"
# importing enum for enumerations
from common_enums import ProjectGroup

from iot_jira_issue import IoTJiraIssue
from code_dx_issue import CCB_CodeDx_Issue

class JiraIssueFactory:
    '''
    Factory class to create jira issue object based on input project group enum
    '''
    logger = None

    @staticmethod
    def get_jira_issue_instance(_enum_project_group: ProjectGroup,
    _project: str, _summary: str = None, _description: str = None, _labels: list = None,
    _issue_severity: str = None, _issue = None):
        '''
        Class factory method to creat jira issue object based on project group
        '''
        if _enum_project_group == ProjectGroup.GROUP_IOT:
            if _issue is not None:
                issue: IoTJiraIssue = _issue
                return IoTJiraIssue(_project, _summary, _description, issue.fields.components)
            else:
                return IoTJiraIssue(_project, _summary, _description, _labels, _issue_severity)
        elif _enum_project_group == ProjectGroup.GROUP_CODEDX:
            if _issue is not None:
                return CCB_CodeDx_Issue(JiraIssueFactory.logger, _project, _issue)
        elif _enum_project_group == ProjectGroup.GROUP_UNKNOWN:
            return None

    # Add separate project group if Jira project group is different
    @staticmethod
    def update_custom_field(_enum_project_group: ProjectGroup,
    _issue, _unique_issue_id: str, _tool_name: str, _stream_name: str, _bd_project_name: str,
    _branch_name: str, _epic_link: str, _unique_lable_name: str, _found_during: str, _found_by: str,
    _scan_type: str, _envrmnt: str, _category: str, _assignee: str, _reporter: str, _component: str):
        '''
        update jira issue custom field
        '''
        if _enum_project_group == ProjectGroup.GROUP_IOT:

            return IoTJiraIssue.update_iot_custom_field(_issue,
            _unique_issue_id, _tool_name, _stream_name, _bd_project_name, _branch_name, _epic_link,
            _unique_lable_name, _found_during, _found_by, _scan_type, _envrmnt, _category,
            _assignee, _reporter, _component)

        elif _enum_project_group == ProjectGroup.GROUP_UNKNOWN:
            return None

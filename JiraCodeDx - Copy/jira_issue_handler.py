'This class read/create/delete issues from Jira instance'
# from operator import contains
from jira.client import JIRA
from numpy import empty
from jira_issue_factory import JiraIssueFactory
from common_enums import ProjectGroup
from file_utility import FileUtility
import json
import csv

class JiraIssueHandler():
    '''
    This class is responsible for connecting to Jira to search issues.
    Basic functionalities such as Search/Create/Delete are provided here
    '''
    # private members
    __JIRA_SERVER = "https://dovercorp.atlassian.net"
    # Jira user name using which account id needed to retrieved
    __JIRA_USER = "<user name>"
    __API_TOKEN = "<api_token>"

    __jira_instance = None
    __project_group: ProjectGroup = ProjectGroup.GROUP_NONE
    __logger = None

    def __init__(self, _logger, _project_group: ProjectGroup):
        '''
        Parameterised constructor of the class
        '''
        self.__logger = _logger
        self.__project_group = _project_group

    def connect_jira(self):
        '''
        Defines a function for connecting to Jira
        Connect to JIRA. Return None on error
        '''
        try:
            self.__logger.debug("JiraIssueHandler.connect_jira: Connecting to JIRA: %s",
                self.__JIRA_SERVER)
            jira_options = {'server': self.__JIRA_SERVER}
            self.__jira_instance = JIRA(options=jira_options, basic_auth=(self.__JIRA_USER, self.__API_TOKEN))
            self.__logger.info("JiraIssueHandler.connect_jira: JIRA Connected")

        except ConnectionError as _ex:
            self.__logger.exception("JiraIssueHandler.connect_jira: Failed to connect to JIRA. %s", str(_ex))
            self.__jira_instance = None

    def get_jira_issues(self, _project_name):
        '''
        Get all jira issues matching input project name
        '''
        try:
            if self.__jira_instance is None:
                return None
            issues = []
            issue_index = 0
            # TODO Reading only In Progress/TO DO and Type Bug.
            # We can optimize by reopen already created issue which is marked Done
            search_criteria = 'project='+_project_name+' and type="Change Request" and created >= "2023-02-17" and text ~ "Security Review"'

            while True:
                jira_issues = self.__jira_instance.search_issues(search_criteria,
                    maxResults=50,
                    startAt=issue_index)
                count = len(jira_issues)

                # for issue in jira_issues:
                #     print(issue)
                if count > 0:
                    self.__logger.debug("JiraIssueHandler.get_jira_issues: Get jira issues index %i, count %i ",
                        issue_index, count)

                    JiraIssueFactory.logger = self.__logger

                    for issue in jira_issues:
                        obj_ji = JiraIssueFactory.get_jira_issue_instance(_enum_project_group = self.__project_group,
                            _project = _project_name, _issue = issue)
                        issues.append(obj_ji)
                    issue_index += count
                else:
                    break

            results = [obj.to_dict() for obj in issues]
            field_names= ['Project Name', 'Tool', 'Testing Type', 'Issue Title', 'CWE', 'Severity',	'Status', 'URL', 'Description']
            with open('existing_jira_issues.csv', 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(results)

            return None
        except Exception as _ex:
            self.__logger.exception("JiraIssueHandler.get_jira_issues: %s", str(_ex))
            return None
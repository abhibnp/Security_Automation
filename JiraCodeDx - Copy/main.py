'''
Main script for creating Jira issue for coverity scan
'''
import sys
from common_enums import ProjectGroup
from jira_issue_handler import JiraIssueHandler
import logging
import time

# main script
logging.basicConfig()
LOGGER = logging.getLogger()
LOGGER.setLevel (logging.INFO)

# We need to add more project group of Jira if project custom fields are different
PROJECT_GROUP: ProjectGroup = ProjectGroup.GROUP_CODEDX

# ==================================================
try:
    JIRA_PROJECT = "CCB"
    LOGGER.info("JIRA Project Name %s", JIRA_PROJECT)

    startTime = time.time()
    jira_issue_handler = JiraIssueHandler(LOGGER, PROJECT_GROUP)

    #Create a connection object of jira. We still do not know whether to dispose
    jira_issue_handler.connect_jira()
    jira_issue_handler.get_jira_issues(JIRA_PROJECT)

    LOGGER.debug("Script Completed in %s", str(time.time() - startTime))
except Exception as _ex:
    LOGGER.exception(str(_ex))
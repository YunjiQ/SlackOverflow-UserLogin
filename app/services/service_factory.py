from framework.services.service_factory import BaseServiceFactory
import app.resources.user_resource as user_resource  # course_resource
from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService


# TODO -- Implement this class
class ServiceFactory(BaseServiceFactory):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_service(cls, service_name):
        #
        # TODO -- The terrible, hardcoding and hacking continues.
        #
        if service_name == 'UserLoginResource':  # 'CourseResource'
            result = user_resource.UserLoginResource(config=None)        # course_resource.CourseResource(config=None)
        elif service_name == 'UserLoginResourceDataService':  # 'CourseResourceDataService'
            context = dict(user="admin", password="slackOverflowDB",
                           host="database-1.ccjxezwbfect.us-east-1.rds.amazonaws.com", port=3306)
            data_service = MySQLRDBDataService(context=context)
            result = data_service
        else:
            result = None

        return result





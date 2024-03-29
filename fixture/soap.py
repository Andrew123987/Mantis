from suds.client import Client
from suds import WebFault
from model.project_model import Project


class SoapHelper():
    def __init__(self, app):
        self.app = app



    def can_login(self, username, password):
        client = Client(self.app.config['soap']['address'])
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault as fault:
            print(fault)
            return False

    def get_projects_for_user(self, username, password):
        client = Client(self.app.config['soap']['address'])
        try:
            data = client.service.mc_projects_get_user_accessible(username, password)
            list = []
            if len(data) > 0:
                for i in range(len(data)):
                    id = data[i].id
                    name = data[i].name
                    status = data[i].status.name
                    enabled = data[i].enabled
                    view_status = data[i].view_state.name
                    description = data[i].description
                    list.append(Project(id=id,
                                        name=name,
                                        status=status,
                                        enabled=enabled,
                                        view_status=view_status,
                                        description=description))
                return list
            else:
                return list
        except WebFault as fault:
            print(fault)
            return False

    def get_projects_unstructured_data_for_user(self, username, password):
        client = Client(self.app.config['soap']['address'])
        try:
            response_data = client.service.mc_projects_get_user_accessible(username, password)
            return response_data
        except WebFault as fault:
            print(fault)
            return False

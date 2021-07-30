from rest_framework import viewsets, permissions
from .models import Contributor
from .serializers import ContributorSerializer
from project.models import Projects

class ContributorViewSet(viewsets.ModelViewSet):

    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer



    def get_queryset(self, *args, **kwargs):
        query_project = self.kwargs.get('project_pk')
        query_user = self.kwargs.get('pk')
        try:
            if query_project and query_user:
                project = Projects.objects.get(pk=query_project)
                users = Contributor.objects.filter(project=project.id)
                user = users.filter(pk=query_user)
                return user
            elif query_project:
                project = Projects.objects.get(pk=query_project)
                users = Contributor.objects.filter(project=project.id)
                return users
            else:
                pass
        except:
            pass



    def perform_create(self, serializer):
        query_project = self.kwargs.get('project_pk')
        if query_project:
            try:
                project = Projects.objects.get(pk=query_project)
                serializer.save(project=project)
            except:
                pass
        else:
            pass


    def perform_update(self, serializer):
        query_project = self.kwargs.get('project_pk')
        if query_project:

                project = Projects.objects.get(pk=query_project)
                users = Contributor.objects.filter(project=project.id)
                print(str(users))
                user = users.get(id=query_project)
                print(str(user))


                serializer.save(id=user.id)













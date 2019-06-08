from django.http import HttpResponse
from rest_framework import viewsets
from restapi.models import Lead
from restapi.serializers import LeadSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at Leads API.")

# class ThisWillBeTheApiTitleView(routers.APIRootView):
#     """
#     This appears where the docstring goes!
#     """
#     pass

class LeadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

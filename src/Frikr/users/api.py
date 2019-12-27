from django.views.generic import View
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http.response import HttpResponse

class UserListAPI(View):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        serializer_users = serializer.data #list of dicts

        renderer = JSONRenderer()
        json_users = renderer.render(serializer_users)

        return HttpResponse(json_users)
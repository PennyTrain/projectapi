from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Accounts
from .serializers import AccountsSerializer

class AccountList(APIView):
    def get(self, request):
        account= Accounts.objects.all()
        serializer = AccountsSerializer(account, many=True)
        return Response(serializer.data)
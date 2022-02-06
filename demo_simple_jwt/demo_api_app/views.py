from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from django.db import connection
from rest_framework_simplejwt.authentication import JWTAuthentication



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        token['email'] = user.email

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def viewUser(request):
    content = {'message': 'Hello, World!'}
    # query = f"""SELECT * FROM public."user"
    #             ORDER BY id ASC """

    # with connection.cursor() as cursor:
    #     q_data = cursor.execute(query)
    #     q_data_fatch_all = cursor.fetchall()

    return Response(
        {
            "status": "success",
            "message": "Table created successfully",
            "data": content,
        },
        status=status.HTTP_200_OK,
    )

    
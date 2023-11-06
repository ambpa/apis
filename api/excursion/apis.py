from rest_framework import views
from rest_framework import permissions
from rest_framework import response
from rest_framework import status as rest_status
from rest_framework.decorators import authentication_classes, permission_classes

from user import authentication
from user import permissions as user_permissions

from . import serializer as excursion_serializer
from . import services

@authentication_classes([authentication.CustomUserAuthentication])
@permission_classes([permissions.IsAuthenticated])
class ExcursionCreateListApi(views.APIView):


    def post(self, request):
        serializer = excursion_serializer.ExcursionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        serializer.instance = services.create_excursion(user=request.user, excursion=data)

        return response.Response(data=serializer.data)

    def get(self, request):
        excursion_collection = services.get_user_excursion(user=request.user)
        serializer = excursion_serializer.ExcursionSerializer(excursion_collection, many=True)
        return response.Response(data=serializer.data)


@authentication_classes([authentication.CustomUserAuthentication])
@permission_classes([permissions.IsAuthenticated, user_permissions.IsStaff])
class ExcursionRetrieveUpdateDelete(views.APIView):

    def get(self, request, excursion_id):
        excursion = services.get_user_excursion_detail(excursion_id=excursion_id)
        serializer = excursion_serializer.ExcursionSerializer(excursion)
        return response.Response(data=serializer.data)

    def delete(self, request, excursion_id):
        services.delete_user_excursion(user=request.user, excursion_id=excursion_id)
        return response.Response(status=rest_status.HTTP_204_NO_CONTENT)

    def put(self, request, excursion_id):
        serializer = excursion_serializer.ExcursionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        excursion = serializer.validated_data
        serializer.instance = services.update_user_excursion(
            user=request.user, excursion_id=excursion_id, excursion_data=excursion
        )

        return response.Response(data=serializer.data)

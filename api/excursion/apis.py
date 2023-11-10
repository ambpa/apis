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
@permission_classes([permissions.IsAuthenticated, user_permissions.IsStaff])
class ExcursionCreateListApi(views.APIView):
    """
    View to list all excursion in the system.

    * Requires jwt authentication.
    * Only staff users are able to access this view.
    """

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
    """
    View to retrieve, update, and delete excursion details.

    This API view allows authenticated users to perform the following actions on an excursion:
    - Retrieve excursion details based on the provided 'id'.
    - Update excursion data with the provided information.
    - Delete an excursion.

    Authentication:
    - JWT authentication is required using a custom user authentication class.

    Permissions:
    - Only staff users (users with 'IsStaff' permission) are allowed to access this view.

    HTTP Methods and Usage:
    - GET: Retrieve excursion details by providing the 'id' of the excursion in the request data.
    - DELETE: Delete an excursion by providing the 'id' of the excursion in the request data.
    - PUT: Update an existing excursion by providing the 'id' and excursion data in the request.

    Response:
    - For GET, it returns the serialized excursion details.
    - For DELETE, it returns a 204 No Content response upon successful deletion.
    - For PUT, it returns the updated excursion details after a successful update.

    Note:
    - Users attempting to perform these actions on excursions that do not belong to them will
        receive a "PermissionDenied" response.
"""


    def get(self, request):
        excursion_id = request.data.get('id')
        print(excursion_id)
        excursion = services.get_user_excursion_detail(user=request.user, excursion_id=excursion_id)
        serializer = excursion_serializer.ExcursionSerializer(excursion)
        return response.Response(data=serializer.data)

    def delete(self, request):
        excursion_id = request.data.get('id')
        services.delete_user_excursion(user=request.user, excursion_id=excursion_id)
        return response.Response(status=rest_status.HTTP_204_NO_CONTENT)

    def put(self, request):
        excursion_id = request.data.get('id')
        print(excursion_id)
        serializer = excursion_serializer.ExcursionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        excursion = serializer.validated_data
        serializer.instance = services.update_user_excursion(
            user=request.user, excursion_id=excursion_id, excursion_data=excursion
        )

        return response.Response(data=serializer.data)



@authentication_classes([authentication.CustomUserAuthentication])
@permission_classes([permissions.IsAuthenticated])
class ReservationCreateListApi(views.APIView):
    """
    View to list all reservation in the system.

    * Requires jwt authentication.
    """

    def post(self, request):
        serializer = excursion_serializer.ReservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        excursion_id = request.data.get('excursion_id')

        serializer.instance = services.create_reservation(user=request.user, excursion_id=excursion_id, reservation=data)

        return response.Response(data=serializer.data)

    def get(self, request):
        reservation_collection = services.get_user_reservation(user=request.user)
        serializer = excursion_serializer.ReservationSerializer(reservation_collection, many=True)
        return response.Response(data=serializer.data)

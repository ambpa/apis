from django.urls import path

from . import apis

urlpatterns = [
    path("excursion/", apis.ExcursionCreateListApi.as_view(), name="excursion"),
    path(
        "excursion/<int:excursion_id>/",
        apis.ExcursionRetrieveUpdateDelete.as_view(),
        name="excursion_detail",
    ),
]

from django.urls import path

from . import apis

urlpatterns = [
    path("excursion/", apis.ExcursionCreateListApi.as_view(), name="excursion"),
    path(
        "excursion_detail/",
        apis.ExcursionRetrieveUpdateDelete.as_view(),
        name="excursion_detail",
    ),
]

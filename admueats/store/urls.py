from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("cafs", views.cafs, name="cafs-page"),
    path("cafs/tables",views.occupancy, name='occupancy'),
    path("cafs/<slug:slug>/menu", views.caf_detail,
         name="caf-menu-page"),
    path("cafs/<slug:slug>/tables", views.table_detail,
         name="caf-tables-page"),
]


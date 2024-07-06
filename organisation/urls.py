from django.urls import path
from .views import OrganisationListView, OrganisationDetailView, OrganisationAddUserView

urlpatterns = [
    path('', OrganisationListView.as_view(), name='organisation-list'),
    path('<uuid:orgId>/', OrganisationDetailView.as_view(), name='organisation-detail'),
    path('<uuid:orgId>/users/', OrganisationAddUserView.as_view(), name='organisation-add-user'),
]
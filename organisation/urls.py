from django.urls import path
from .views import OrganisationListView, OrganisationDetailView

urlpatterns = [
    path('', OrganisationListView.as_view(), name='organisation-list'),
    path('<uuid:orgId>/', OrganisationDetailView.as_view(), name='organisation-detail'),
]
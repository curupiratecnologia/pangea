from rest_framework import viewsets
from rest_framework import permissions

from django.contrib.auth.models import User, Group, Permission
from .serializers import UserSerializer, GroupSerializer, PermissionSerializer

from .models import ImportedTabularData, ImportedGeographicData, DataStatus, GeneralizationParams, LayerMetadata, Column
from .serializers import ImportedTabularDataSerializer, ImportedGeographicDataSerializer, DataStatusSerializer, GeneralizationParamsSerializer, LayerMetadataSerializer, ColumnSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAdminUser]



class ImportedTabularDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ImportedTabularData.objects.all()
    serializer_class = ImportedTabularDataSerializer
    permission_classes = [permissions.IsAdminUser, permissions.DjangoModelPermissions]


class ImportedGeographicDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ImportedGeographicData.objects.all()
    serializer_class = ImportedGeographicDataSerializer
    permission_classes = [permissions.IsAdminUser, permissions.DjangoModelPermissions]



class DataStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = DataStatus.objects.all()
    serializer_class = DataStatusSerializer
    permission_classes = [permissions.IsAdminUser]


class GeneralizationParamsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = GeneralizationParams.objects.all()
    serializer_class = GeneralizationParamsSerializer
    permission_classes = [permissions.IsAdminUser]


class LayerMetadataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = LayerMetadata.objects.all()
    serializer_class = LayerMetadataSerializer
    permission_classes = [permissions.IsAdminUser, permissions.DjangoModelPermissions]


class ColumnViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = [permissions.IsAdminUser, permissions.DjangoModelPermissions]
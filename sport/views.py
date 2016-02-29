from django.shortcuts import render
from .serializers import SportSerializer
from .models import Sport
from level.models import Level
from level.serializers import LevelReadSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route

# Create your views here.
class SportViewSet(viewsets.ModelViewSet):
	queryset = Sport.objects.all()
	serializer_class = SportSerializer
	permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

	@detail_route(methods=['get'])
	def levels(self, request, pk=None):
		sport = Sport.objects.get(pk=pk)
		queryset = Level.objects.filter(sport=sport)
		serializer = LevelReadSerializer(queryset, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
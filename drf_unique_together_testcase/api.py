from rest_framework import serializers, viewsets, routers, permissions

from drf_unique_together_testcase.models import Thing


class ThingSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault()),
    )

    class Meta:
        model = Thing
        fields = ('owner', 'name')
        read_only_fields = ('owner',)


class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


router = routers.DefaultRouter()
router.register('things', ThingViewSet)

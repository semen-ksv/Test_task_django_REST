from rest_framework.decorators import action
from rest_framework.response import Response
from .services import add_like, remove_like


class LikedMixin:
    @action(detail=True, methods=['POST'])
    def like(self, request, slug=None):
        """Лайкает `obj`.
        """
        obj = self.get_object()
        add_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def unlike(self, request, slug=None):
        """Удаляет лайк с `obj`.
        """
        obj = self.get_object()
        remove_like(obj, request.user)
        return Response()

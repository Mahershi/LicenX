from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..models import User
from ..helpers.scripts import custom_response, error_response
from django.http.response import Http404
from rest_framework.request import Request
from rest_framework.decorators import action
from ..serializers import UserSerializer
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]

        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        try:
            resp = super().create(request, *args, **kwargs)
            return custom_response(
                status=200,
                data=resp.data
            )
        except ValidationError as e:
            return error_response(
                status=400,
                error=e.detail
            )

    # set the password of authenticated user to "new_password"
    # user needs to be authenticated through token.
    @action(methods=['POST'], detail=False)
    def change_password(self, request: Request, *args, **kwargs):
        try:
            new_password = request.data['new_password']
            request.user.set_password(new_password)
            request.user.save()

            return custom_response(
                status=200,
                data="Password Updated!"
            )
        except Exception as e:
            return error_response(
                status=400,
                error=str(e)
            )

    # TODO: destroying user is not implemented yet.
    # to delete an existing user account, by the user themself or by superuser.
    def destroy(self, request, *args, **kwargs):
        return error_response(
            status=404,
        )


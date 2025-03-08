from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from ..models import Instance, Project, User, Subscriptions
from ..serializers import InstanceSerializer
from rest_framework.decorators import action
from rest_framework.request import Request
from ..helpers.scripts import custom_response, error_response
from rest_framework.renderers import JSONRenderer
from django.core.exceptions import ObjectDoesNotExist


class InstanceView(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = InstanceSerializer
    queryset = Instance.objects.all()
    renderer_classes = [JSONRenderer]

    @action(methods=['GET'], detail=False)
    def get_license(self, request: Request):
        if not request.query_params.get('project'):
            return error_response(
                status=400,
                error="Project Not provided in QP"
            )

        project_identity = request.query_params.get('project')

        try:
            project: Project = Project.objects.get(identity=project_identity)
            print(project)
            instance: Instance = Instance.objects.get(project=project)
            subscription: Subscriptions = Subscriptions.objects.get(instance=instance)

            return custom_response(
                status=200,
                data={
                    "project_id": project_identity,
                    "hwid": instance.hwid,
                    "domain": instance.domain,
                    "grace_period": subscription.grace_period,
                    "expiry": subscription.expires,
                    "checkin_interval": subscription.checkin_interval
                }
            )
        except ObjectDoesNotExist as e:
            return error_response(
                status=400,
                error="Object Not Found:" + str(e)
            )
        except Exception as e:
            return error_response(
                status=400,
                error="Unknown Exception:" + str(e)
            )


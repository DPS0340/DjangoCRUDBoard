from board.utils import send_json
from ..responses import illegalArgument, userDoesNotExist, promoteSucceed
from ..models import User

class PromoteView(View):
    def post(self, request):
        # Promoter 인증 로직 TODO
        if 'pk' not in request.POST:
            return send_json(illegalArgument)
        pk = request.POST['pk']
        found = User.objects.filter(pk=pk)
        if found.count() != 1:
            return send_json(userDoesNotExist)
        else:
            found.update(isAdmin=True)
            return send_json(promoteSucceed)
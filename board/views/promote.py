from board.utils import send_json
from ..responses import illegalArgument, userDoesNotExist, promoteSucceed, alreadyPromoted
from ..models import User
from django.views import View

class PromoteView(View):
    def post(self, request):
        # Promoter 인증 로직 TODO
        if 'userid' not in request.POST:
            return send_json(illegalArgument)
        userid = request.POST['userid']
        found = User.objects.filter(id=userid)
        if found.count() != 1:
            return send_json(userDoesNotExist)
        user = found[0]
        if user.isAdmin == True:
            return send_json(alreadyPromoted)
        found.update(isAdmin=True)
        return send_json(promoteSucceed)
from os import F_OK
from ..utils import decode_jwt, send_json
from ..models import User
from ..decorators import login_required
from ..responses import userDoesNotExist, ok, no

class IsAdminView(View):
    @login_required
    def get(self, request):
        session = request.session
        decoded = decode_jwt(session)
        userid = decoded['userid']
        found = User.objects.filter(id=userid)
        if found.count() != 1:
            return send_json(userDoesNotExist)
        user = found[0]
        if user.isAdmin:
            data = ok
        else:
            data = no
        return send_json(data)

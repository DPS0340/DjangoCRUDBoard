# JSON 응답 딕셔너리를 모아둔 코드

APIOnly = {
    'success': True,
    'status': 200,
    'comment': 'API Only'
}
postOnly = {
    'success': False,
    'status': 400,
    'comment': 'only POST allowed'
}
noUser = {
    'success': False,
    'status': 401,
    'comment': 'there\'s no matched user'
}
deleteUserSucceed = {
    'success': True,
    'status': 200,
    'comment': 'delete user succeed'
}
modifyUserSucceed = {
    'success': True,
    'status': 200,
    'comment': 'modify user succeed'
}
userAlreadyRegistered = {
    'success': False,
    'status': 403,
    'comment': 'User has already registered'
}
registerSucceed = {
    'success': True,
    'status': 200,
    'comment': 'register succeed'
}
userAlreadyLogin = {
    'success': False,
    'status': 400,
    'comment': 'User has already logged in'
}
userLogin = {
    'success': True,
    'status': 200,
    'comment': 'Login succeed'
}
userDoesNotExist = {
    'success': False,
    'status': 403,
    'comment': 'User does not exists'
}
userDoesNotMatch = {
    'success': False,
    'status': 403,
    'comment': 'Username and password does not match'
}
userAlreadyLogout = {
    'success': False,
    'status': 403,
    'comment': 'User has already logged out'
}
userLogout = {
    'success': True,
    'status': 200,
    'comment': 'Logout succeed'
}
loginRequired = {
    'success': False,
    'status': 401,
    'comment': 'not Authorized'
}
postSucceed = {
    'success': True,
    'status': 200,
    'comment': 'Post request succeed'
}


def getSucceedFunc(field): return {
    'success': True,
    'status': 200,
    'comment': f'obtaining {field} succeed'
}


boardRequired = {
    'success': False,
    'status': 400,
    'comment': 'Board argument required'
}
notImplemented = {
    'success': False,
    'status': 502,
    'comment': 'Not Implemented'
}
postingElementExists = {
    'success': False,
    'status': 400,
    'comment': 'Posting Element Exists'
}
boardDoesNotExists = {
    'success': False,
    'status': 400,
    'comment': 'Board does not exists'
}
illegalArgument = {
    'success': False,
    'status': 400,
    'comment': 'Illegal argument'
}
illegalModifyArgument = {
    'success': False,
    'status': 400,
    'comment': 'Illegal modify argument'
}
postRequired = {
    'success': False,
    'status': 400,
    'comment': 'Post argument required'
}
postDoesNotExists = {
    'success': False,
    'status': 400,
    'comment': 'Post does not exists'
}
replySucceed = {
    'success': True,
    'status': 200,
    'comment': 'reply request succeed'
}
ok = {
    'success': True,
    'status': 200,
    'comment': 'OK'
}
no = {
    'success': False,
    'status': 400,
    'comment': 'NO'
}
replyRequired = {
    'success': False,
    'status': 400,
    'comment': 'Reply argument required'
}
replyDoesNotExists = {
    'success': False,
    'status': 400,
    'comment': 'Reply does not exists'
}
answerReplyDoesNotExists = {
    'success': False,
    'status': 400,
    'comment': 'AnswerReply does not exists'
}
answerReplySucceed = {
    'success': True,
    'status': 200,
    'comment': 'AnswerReply request succeed'
}
deleteAnsreplySucceed = {
    'success': True,
    'status': 200,
    'comment': 'delete AnswerReply succeed'
}
changeAnswerReplySucceed = {
    'success': True,
    'status': 200,
    'comment': 'change AnswerReply succeed'
}
changeReplySucceed = {
    'success': True,
    'status': 200,
    'comment': 'change Reply succeed'
}
changePostSucceed = {
    'success': True,
    'status': 200,
    'comment': 'change Post succeed'
}
AnsDoesNotMatch = {
    'success': False,
    'status': 400,
    'comment': 'does not match the author'
}
replyDoesNotMatch = {
    'success': False,
    'status': 400,
    'comment': 'does not match the reply'
}
PostDoesNotMatch = {
    'success': False,
    'status': 400,
    'comment': 'does not match the post'
}
promoteSucceed = {
    'success': True,
    'status': 200,
    'comment': 'Promote request succeed'
}
alreadyPromoted = {
    'success': False,
    'status': 403,
    'comment': 'User has already promoted'
}

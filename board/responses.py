APIOnly = {
    'success': False,
    'status': 404,
    'comment': 'API Only'
}
postOnly = {
    'success': False,
    'status': 400,
    'comment': 'only POST allowed'
}
noUser = {
    'success': True,
    'status': 401,
    'comment': 'there\'s no matched user'
}
deleteUserSucceed = {
    'success': True,
    'status': 200,
    'comment': 'delete user succeed'
}
userAlreadyRegistered = {
    'success': True,
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
getSucceedFunc = lambda field: {
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
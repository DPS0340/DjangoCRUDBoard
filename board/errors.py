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
    'comment': 'User already registered'
}
registerSucceed = {
    'success': True,
    'status': 200,
    'comment': 'register succeed'
}
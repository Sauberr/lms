def cleanup_social_account(backend, uid, user=None, *args, **kwargs):
    user.avatar = kwargs['response']['picture']
    user.save()
    return {'user': user}

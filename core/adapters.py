from allauth.account.adapter import DefaultAccountAdapter


class NoSignupAccountAdapter(DefaultAccountAdapter):
    """An account adapter to disable signups, which twonum.org does not
    invite.
    """

    def is_open_for_signup(self, request):
        return False

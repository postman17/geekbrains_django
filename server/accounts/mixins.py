from django.shortcuts import redirect


class AdminRoleRequired:
    login_url = ''

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms([
            'product.add_product',
            'product.change_product',
        ]):
            return redirect(self.login_url)
        
        return super(AdminRoleRequired, self).dispatch(request, *args, **kwargs)

from django.contrib.auth.base_user import BaseUserManager



class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, username, password , **extra_fields):
        if not username:
            raise ValueError(_("Username must be set"))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password , **extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)
        return self.create_user(username, password, **extra_fields)
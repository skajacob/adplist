from django.contrib.auth.models import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, user_type, password=None):
        user = self.model(
            email=self.normalize_email(email),
            #username=username,
            user_type=user_type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, user_type):
        user = self.create_user(
            email=self.normalize_email(email),
            #username=username,
            password=password,
            user_type=user_type
    
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
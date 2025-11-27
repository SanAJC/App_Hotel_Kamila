from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager , PermissionsMixin

class MyAccountManager(BaseUserManager):
    def create_user(self,nombre_usuario,email,password, rol="gerente"):
        if not email:
            raise ValueError('el usuario debe tener un email')
     
        user=self.model(
            email=self.normalize_email(email),
            nombre_usuario=nombre_usuario,
            rol=rol,  
        )
        user.is_active=True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, nombre_usuario, email, password=None, rol="gerente"):
        user = self.create_user(
            nombre_usuario=nombre_usuario,
            email=email,
            password=password,
            rol=rol,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser ,PermissionsMixin):
    Roles = [
        ('gerente', 'gerente'),
        ('recepcionista', 'recepcionista'),
    ]
    nombre_usuario = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    rol = models.CharField(max_length=50, choices=Roles, default="gerente")

    # Campos adicionales requeridos por Django
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'nombre_usuario'
    REQUIRED_FIELDS = ['email', 'rol']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

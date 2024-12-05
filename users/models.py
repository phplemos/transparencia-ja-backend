from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Cria e salva um usuário com email e senha"""
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)

        # Criando o usuário com o campo 'email' e 'password' automaticamente
        user = self.model(email=email, **extra_fields)

        if password:
            user.set_password(password)  # Usa o 'set_password' para garantir que a senha seja criptografada
        else:
            raise ValueError("A senha é obrigatória")

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Cria e salva um superusuário com email e senha"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superusuário precisa ter is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superusuário precisa ter is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    papel = models.CharField(max_length=200, default="cidadao")
    pontos = models.FloatField(default=0.0)
    nivel = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome"]

    def __str__(self):
        return self.email


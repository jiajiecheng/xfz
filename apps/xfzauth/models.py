from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from shortuuidfield import ShortUUIDField
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, telephone, username, password, **kwargs):
        if not telephone:
            raise ValueError("请传递手机号码。")
        if not username:
            raise ValueError("请传递用户名")
        if not password:
            raise ValueError("请传递密码")
        user = self.model(telephone=telephone, username=username, **kwargs)
        user.set_password(password)
        return user

    def create_user(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone, username, password, **kwargs)

    def create_superuser(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(telephone, username, password, **kwargs)


# 重写Django提供的User类
class User(AbstractBaseUser, PermissionsMixin):
    # 不使用自增长主键
    # 使用uuid/shortuuid(保证字符的唯一性以及较少的存储占用)
    uid = ShortUUIDField(primary_key=True)
    email = models.CharField(unique=True, max_length=20)
    telephone = models.CharField(unique=True, max_length=11)
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=100)
    # 是否为普通用户
    is_staff = models.BooleanField(default=True)
    date_join = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = ['username']
    # 给指定用户发送邮件
    EMAIL_FIELD = 'email'
    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

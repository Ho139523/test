from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from utils.variables.countries import countries
from django.core.validators import MinLengthValidator, int_list_validator


class User(AbstractUser):
    special_user = models.DateTimeField(default=timezone.now)

    def is_special_user(self):
        return self.special_user > timezone.now()

    is_special_user.boolean = True
    is_special_user.short_description = "Special User"

    def save(self, *args, **kwargs):
        # Lowercase and trim the username before saving
        self.username = self.username.strip().lower()
        super().save(*args, **kwargs)

    # Make username queries case-insensitive
    def get_by_natural_key(self, username):
        return self.__class__.objects.get(username__iexact=username.strip())


class ProfileModel(models.Model):
    def default_tel_menu():
        return [
            "🧮 موجودی", "خرید با کد کالا", "🗂 دسته بندی ها",
            "🖥 بازدید سایت", "💬 پیام به پشتیبان", "تنظیمات ⚙"
        ]
    def default_extra_button_menu():
        return ["🔐     ایجاد حساب کاربری    🛡️",]
    
    def default_settings_menu():
        return ["فروشنده شو",]

    user = models.OneToOneField(User, unique=True, null=True, on_delete=models.SET_NULL, blank=True)
    fname = models.CharField(max_length=100, blank=True, null=True, verbose_name="First Name")
    lname = models.CharField(max_length=150, blank=True, null=True, verbose_name="Last Name")
    avatar = models.ImageField(
        default="registration/user_avatars/default-avatar.png",
        upload_to="registration/user_avatars"
    )
    background_pic = models.ImageField(
        default="registration/user_headers/default_header.avif",
        upload_to="registration/user_headers",
        verbose_name="Header Image"
    )
    birthday = models.DateField(blank=True, null=True)
    Phone = models.CharField(max_length=10, blank=True, null=True, verbose_name="Phone Number")
    about_me = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        default="Describe yourself, your capabilities and talents here. Let others know how awesome you are ;)",
        verbose_name="About Me"
    )
    instagram = models.CharField(max_length=120, unique=True, blank=True, null=True, verbose_name="Instagram ID")
    tweeter = models.CharField(max_length=120, unique=True, blank=True, null=True, verbose_name="Tweeter ID")
    telegram = models.CharField(max_length=120, unique=True, blank=True, null=True, verbose_name="Telegram ID")
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False, blank=True)
    tel_id = models.CharField(
        max_length=10,
        validators=[int_list_validator(sep=''), MinLengthValidator(10)],
        default='100000000',
        unique=True,
        null=False,
        blank=True
    )
    tel_menu = models.JSONField(default=default_tel_menu, blank=True, null=False)
    extra_button_menu = models.JSONField(default=default_extra_button_menu, blank=True, null=False)
    seller_mode = models.BooleanField(default=False, blank=False, null=False)
    settings_menu = models.JSONField(default=default_settings_menu, blank=True, null=False)
    
    shipping_line1 = models.CharField(max_length=40, blank=True, null=True, verbose_name="Address Line 1")
    shipping_line2 = models.CharField(max_length=40, blank=True, null=True, verbose_name="Address Line 2")
    shipping_country = models.CharField(max_length=10, choices=countries, blank=True, null=True, verbose_name="Country")
    shipping_city = models.CharField(max_length=10, blank=True, null=True, verbose_name="City")
    shipping_province = models.CharField(max_length=30, blank=True, null=True, verbose_name="Province")
    shipping_zip = models.CharField(max_length=10, blank=True, null=True, verbose_name="Zip Code")
    shipping_home_phone = models.CharField(max_length=8, blank=True, null=True, verbose_name="Residential Phone Number")

    class UserLevel(models.TextChoices):
        BLUE = 'blue', 'Blue User'
        GREEN = 'green', 'Green User'
        SILVER = 'silver', 'Silver User'
        GOLD = 'gold', 'Golden User'

    user_level = models.CharField(
        max_length=10,
        choices=UserLevel.choices,
        default=UserLevel.BLUE
    )

    LEVEL_MENUS = {
        'blue': [
        [
            "🧮 موجودی", "خرید با کد کالا", "🗂 دسته بندی ها",
            "🖥 بازدید سایت","💬 پیام به پشتیبان", "تنظیمات ⚙"
        ],
        ["🔐     ایجاد حساب کاربری    🛡️",],
        ["فروشنده شو", "افزودن آدرس پستی"],
        ],
        'green': [
        [
            "🧮 موجودی", "خرید با کد کالا", "🗂 دسته بندی ها",
            "🖥 بازدید سایت","💬 پیام به پشتیبان", "تنظیمات ⚙"
        ],
        [""],
        ["فروشنده شو", "تغییر آدرس پستی"],
        ],
        'silver': [
            "🧮 موجودی", "🛒 خرید سریع", "🖥 بازدید سایت", "💬 پیام به پشتیبان"
        ],
        'gold': [
            "💰 گزارش مالی", "🛒 خرید پیشرفته", "📊 تحلیل‌ها", "🖥 بازدید سایت"
        ],
        'seller': [
        [
            "افزودن کالا", "حذف کالا", "افزودن دسته بندی", "💰 گزارش مالی", "📊 تحلیل‌ها", "تنظیمات ⚙"
        ],
        ["آمار فروش"],
        ["بازگشت به حالت خریدار", "تغییر آدرس انبار"],
        ],
    }

    def __str__(self):
        return self.user.username if self.user else self.tel_id

    @property
    def age(self):
        if self.birthday:
            today = timezone.now().date()
            age = (
                today.year - self.birthday.year
                - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
            )
            return age
        return None

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = ProfileModel.objects.get(pk=self.pk)
            # Update tel_menu only when user_level changes
            if old_instance.user_level != self.user_level and self.user_level in self.LEVEL_MENUS:
                self.tel_menu = self.LEVEL_MENUS[self.user_level][0]
                self.extra_button_menu = self.LEVEL_MENUS[self.user_level][1]
                self.settings_menu = self.LEVEL_MENUS[self.user_level][2]
                
            if old_instance.seller_mode:
                self.tel_menu = self.LEVEL_MENUS["seller"][0]
                self.extra_button_menu = self.LEVEL_MENUS["seller"][1]
                self.settings_menu = self.LEVEL_MENUS["seller"][2]
                
            if not old_instance.seller_mode:
                self.tel_menu = self.LEVEL_MENUS[self.user_level][0]
                self.extra_button_menu = self.LEVEL_MENUS[self.user_level][1]
                self.settings_menu = self.LEVEL_MENUS[self.user_level][2]
                
        super().save(*args, **kwargs)

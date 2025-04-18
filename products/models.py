from django.db import models, transaction
from accounts.models import User, ProfileModel
from django.core.exceptions import ValidationError
import os


class CategoryModel(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Title')
    slug = models.SlugField(unique=True)  # Ensure the slug is unique
    status = models.BooleanField(default=True, verbose_name='Publish Status') 
    position = models.IntegerField(verbose_name='Position')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["position"]


class TutorialModel(models.Model):
    title = models.CharField(max_length=50, unique=True, blank=False, null=False, verbose_name='Title')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')  # Price field for tutorial
    video = models.FileField(upload_to='tutorial_videos/', verbose_name='Video')  # Upload location for videos
    video_poster = models.ImageField(upload_to='tutorial_posters/', verbose_name='Video Poster')  # Video poster image
    poster = models.ImageField(upload_to='tutorial_poster/', verbose_name='Tutorial Poster')  # Poster image
    about = models.TextField(max_length=5000, blank=False, null=False, verbose_name='Description')
    tag = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, verbose_name='Tag')  # ForeignKey to Tag model
    status = models.BooleanField(default=False, verbose_name='Publish Status')
    slug = models.SlugField(unique=True)  # Ensure the slug is unique
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tutorials_authored', verbose_name='Author')  # Tutorial author
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tutorials_taught', verbose_name='Teacher')  # Tutorial teacher
    attachment = models.FileField(upload_to='tutorial_attachments/', blank=True, null=True, verbose_name='Attachments')  # Optional attachment
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    installment = models.BooleanField(default=False, verbose_name='Installment Purchase')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = "Tutorial"
        verbose_name_plural = "Toturials"
        ordering = ["created"]
        
        
        
class ArticleModel(models.Model):
    title = models.CharField(max_length=50, unique=True, blank=False, null=False, verbose_name='Title')
    poster = models.ImageField(upload_to='article_poster/', verbose_name='Artilce Poster')  # Poster image
    context = models.TextField(max_length=5000, blank=False, null=False, verbose_name='Description')
    tag = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, verbose_name='Tag')  # ForeignKey to Tag model
    status = models.BooleanField(default=False, verbose_name='Publish Status')
    slug = models.SlugField(unique=True)  # Ensure the slug is unique
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article_authored', verbose_name='Author')  # Tutorial author
    attachment = models.FileField(upload_to='tutorial_attachments/', blank=True, null=True, verbose_name='Attachments')  # Optional attachment
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    time_takes = models.IntegerField(verbose_name='Time it takes to read it')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["created"]
    
    @property
    def required_time(self):
        hour = self.time_takes//60
        min =  self.time_takes-hour
        return [hour, min]




#class ShoeModel(models.Model):
#    title = models.CharField(max_length=100, unique=True, blank=False, null=False)
#    description = models.TextField(max_length=1000, unique=False, blank=True, null=True)
#    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preliminary price
#    size = models.IntegerField()
#    length = models.DecimalField(max_digits=3, decimal_places=1)
#    stock = models.BooleanField(default=True)
#    pic1 = models.ImageField(upload_to='shoes_image')
#    pic2 = models.ImageField(upload_to='shoes_image')
#    pic3 = models.ImageField(upload_to='shoes_image')
#    pic4 = models.ImageField(upload_to='shoes_image')
#
#

#    def __str__(self):
#

#    @property
#    def final_price(self):
#        """Calculate the price after applying the discount percentage."""
#        discount_amount = (self.price * self.off) / 100
#



class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Category Title')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    status = models.BooleanField(default=True, verbose_name='Publish Status')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories',
        verbose_name='Parent Category'
    )
    position = models.IntegerField(verbose_name='Position')
    stores = models.ManyToManyField('Store', blank=True, related_name='categories', verbose_name='Stores')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["position"]

    # Recursive method to get full hierarchy of parents
    def get_parents(self):
        parents = []
        category = self
        while category.parent:
            parents.append(category.parent)
            category = category.parent
        return parents

    def get_full_path(self):
        return " > ".join([parent.title for parent in reversed(self.get_parents())] + [self.title])

    def get_all_subcategories(self):
        subcategories = set()
        categories_to_check = [self]

        while categories_to_check:
            current = categories_to_check.pop()
            children = current.subcategories.all()
            subcategories.update(children)
            categories_to_check.extend(children)
        
        return subcategories
    
    def get_next_layer_categories(self):
        return self.subcategories.filter(status=True)

    # New to_dict method
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "slug": self.slug,
            "status": self.status,
            "parent": self.parent.title if self.parent else None,
            "position": self.position,
            "stores": [store.name for store in self.stores.all()]  # Assuming Store model has a name field
        }
        
    def save(self, *args, **kwargs):
        is_new = self.pk is None  # بررسی کنیم آیا دسته جدید است

        super().save(*args, **kwargs)  # ابتدا دسته جدید را ذخیره کنیم

        if is_new and self.parent:  # اگر دسته جدید است و والد دارد
            parent_category = self.parent

            if parent_category.products.exists():
                with transaction.atomic():
                    parent_category.products.update(category=self)  # انتقال محصولات به دسته جدید


        super().save(*args, **kwargs)  # ذخیره دسته‌بندی جدید



from django.db import models

class Product(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="profilemodel")
    name = models.CharField(max_length=100, verbose_name='Product Name')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    brand = models.CharField(max_length=50, blank=True, null=True, verbose_name='Brand')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Price')
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='Discount (%)')
    stock = models.PositiveIntegerField(default=0, verbose_name='Stock')
    status = models.BooleanField(default=True, verbose_name='Status')
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, related_name='products', verbose_name='Category'
    )
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    main_image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name='Main Image')
    additional_images = models.ManyToManyField('ProductImage', blank=True, related_name='product_images')
    code = models.CharField(max_length=10, unique=True, editable=False, blank=True)  # فیلد کد ده رقمی
    store = models.ForeignKey('Store', on_delete=models.CASCADE, related_name='product_store', verbose_name='Store')



    def __str__(self):
        return self.name

    @property
    def final_price(self):
        if self.discount > 0:
            discount_amount = (self.price * self.discount) / 100
            return self.price - discount_amount
        return self.price

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    def clean(self):
        """ بررسی اضافه کردن محصول به دسته‌بندی‌ای که دارای زیرمجموعه است """
        if self.category and self.category.get_next_layer_categories().exists():
            raise ValidationError(
                {'category': "This category includes subcategory. So you can't add product to it."}
            )

        if self.price < 10000:
            raise ValidationError({'price': 'قیمت نمی‌تواند کمتر از 10000 باشد.'})

    def save(self, *args, **kwargs):
        self.clean()  # اجرای اعتبارسنجی هنگام ذخیره
        if not self.code:
            product_code_counter, created = ProductCodeCounter.objects.get_or_create(id=1)
            self.code = product_code_counter.get_next_code()
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        # حذف تصویر اصلی از سیستم
        if self.main_image and os.path.isfile(self.main_image.path):
            os.remove(self.main_image.path)

        # حذف تمام تصاویر اضافی مرتبط و فایل‌های فیزیکی‌شان
        for image in self.image_set.all():  # توجه به related_name جدید
            if image.image and os.path.isfile(image.image.path):
                os.remove(image.image.path)
            image.delete()  # حذف رکورد از دیتابیس

        super().delete(*args, **kwargs)  # حذف خود محصول از دیتابیس


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/', verbose_name='Product Image')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image_set', verbose_name='Product')  # تغییر related_name

    def __str__(self):
        return f"Image: {self.id}"
        
    def delete(self, *args, **kwargs):
        # حذف فایل تصویر از سیستم
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        
        super().delete(*args, **kwargs)  # حذف رکورد از دیتابیس
        
        
        
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')
    key = models.CharField(max_length=50, verbose_name='Attribute Key')  # مثل "Weight" یا "Size"
    value = models.CharField(max_length=100, verbose_name='Attribute Value')  # مثل "1kg" یا "42"

    def __str__(self):
        return f"{self.key}: "
        

class ProductCodeCounter(models.Model):
    # برای مدیریت شمارنده کد محصولات
    counter = models.BigIntegerField(default=1, unique=True)

    def get_next_code(self):
        # افزایش شمارنده و بازگشت کد جدید
        self.counter += 1
        self.save()
        return f"{self.counter:010d}"  # فرمت ده رقمی

    def reset_counter(self, start_value=1):
        """
        بازنشانی شمارنده به مقدار اولیه (به‌صورت پیش‌فرض ۱)
        :param start_value: مقدار شروع جدید (پیش‌فرض ۱)
        """
        self.counter = start_value
        self.save()


        
class Store(models.Model):
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name="store")
    name = models.CharField(max_length=100, verbose_name='Store Name')
    address = models.CharField(max_length=255, verbose_name='Address')
    city = models.CharField(max_length=50, verbose_name='City')
    province = models.CharField(max_length=50, verbose_name='Province')
    logo = models.ImageField(upload_to="store_logos/", blank=True, null=True, verbose_name="Store Logo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"
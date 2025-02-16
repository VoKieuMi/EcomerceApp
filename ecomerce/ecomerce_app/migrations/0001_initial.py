# Generated by Django 4.2.11 on 2025-02-05 16:19

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('user', 'User'), ('admin', 'Admin'), ('staff', 'Staff'), ('seller', 'Seller')], default='user', max_length=20)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/avatar/%Y/%m/%d')),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('updated_data', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')], max_length=50)),
                ('payment', models.CharField(max_length=255)),
                ('status_payment', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('updated_data', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='products/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StoreCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('updated_data', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(max_length=255)),
                ('payment_method', models.CharField(max_length=255)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='ecomerce_app.order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('updated_data', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='ecomerce_app.storecategory')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SaleStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('updated_data', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('month', models.IntegerField()),
                ('quarter', models.IntegerField()),
                ('year', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_statistics', to='ecomerce_app.store')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('updated_data', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='ecomerce_app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='ecomerce_app.store')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('store_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_categories', to='ecomerce_app.storecategory')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecomerce_app.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecomerce_app.store'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('updated_data', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='ecomerce_app.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='ecomerce_app.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdminStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('updated_data', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('month', models.IntegerField()),
                ('quarter', models.IntegerField()),
                ('year', models.IntegerField()),
                ('sold', models.IntegerField()),
                ('total', models.IntegerField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_statistics', to='ecomerce_app.store')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

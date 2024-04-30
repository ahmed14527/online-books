# Generated by Django 5.0.4 on 2024-04-30 06:46

import django.core.validators
import django.db.models.deletion
import django_countries.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=17)),
                ('address_line_1', models.CharField(max_length=254)),
                ('address_line_2', models.CharField(blank=True, max_length=254, null=True)),
                ('zip', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('concluded', models.BooleanField(default=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('cart_total', models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)])),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=8, validators=[django.core.validators.MinValueValidator(0)])),
                ('original_cart', models.TextField(default='')),
                ('stripe_pid', models.CharField(default='', max_length=254)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.userprofile')),
            ],
            options={
                'ordering': ['-order_date'],
            },
        ),
        migrations.CreateModel(
            name='OrderSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('set_total', models.DecimalField(decimal_places=2, editable=False, max_digits=8)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartitems', to='checkout.order')),
            ],
        ),
    ]
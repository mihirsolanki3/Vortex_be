# Generated by Django 5.0.3 on 2024-03-27 10:41

import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import vortex_app.manager
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search_Retrieval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchengine', models.CharField(max_length=50)),
                ('content_api', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('source_id', models.AutoField(primary_key=True, serialize=False)),
                ('source_name', models.CharField(max_length=50)),
                ('api_endpoint', models.CharField(max_length=100)),
                ('apikey', models.CharField(max_length=50)),
            ],
        ),
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
                ('user_bio', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', vortex_app.manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('content_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('source_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('type', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Content_Moderation',
            fields=[
                ('moderation_id', models.AutoField(primary_key=True, serialize=False)),
                ('moderation_status', models.TextField()),
                ('moderation_date', models.DateTimeField(auto_now_add=True)),
                ('content_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='vortex_app.content')),
                ('moderator_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContentInteraction',
            fields=[
                ('interaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('interaction_type', models.CharField(max_length=50)),
                ('content_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='vortex_app.content')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_amount', models.FloatField()),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('ad_id', models.AutoField(primary_key=True, serialize=False)),
                ('ad_title', models.CharField(max_length=50)),
                ('ad_description', models.TextField()),
                ('ad_imageurl', models.CharField(max_length=100)),
                ('ad_linkurl', models.CharField(max_length=100)),
                ('ad_startdate', models.DateTimeField()),
                ('ad_enddate', models.DateTimeField()),
                ('adstatus_active', models.BooleanField(default=False)),
                ('adstatus_inactive', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('payment_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='vortex_app.payments')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('subscription_id', models.AutoField(primary_key=True, serialize=False)),
                ('subscription_type', models.CharField(max_length=50)),
                ('subscription_status', models.CharField(max_length=100)),
                ('subscription_startdate', models.DateTimeField()),
                ('subscription_enddate', models.DateTimeField()),
                ('payment_amount', models.FloatField()),
                ('payment_date', models.DateTimeField()),
                ('payment_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='vortex_app.payments')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
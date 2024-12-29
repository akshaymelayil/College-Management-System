# Generated by Django 5.1.3 on 2024-12-05 20:45

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('dob', models.DateField(default='2000-01-01')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='', max_length=15)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10)),
                ('nationality', models.CharField(default='Unknown', max_length=50)),
                ('address', models.TextField(default='')),
                ('academic_details', models.TextField(default='Not Provided')),
                ('qualification', models.CharField(default='Not Specified', max_length=100)),
                ('course', models.CharField(default='Not Selected', max_length=50)),
                ('documents', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='faculties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.CharField(max_length=20, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('department', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=128)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='faculty_photos/')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('category_key', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('nationality', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('course', models.CharField(choices=[('BTech', 'Computer Science Engineering'), ('MTech_Civil', 'Civil Engineering'), ('MTech_EEE', 'Electrical and Electronics Engineering'), ('MTech_Marine', 'Marine Engineering'), ('MTech_AI', 'AI & ML Engineering'), ('MTech_Robotics', 'Robotics Engineering')], max_length=20)),
                ('documents', models.FileField(upload_to='admissions/documents/')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='students/photos/')),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoursePlanning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('timing', models.TimeField()),
                ('study_plan', models.TextField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeweb.faculties')),
            ],
        ),
        migrations.CreateModel(
            name='FacultyAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeweb.faculties')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('month', models.CharField(max_length=15)),
                ('year', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Recieved', 'Recieved'), ('Pending', 'Pending')], max_length=10)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeweb.faculties')),
            ],
        ),
        migrations.CreateModel(
            name='Grievance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('response', models.TextField(blank=True, null=True)),
                ('resolved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resolved_grievances', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grievances', to='collegeweb.students')),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fees', to='collegeweb.students')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(max_length=200)),
                ('issued_by', models.CharField(max_length=100)),
                ('issue_date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='collegeweb.students')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='collegeweb.students')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('attendance', models.FloatField(default=0.0)),
                ('subject_1', models.CharField(blank=True, max_length=100, null=True)),
                ('marks_1', models.IntegerField(blank=True, null=True)),
                ('subject_2', models.CharField(blank=True, max_length=100, null=True)),
                ('marks_2', models.IntegerField(blank=True, null=True)),
                ('subject_3', models.CharField(blank=True, max_length=100, null=True)),
                ('marks_3', models.IntegerField(blank=True, null=True)),
                ('subject_4', models.CharField(blank=True, max_length=100, null=True)),
                ('marks_4', models.IntegerField(blank=True, null=True)),
                ('subject_5', models.CharField(blank=True, max_length=100, null=True)),
                ('marks_5', models.IntegerField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='academic_details', to='collegeweb.students')),
            ],
        ),
    ]

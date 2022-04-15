import datetime
from django.db import models
import uuid
from django.db import models, transaction
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager)
from django.utils import timezone


class Role(models.Model):
    IS_SUPERADMIN = 1
    IS_ADMIN = 2
    IS_TEACHER = 3
    IS_STUDENT = 4

    ROLE_CHOICES = (
        (IS_SUPERADMIN, 'is_superadmin'),
        (IS_ADMIN, 'is_admin'),
        (IS_TEACHER, 'is_teacher'),
        (IS_STUDENT, 'is_student')
    )
    ROLES_CHOICES = (
        ('SUPERADMIN', 'is_superadmin'),
        ('ADMIN', 'is_admin'),
        ('TEACHER', 'is_teacher'),
        ('STUDENT', 'is_student')
    )

    id = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, primary_key=True)
    name = models.CharField(
        max_length=50, choices=ROLES_CHOICES, blank=True, null=True)

    def __str__(self):
        return str(self.name)
    
    
    
class UserManager(BaseUserManager):

    def _create_user(self, contact, password, **extra_fields):
        if not contact:
            raise ValueError('The given contact must be set')
        try:
            with transaction.atomic():
                user = self.model(contact=contact, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, contact, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(contact, password, **extra_fields)

    def create_superuser(self, contact, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('roles_id', 1)

        return self._create_user(contact, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=100,unique=True,default='abc@xyz.com')
    roles = models.ForeignKey(Role, on_delete=models.CASCADE, default=4)
    contact = models.BigIntegerField(default=0, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return str(self.email)

    class Meta:
        ordering = ['-date_joined']

    
class Branch(models.Model):
    name = models.CharField(max_length=50, unique=True)
    details = models.TextField(null=True,blank=True)
    
    class Meta:
        db_table = 'student_branch'
        
    def __str__(self):
        return f'{self.name}'
class Semester(models.Model):
    Academic_Year = models.DateField(null=True, blank=True)
    semester_number = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'student_semester'
    
    def __str__(self):
        return f'{self.semester_number} Semester of ACADEMIC YEAR {datetime.datetime.strftime(self.Academic_Year,"%Y")}'
        
class Syllabus(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,null=True,blank=True)
    sem = models.ForeignKey(Semester, on_delete=models.CASCADE,null=True,blank=True)
    details = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'syllabus_table'

    def __str__(self):
        return f'{self.branch} {self.sem}'

class Section(models.Model):
    name = models.CharField(max_length=5,null=True,blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE,null=True,blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,null=True,blank=True)
    
    class Meta:
        db_table = 'section'
        
    def __str__(self):
        return f'{self.name} {self.semester} {self.branch}'
class Student(models.Model):
    user = models.ForeignKey(User, related_name='student', on_delete=models.CASCADE)
    student_id = models.BigIntegerField(unique=True,null=True)
    name = models.CharField(max_length=50,blank=True, null=True)
    section = models.ForeignKey(Section, null=True, blank=True, on_delete=models.CASCADE)
    roll_no = models.SmallIntegerField(null=True, blank=True)
    profile_image = models.ImageField(
        upload_to='student_profile_image', null=True, blank=True)
    class Meta:
        db_table = 'student'
    
    def __str__(self):
        return self.name + ' ' + str(self.student_id)
    

class Teacher(models.Model):
    user = models.ForeignKey(User, related_name='teacher', on_delete=models.CASCADE)
    employee_id = models.BigIntegerField(unique=True,null=True)
    name = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        upload_to='teacher_profile_image',
        null=True,blank=True
    )
    details = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'teacher'
        
    def __str__(self):
        return f'{self.name} {self.employee_id}'
    
    
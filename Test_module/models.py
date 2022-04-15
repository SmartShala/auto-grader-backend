from django import db
from django.db import models
from users.models import (
    Branch, Section, Teacher,
    Student,Semester, User,
)
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import now

class Subject(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    detail = models.TextField(null=True,blank=True)
    
    class Meta:
        db_table = 'subjects'
        
    def __str__(self):
        return f'{self.name}'
    
class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    detail = models.TextField(max_length=1000,null=True,blank=True)
    
    class Meta:
        db_table = 'subject_topics'
        
    def __str__(self):
        return f'{self.subject.name} :: {self.name}'

# Create your models here.
class Assignment(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    assigned_by = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True,blank=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    submit_by = models.DateTimeField(null=True,blank=True)
    details = models.TextField(null=True, blank=True)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,null=True, blank=True)
    total_marks = models.IntegerField(default=0,null=True, blank=True)    
    submissions = models.IntegerField(default=0,null=True, blank=True)
    class Meta:
        db_table = 'assignments'
        
    def __str__(self):
        return f'{self.name} : C: {self.created_at}'


class AssignmentAssigner(models.Model):
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE,null=True,blank=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True,blank=True)
    section = models.ForeignKey(Section,on_delete=models.CASCADE,null=True,blank=True)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE,null=True,blank=True)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True,blank=True)
    
    class Meta:
        db_table = 'assignment_assigner'
        
    def __str__(self):
        return f'{self.assignment}'

class Questions(models.Model):
    question = models.TextField(null=True,blank=True)
    marks = models.IntegerField(default=0,null=True, blank=True)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,
                                   blank=True,related_name='user_added')
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    updated_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,
                                   blank=True,related_name='user_updated')
    Default_answer = models.TextField(null=True, blank=True)
    multiple_choices = ArrayField(models.CharField(max_length=200),null=True)
    is_mcq = models.BooleanField(default=False)
    is_code = models.BooleanField(default=False)
    is_descriptive = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'assignment_questions'
        
    def __str__(self):
        return f'{self.question} [{self.marks}]'
    

class StudentAssignmentAns(models.Model):
    assignment = models.ForeignKey(Assignment,on_delete=models.SET_NULL,null=True,blank=True)
    student = models.ForeignKey(Student,on_delete=models.SET_NULL,null=True,blank=True)
    is_submitted = models.BooleanField(default=False,null=True, blank=True)
    submit_time = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'student_assignments'
        
    def __str__(self):
        return f'{self.assignment} {self.student}'
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_submitted and self.submit_time is not None:
            self.submit_time = now()
        super().save(force_insert,force_update,using,update_fields)
        

class StudentAnswers(models.Model):
    student_assignment = models.ForeignKey(StudentAssignmentAns,on_delete=models.CASCADE,null=True,blank=True)
    question = models.ForeignKey(Questions,on_delete=models.CASCADE,null=True,blank=True)
    answer = models.TextField(blank=True,null=True)
    is_locked = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'student_answers'
        
    def __str__(self):
        return f'{self.student_assignment} f{self.question}'
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.student_assignment is not None:
            if self.student_assignment.is_submitted:
                self.is_locked = True
        
        if self.is_locked:
            return None
        super().save(force_insert, force_update, using, update_fields)
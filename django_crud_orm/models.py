from django.db import models
from django.utils import timezone

#User Model
class User(models.Model):
    first_name = models.CharField(null=False,max_length=30,default="john")
    last_name = models.CharField(null=False,max_length=30,default="doe")
    dob = models.DateField(null=True)
    email = models.CharField(null=False,max_length=30,default="<email>")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#Instructor model
class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    # Create a toString method for object string representation
    def __str__(self):
        return f'First name:{self.first_name}, Last name:{self.last_name}, Is full time:{str(self.full_time)}, Total Learners:{str(self.total_learners)}'

#Learner Model
class Learner(User):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENCE = 'data_science'
    DATABASE_ADMIN = 'dba'
    occupation_choices=[
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENCE, 'Data Science'),
        (DATABASE_ADMIN, 'Database Admin'),
    ]
    occupation = models.CharField(null=False,
                                  max_length=20,
                                  choices=occupation_choices,
                                  default=STUDENT)
    # Social link URL field
    social_link = models.URLField(max_length=200)

    # Create a toString method for object string representation
    def __str__(self):
        return (
            "First name: " + self.first_name + ", " +
            "Last name: " + self.last_name + ", "
            "Date of Birth: " + str(self.dob) + ", " +
            "Occupation: " + self.occupation + ", " +
            "Social Link: " + self.social_link)

#Course Model
class Course(models.Model):
    name = models.CharField(null=False,max_length=100,default="online course")
    description = models.CharField(max_length=500)

    # Many-To-Many relationship with Learner via Enrollment relationship
    learners = models.ManyToManyField(Learner,through='Enrollment')
    # Many-To-Many relationship with Instructors
    instructors = models.ManyToManyField(Instructor)

    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description

#Lesson model
class Lesson(models.Model):
    title = models.CharField(max_length=200,default="title")
    course = models.ForeignKey(Course,null=True,on_delete=models.CASCADE)
    content = models.TextField()


# Enrollment model as a lookup table with additional enrollment info
class Enrollment(models.Model):
        AUDIT = 'audit'
        HONOR = 'honor'
        COURSE_MODES = [
            (AUDIT, 'Audit'),
            (HONOR, 'Honor'),
        ]
        # Add a learner foreign key
        learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
        # Add a course foreign key
        course = models.ForeignKey(Course, on_delete=models.CASCADE)
        # Enrollment date
        date_enrolled = models.DateField(default=timezone.now)
        # Enrollment mode
        mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)





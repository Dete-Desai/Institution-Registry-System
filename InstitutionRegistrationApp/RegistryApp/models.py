
from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.

#Patient Registration Form db
class patientregistrationformdb(models.Model):
    hospital_id = models.CharField(primary_key=True, max_length=50)
    hospital_name = models.CharField(max_length=30)
    id_birth_number = models.CharField(max_length=30)
    nhif_number = models.CharField(max_length=30)
    patient_name = models.CharField(max_length=30)

    def __str__(self):
        return "{}-{}".format(self.hospital_id, self.hospital_name,self.id_birth_number, self.nhif_number,self.patient_name)
        #return self.id

#Student Registration Form db
class studentregistrationformdb(models.Model):
    school_id = models.CharField(primary_key=True, max_length=50)
    school_name = models.CharField(max_length=30)
    student_name = models.CharField(max_length=30)
    student_pupil_id_birth_number = models.CharField(max_length=30)
    student_pupil_number = models.CharField(max_length=30)
    grade_year_number = models.CharField(max_length=30)

    def __str__(self):
        return "{}-{}".format(self.school_id, self.school_name,self.student_name, self.student_pupil_id_birth_number,self.student_pupil_number,self.grade_year_number)
        #return self.id

#Hospital Staff Registration Form db
class hospitalstaffregistrationformdb(models.Model):
    hospital_clinic_id = models.CharField(primary_key=True, max_length=50)
    national_passport_id = models.CharField(max_length=50)
    staff_work_id = models.CharField(max_length=50)
    hospital_clinic_name = models.CharField(max_length=30)
    staff_name = models.CharField(max_length=30)
    staff_role = models.CharField(max_length=30)

    def __str__(self):
        return "{}-{}".format(self.hospital_clinic_id, self.national_passport_id,self.staff_work_id, self.hospital_clinic_name,self.staff_name,self.staff_role)
        #return self.id

#School Staff Registration Form db
class schoolstaffregistrationformdb(models.Model):
    school_id = models.CharField(primary_key=True, max_length=50)
    school_name = models.CharField(max_length=30)
    national_passport_id = models.CharField(max_length=50)
    staff_work_id = models.CharField(max_length=50)
    staff_name = models.CharField(max_length=30)
    staff_role = models.CharField(max_length=30)

    def __str__(self):
        return "{}-{}".format(self.school_id, self.school_name,self.national_passport_id, self.staff_work_id,self.staff_name,self.staff_role)
        #return self.id

#Hospital Registration Form db
HOSPITAL_TYPE_CHOICES = (
    ('general', 'General'),
    ('special', 'Special'),
    ('rehabilitationandchronicdisease', 'Rehabilitation and Chronic Disease'),
    ('psychiatric', 'Psychiatric '),
)

HOSPITAL_LEVEL_CHOICES = (
    ('level1', 'LEVEL 1'),
    ('level2', 'LEVEL 2'),
    ('level3', 'LEVEL 3'),
    ('level4', 'LEVEL 4'),
    ('level5', 'LEVEL 5'),
    ('level6', 'LEVEL 6'),
)

HOSPITAL_RESPONSE_CHOICES = (
    ('yes', 'YES'),
    ('no', 'NO'),
)


class hospitalregistrationformdb(models.Model):
    hospital_id = models.CharField(primary_key=True, max_length=50)
    hospital_name = models.CharField(max_length=30)
    hospital_type = models.CharField(max_length=15, choices=HOSPITAL_TYPE_CHOICES, default='level1')
    hospital_level = models.CharField(max_length=8, choices=HOSPITAL_LEVEL_CHOICES, default='higherlevel')
    hospital_registration_response_one = models.CharField(max_length=4, choices=HOSPITAL_RESPONSE_CHOICES, default='yes')
    hospital_registration_response_two = models.CharField(max_length=4, choices=HOSPITAL_RESPONSE_CHOICES, default='yes')
    hospital_registration_response_three = models.CharField(max_length=4, choices=HOSPITAL_RESPONSE_CHOICES, default='yes')
    hospital_registration_response_four = models.CharField(max_length=4, choices=HOSPITAL_RESPONSE_CHOICES, default='yes')
    hospital_registration_response_five = models.CharField(max_length=4, choices=HOSPITAL_RESPONSE_CHOICES, default='yes')
    hospital_registration_response_six = models.CharField(max_length=4, choices=HOSPITAL_RESPONSE_CHOICES, default='yes')
    hospital_registration_response_seven = models.CharField(max_length=4, choices=HOSPITAL_RESPONSE_CHOICES, default='yes')
    hospital_registration_response_eight = models.CharField(max_length=4, choices=HOSPITAL_RESPONSE_CHOICES, default='yes')
    hospital_registration_response_nine = models.CharField(max_length=4, choices=HOSPITAL_RESPONSE_CHOICES, default='yes')
    hospital_registration_response_ten = models.CharField(max_length=4, choices=HOSPITAL_RESPONSE_CHOICES, default='yes')

    def __str__(self):
        return "{}-{}".format(self.hospital_id, self.hospital_name,self.hospital_type, self.hospital_level)
        #return self.id

#Hospital Registration Form db
SCHOOL_TYPE_CHOICES = (
    ('university', 'University'),
    ('highschool', 'High School'),
    ('primary', 'Primary'),
    ('kindergarten', 'Kindergarten '),
)

SCHOOL_LEVEL_CHOICES = (
    ('higherinstitution', 'Higher Institution'),
    ('middleinstitution', 'Middle Institution'),
    ('lowerinstitution', 'Lower Institution'),
)

SCHOOL_RESPONSE_CHOICES = (
    ('yes', 'YES'),
    ('no', 'NO'),
)

class schoolsregistrationformdb(models.Model):
    school_id = models.CharField(primary_key=True, max_length=50)
    school_name = models.CharField(max_length=30)
    school_type = models.CharField(max_length=15, choices=SCHOOL_TYPE_CHOICES, default='university')
    school_level = models.CharField(max_length=8, choices=SCHOOL_LEVEL_CHOICES, default='higherinstitution')
    school_registration_response_one = models.CharField(max_length=4, choices=SCHOOL_RESPONSE_CHOICES, default='yes')
    school_registration_response_two = models.CharField(max_length=4, choices=SCHOOL_RESPONSE_CHOICES, default='yes')
    school_registration_response_three = models.CharField(max_length=4, choices=SCHOOL_RESPONSE_CHOICES, default='yes')
    school_registration_response_four = models.CharField(max_length=4, choices=SCHOOL_RESPONSE_CHOICES, default='yes')
    school_registration_response_five = models.CharField(max_length=4, choices=SCHOOL_RESPONSE_CHOICES, default='yes')
    school_registration_response_six = models.CharField(max_length=4, choices=SCHOOL_RESPONSE_CHOICES, default='yes')
    school_registration_response_seven = models.CharField(max_length=4, choices=SCHOOL_RESPONSE_CHOICES, default='yes')
    school_registration_response_eight = models.CharField(max_length=4, choices=SCHOOL_RESPONSE_CHOICES, default='yes')
    school_registration_response_nine = models.CharField(max_length=4, choices=SCHOOL_RESPONSE_CHOICES, default='yes')
    school_registration_response_ten = models.CharField(max_length=4, choices=SCHOOL_RESPONSE_CHOICES, default='yes')

    def __str__(self):
        return "{}-{}".format(self.school_id, self.school_name,self.school_type, self.school_level)
        #return self.id
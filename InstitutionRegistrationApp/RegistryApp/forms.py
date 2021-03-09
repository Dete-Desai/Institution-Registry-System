from .models import schoolsregistrationformdb
from .models import hospitalregistrationformdb
from .models import schoolstaffregistrationformdb
from .models import hospitalstaffregistrationformdb
from .models import studentregistrationformdb
from .models import patientregistrationformdb
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)

from crispy_forms.helper import FormHelper

User = get_user_model()


class patientregistration_form(forms.ModelForm):

    class Meta:
        model = patientregistrationformdb
        fields = (
            'hospital_id',
            'hospital_name',
            'id_birth_number',
            'nhif_number',
            'patient_name'
        )
        labels = {
            'hospital_id': '',
            'hospital_name': '',
            'id_birth_number': '',
            'nhif_number': '',
            'patient_name': ''
        }


class studentregistration_form(forms.ModelForm):

    class Meta:
        model = studentregistrationformdb
        fields = (
            'school_id',
            'school_name',
            'student_name',
            'student_pupil_id_birth_number',
            'student_pupil_number',
            'grade_year_number'
        )
        labels = {
            'school_id': '',
            'school_name': '',
            'student_name': '',
            'student_pupil_id_birth_number': '',
            'student_pupil_number': '',
            'grade_year_number': ''
        }


class hospitalstaffregistration_form(forms.ModelForm):

    class Meta:
        model = hospitalstaffregistrationformdb
        fields = (
            'hospital_clinic_id',
            'national_passport_id',
            'staff_work_id',
            'hospital_clinic_name',
            'staff_name',
            'staff_role'
        )
        labels = {
            'hospital_clinic_id': '',
            'national_passport_id': '',
            'staff_work_id': '',
            'hospital_clinic_name': '',
            'staff_name': '',
            'staff_role': ''
        }


class schoolstaffregistration_form(forms.ModelForm):

    class Meta:
        model = schoolstaffregistrationformdb
        fields = (
            'school_id',
            'school_name',
            'national_passport_id',
            'staff_work_id',
            'staff_name',
            'staff_role',
        )
        labels = {
            'school_id': '',
            'school_name': '',
            'national_passport_id': '',
            'staff_work_id': '',
            'staff_name': '',
            'staff_role': '',
        }


class hospitalregistration_form(forms.ModelForm):

    class Meta:
        model = hospitalregistrationformdb
        fields = (
            'hospital_id',
            'hospital_name',
            'hospital_type',
            'hospital_level',
            'hospital_registration_response_one',
            'hospital_registration_response_two',
            'hospital_registration_response_three',
            'hospital_registration_response_four',
            'hospital_registration_response_five',
            'hospital_registration_response_six',
            'hospital_registration_response_seven',
            'hospital_registration_response_eight',
            'hospital_registration_response_nine',
            'hospital_registration_response_ten'
        )
        labels = {
            'hospital_id': '',
            'hospital_name': '',
            'hospital_type': '',
            'hospital_level': '',
            'hospital_registration_response_one': '',
            'hospital_registration_response_two': '',
            'hospital_registration_response_three': '',
            'hospital_registration_response_four': '',
            'hospital_registration_response_five': '',
            'hospital_registration_response_six': '',
            'hospital_registration_response_seven': '',
            'hospital_registration_response_eight': '',
            'hospital_registration_response_nine': '',
            'hospital_registration_response_ten': '',
        }


class schoolsregistration_form(forms.ModelForm):

    class Meta:
        model = schoolsregistrationformdb
        fields = (
            'school_id',
            'school_name',
            'school_type',
            'school_level',
            'school_registration_response_one',
            'school_registration_response_two',
            'school_registration_response_three',
            'school_registration_response_four',
            'school_registration_response_five',
            'school_registration_response_six',
            'school_registration_response_seven',
            'school_registration_response_eight',
            'school_registration_response_nine',
            'school_registration_response_ten'
        )
        labels = {
            'school_id': '',
            'school_name': '',
            'school_type': '',
            'school_level': '',
            'school_registration_response_one': '',
            'school_registration_response_two': '',
            'school_registration_response_three': '',
            'school_registration_response_four': '',
            'school_registration_response_five': '',
            'school_registration_response_six': '',
            'school_registration_response_seven': '',
            'school_registration_response_eight': '',
            'school_registration_response_nine': '',
            'school_registration_response_ten': '',
        }

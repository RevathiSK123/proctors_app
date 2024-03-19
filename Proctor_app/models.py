from django.db import models


# Create your models here.
class Student(models.Model):
    std_id = models.CharField(max_length=20, primary_key=True)
    std_name = models.CharField(max_length=100)
    std_dept = models.CharField(max_length=20)
    std_phone= models.CharField(max_length=20)
    
    def _str_(self):
        return f"Student {self.std_id} - {self.std_name}"
    
class Proctor(models.Model):
    pctr_id = models.CharField(primary_key=True,max_length=100)
    pctr_name = models.CharField(max_length=15)
    pctr_phone=models.CharField(max_length=15)
    pctr_dept = models.CharField(max_length=20)
    std_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    def _str_(self):
        return f"Proctor {self.pctr_id} - {self.pctr_name}"


class Parent(models.Model):
    par_name = models.CharField(max_length=100)
    par_phone = models.CharField(max_length=15)
    par_address = models.TextField()
    std_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.par_name} - Parent of {self.std_id.std_name}"
 
class Faculty(models.Model):
    fac_id = models.CharField(primary_key=True,max_length=100)
    fac_dept = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def _str_(self):
        return f"Faculty {self.fac_id} - {self.fac_dept}" 
    
class Department(models.Model):
    dept_id = models.CharField(primary_key=True,max_length=100)
    std_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    fac_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    dept_name = models.CharField(max_length=100)

    def _str_(self):
        return f"Department {self.dept_id} - {self.dept_name}"

class HOD(models.Model):
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='hod_dept_id')
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='hod_dept_name')

    def _str_(self):
        return f"HOD - {self.dept_name}"
from django.db import models

# Create your models here.
class Course(models.Model):
    # add columns to our table
    created_at = models.DateTimeField(auto_now_add=True)#add now msg? when item created
    title = models.CharField(max_length=225)
    description = models.TextField()

    #defines this thing turns into a string
    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, default='')
    order = models.IntegerField(default=0) #order of step
    course = models.ForeignKey(Course) # a column that points to a record in a different table

    class Meta:
        ordering = ['order',]
        #this tells django to order all our records by the order attribute

    def __str__(self):
        return self.title

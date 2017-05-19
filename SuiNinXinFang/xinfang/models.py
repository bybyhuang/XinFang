from django.db import models

# Create your models here.

class Message(models.Model):
    title = models.CharField(max_length=200,verbose_name='标题')
    content = models.CharField(max_length=10000,verbose_name='内容')



class User(models.Model):
    name = models.CharField(max_length=100,verbose_name='姓名')
    phone = models.CharField(max_length=11,verbose_name='手机号')
    password = models.CharField(max_length=50,verbose_name='密码')

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100,verbose_name='区域名称')
    def __str__(self):
        return self.name

class CaseState(models.Model):
    stateName = models.CharField(max_length=100,verbose_name='化解状态')
    def __str__(self):
        return self.stateName

class Case(models.Model):
    reportName = models.CharField(max_length=100,verbose_name='反映人姓名')
    adress = models.CharField(max_length=200,verbose_name='反映人住址')
    question = models.TextField(verbose_name='反映的问题')
    belongUnit = models.CharField(max_length=200,verbose_name='责任单位')
    remark = models.TextField(verbose_name="备注")
    belongArea = models.ForeignKey(Area,verbose_name="所属区域")
    belongUserId = models.ForeignKey(User,verbose_name='县包案领导')
    state = models.ForeignKey(CaseState,verbose_name="目前化解的情况")
    creatTime = models.DateTimeField(verbose_name="创建时间")
    finishTime = models.DateTimeField(verbose_name='化解完成时间',blank=True)





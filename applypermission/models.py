from django.db import models

# Create your models here.
'''维护授权码和公司的对应关系'''
class AuthCode(models.Model):
    '''授权码'''
    AuthCode = models.CharField(max_length=50,primary_key=True)
    '''公司名称'''
    CompanyName = models.CharField(max_length=50)
    '''是否已使用'''
    flag = models.BooleanField(default=False)

'''用户注册表'''
class UerInfo(models.Model):
    '''授权码外键'''
    CompanyAuthCode = models.CharField(max_length=50)
    '''用户昵称'''
    NickName = models.CharField(max_length=24)
    '''密码'''
    password = models.CharField(max_length=50)
    '''手机号'''
    PhoneNum = models.CharField(max_length=11,primary_key =True)


class SrRequest(models.Model):
    '''自增id号'''
    ID = models.AutoField(primary_key =True)
    '''标题'''
    title = models.CharField(max_length=100)
    '''详细描述'''
    DetailDescrip = models.CharField(max_length=400)
    '''紧急情况'''
    ugency =models.CharField(max_length=20)
    '''deadline'''
    DueDate = models.DateTimeField()
    '''SR状态'''
    status = models.CharField(max_length=20)
    '''创建时间'''
    CreateDate=models.DateTimeField()
    '''修改时间'''
    ModifyDate=models.DateTimeField()

'''记录附件的存放路径，PicID为SrRequest里的ID'''
class PicRelated(models.Model):
    PicID = models.CharField(max_length=50)
    path = models.CharField(max_length=100)





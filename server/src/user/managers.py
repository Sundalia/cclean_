from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
  
  def _create_user(self, username=None, email=None, mobile=None, password=None, **extra_fields):
    
    if extra_fields.is_customer == True:
      extra_fields.is_cleaner=False
      
      
      
    if extra_fields.is_cleaner == True:
      extra_fields.is_customer=False
      
    if not username:
        if not mobile:
            raise ValueError('Заполните номер телефона')


    if mobile:
        if not username:
            username = mobile

        user = self.model(
            username=username,
            mobile=mobile,
            **extra_fields
        )
        
    if extra_fields.get('is_superuser'):
        user = self.model(
            username=username,
            **extra_fields
        )

    user.set_password(password)
    user.save(using=self._db)
    return user
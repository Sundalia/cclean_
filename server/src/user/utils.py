from .smsc_api import *

def send_sms(mobile, otp):
  smsc = SMSC()
  number = ''.join(('+',mobile))
  print(number, otp)
  send_sms = smsc.send_sms(phones=number, message=f'C-clean: {str(otp)} - Ваш одноразовый пароль для входа', sender='ccleanspb', format=0)
  return send_sms
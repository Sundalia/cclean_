import pyotp
from datetime import datetime, timedelta
from sms import send_sms


def send_otp(request):
  totp = pyotp.TOTP(pyotp.random_base32(), interval=60)
  otp = totp.now()
  request.session['otp_secret_key'] = totp.secret
  valid_date = datetime.now() + timedelta(minutes=1)
  request.session['otp_valid_date'] = str(valid_date)
  
  
  print(f'Cclean код для входа: {otp}')
  send_sms(
    f'Cclean код для входа: {otp}',
    'CClean',
    ['+79048459366'],
    fail_silently=False
  )
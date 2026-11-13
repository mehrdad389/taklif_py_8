"""
in the name of god
l_4
"""
#L_4_0

number = int(input('yek adad vared konid:'))
if number>0:
    print('adad mosbat ast')
elif number<0:
    print('adad mani ast')
else:
    print('adad 0 ast')
    
if number % 2 == 0:
   print('adad zoj ast')
else:
    print ('adad manfi ast')
    
#=======================================
#=======================================
#=======================================

#L_4_1
battery_level = int(input('dasad battery ra vared konid:'))
if battery_level <=20:
    print('sharjher ra vasl konid')
print('barrasi tamam shod.')

#=======================================
#=======================================
#=======================================

#L_4_2

stock = int(input('mojoodi ra vared konid:'))
if stock <= 0 :
    print('emkane kharid vojood darad.')
else:
    print('mahsool namojood ast.')

#=======================================
#=======================================
#=======================================

#L_4_3

price = int(input('mablaghe kharid ra vared konid:'))
if price >= 1000000:
    shipping = 0
   
elif price >= 500000:    
    shipping = 30000
   
else:    
    shipping = 60000
total_price = price + shipping
print('jame kol:',total_price)
print('hazine ersal:',shipping,'tooman')
    
    
#=======================================
#=======================================
#=======================================

#L_4_4    
#===================1=========================    
password = input('passwort ra vared konid:')
if len (password) < 8:
    print('ramz kootah ast.')    
if password.isdigit():
    print('password faghat adad ast.') 
if ' ' in password:
    print('password daraye fasele ast.')
    
#====================2========================    
   
password = input('passwort ra vared konid:')
if len (password) < 8:
    print('ramz kootah ast.')
    if password.isdigit():
        print('password faghat adad ast.') 
    if ' ' in password:
        print('password daraye fasele ast.')
else:
    print('moafag boob')
    
#====================3========================      

password = input('passwort ra vared konid:')
if len (password) < 8:
    print('ramz kootah ast.')
elif password.isdigit():
        print('password faghat adad ast.') 
elif ' ' in password:
        print('password daraye fasele ast.')
else:
    print('moafag boob')


#=======================================
#=======================================
#=======================================

#L_4_5

users = ["ali", "sara", "reza", "maryam"] 
user_name = input('name karbari ra vared konid')
if user_name in users:
   password = input('ramz ra vared konid:')
   if password == 'python123':
       print('wellcome')
   else:
       print('ramz eshtebah ast.')
else:
    print('uer not found')

#=======================================
#=======================================
#=======================================

#L_4_6


num1 = float(input('adad aval ra vared konid'))
num2 = float(input('adad dovom ra vared konid'))

amaliyat = input('amaliyat ra vared konid (+ - * /):')

if amaliyat == "+":
    print('result:', num1 + num2)

elif amaliyat == "-":
    print('result:', num1 - num2)

elif amaliyat == "*":
    print('result:', num1 * num2)

elif amaliyat == "/":
            print('result:', num1 / num2)

else:
    print('amaliyat na motabar ast')

#==============================================================================





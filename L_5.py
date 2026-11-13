#L_5
"""
in the name of god
"""
#l5_1 ========nemayesh adade fard========

for i in range (10,51):
    if i % 2 !=0:
        print(i)
'''
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
'''        
#============================================
#============================================
#============================================


#l5_2=======shomareshe makoos============
        
for i in range(20,0,-1):
    print(i)
        
'''
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
'''
#============================================
#============================================
#============================================

       
#l5_3======majmoo adad=======

sum = 0

for i in range (1,101):
    sum = sum + i
print('majmoo adad 1 ta 100 barabar ast ba:', sum)      
        
#majmoo adad 1 ta 100 barabar ast ba: 5050      
        
#============================================
#============================================
#============================================

#l5_4======jadvale zarb=========

number = int(input('inter a number:'))

for i in range (1,11):
    
    print (number,'*',i,'=',number*i)
'''
inter a number:-20
-20 * 1 = -20
-20 * 2 = -40
-20 * 3 = -60
-20 * 4 = -80
-20 * 5 = -100
-20 * 6 = -120
-20 * 7 = -140
-20 * 8 = -160
-20 * 9 = -180
-20 * 10 = -200   
'''      
        
#============================================
#============================================
#============================================

      
#l5_5_1 ===========A=========     
numbers = [12, 7, 25, 18, 3, 40, 11, 8]        
        
for i in numbers:
    if i % 2 == 0:
        print(i)      
'''
12
18
40
8
'''
#l5_5_2===========B========= 

numbers = [12, 7, 25, 18, 3, 40, 11, 8]  

count = 0

for i in numbers:
    if i % 2 == 0:
        count=(count + 1)
print('tedad adade zoj baraba ast ba:',count) #tedad adade zoj baraba ast ba: 4

#L5_5_3===========C========= 

numbers = [12, 7, 25, 18, 3, 40, 11, 8]

even_numbers=[]

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
print('liste adade zoj barabar ast ba:',even_numbers)
#liste adade zoj barabar ast ba: [12, 18, 40, 8]


#============================================
#============================================
#============================================

#L5_6

scores = [15, 18, 12, 20, 16, 14, 19]

total = 0

for i in scores:
    total = total + i
print (total)         #114


avrage = total/len(scores)

print(avrage)   #16.285714285714285

    
#============================================
#============================================
#============================================

#L5_7

numbers = [2, 4, 6, 8, 10]
new_list = []       
for i in numbers:
    new_list .append(i**2)
print (new_list)            #[4, 16, 36, 64, 100]
      
        
#============================================
#============================================
#============================================     
        
#L5_8     
        
tedade_adad = int(input('chand ta adad mikhahid vared konid?'))

numbers = []

for i in range(tedade_adad):
    number = int(input('yek adad vared konid:'))
    numbers.append(number)

print('adade vared shode:', numbers)     

'''
chand ta adad mikhahid vared konid?10
yek adad vared konid:10
yek adad vared konid:20
yek adad vared konid:30
yek adad vared konid:40
yek adad vared konid:50
yek adad vared konid:60
yek adad vared konid:70
yek adad vared konid:80
yek adad vared konid:90
yek adad vared konid:100
adade vared shode: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
'''
       
        
 #============================================
 #============================================
 #============================================     
         
 #L5_9

numbers = [4, 9, 15, 23, 42, 56, 71]

number = int(input('enter a number?'))

for num in numbers:
    if num == number:
        print('number found')     #enter a number?4 number found
        
        
#============================================
#============================================
#============================================     
          
#L5_10

for i in range(1,31):
    if i % 3 != 0:
        print(i)
'''       
1
2
4
5
7
8
10
11
13
14
16
17
19
20
22
23
25
26
28
29               
'''      
#============================================
#============================================
#============================================     
          
#L5_11        
        
jame_kol = 0

for i in range(10):
    number = int(input('yek adad vared konid:'))

    if number == 0:
        break

#============================================
#============================================
#============================================     
          
#L5_12         

students = [("Ali", 22),("Sara", 19),("Reza", 25),("Nima", 20),("Mina", 23)]

for name , age in students:
    print(f'name:{name},age:{age}')
'''
name:Ali,age:22
name:Sara,age:19
name:Reza,age:25
name:Nima,age:20
name:Mina,age:23

'''
#============================================
#============================================
#============================================     
          
#L5_13

students = [
("Ali", 18),
("Sara", 12),
("Reza", 9),
("Mina", 20),
("Nima", 14)
]

for name , score in students:
    if score>=15:
        print(name) 
'''        
Ali
Mina        
'''      
#============================================
#============================================
#============================================     
          
#L5_14

products = [
("Laptop", 50000, 2),
("Mouse", 800, 3),
("Keyboard", 1500, 2),
("Monitor", 12000, 1)
]

total = 0

for name, price, quantity in products:
    product_total = price * quantity
    print(name, ":", product_total)
    total += product_total

print("--------------------")
print("pardakhte nahayee:", total)

'''
Laptop : 100000
Mouse : 2400
Keyboard : 3000
Monitor : 12000
--------------------
pardakhte nahayee: 117400
'''

#============================================
#============================================
#============================================     
          
#L5_15

users = [
(1, "ali", "active"),
(2, "sara", "inactive"),
(3, "reza", "active"),
(4, "mina", "inactive"),
(5, "nima", "active")
]

new_user_name = input('enter user name:')
for user_id , username , status in users:
    if username ==  new_user_name:
        print('user id:', user_id)
        print('status:',status)
        break
else:
    print('user not found.')    

'''
enter user name:ali
user id: 1
status: active
'''













        
#1.Write code that compute the squares and cubes for numbers from 0 to 5 output as the following: each cell occupies 20 spaces and right-aligned.
#Solution 1
print('{0:>20}{1:>20}{2:>20}'.format("Number","Square","Cube"))
for i in range(0,6):
          print('{0:>20}{1:>20}{2:>20}'.format(i,i*i,i*i*i))# ">" represent right alignment and 20 is width. 

#2.Write code that use formula F = 9 / 5 * C + 32 to calculate and print the Fahrenheit temperature for Celsius value of -40, 0, 40 and 100.
#Solution 2
F1=(9/5)*(-40)+32
F2=(9/5)*(0)+32
F3=(9/5)*(40)+32
F4=(9/5)*(100)+32
print('Coverted celsius to Fahrenheit values','\n',F1,'\n',F2,'\n',F3,'\n',F4)# displaying the output using the formula for F1-F4.

#3.Write code that input three integers from the user. Then print the sum and average ofthe numbers. The sum should use comma (,) separator. The average uses commaseparate and has two decimal places. Each result is in a different line. If the input is 1000, 2000, 4000. The outputs are
#Sloution 3
a=1000
b=2000
c=4000
Total_Value = a+b+c
Average_Value= (a+b+c)/3
Total_Value
Average_Value
print('The sum is','{0:,d}'.format(Total_Value))
print('The Average is','{0:,.2f}'.format(Average_Value))
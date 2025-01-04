#build dictionary of robots and prices

robots = {'NAO':10000,'Pepper':28000,'Romeo':7500,'Atlas':6000,'Whis':4000}

#define function for warranty
def warranty(years):
    if years == '2':
        return 500
    elif years

#define function for training
def addon1(train_opt):
    if train_opt == 'y':
        return 250
    else:
        return 0


#define function for healthcare professional
def addon2(health_opt):
    if health_opt =='y':
        return .20
    else:
        return 0


#prompt user as to which robot to purchase

while True:
    print ('Enter robot you would like to purchase or blank to end')
    robotchoice = input()

    if robotchoice=='':
        break

    if robotchoice in robots:
        print (f'The price of the robot is $ (robots[robotchoice]:,.2f')
    else:
        print ('We do not carry that robot. Please re-enter')
        continue
    # ask if want warranty


    time = input ('Would you like to purchase a 2 year warranty, life or no warranty (2, life or no)?')

    #ask about trianing

    training = input ('would you like to purchase training (y or n)')

    #ask about healthcare
    health = input ('Are you a healthcare professional ? (y or n)')

    #access functions
    warranty_price = warranty(time)
    training_price = addon1(training)
    discout = addon2(health)

    total = float(robots[robotchoice])+warranty_price+training_price
    total = total *(1-discount)
    total = total * 1.07
    print (f'\n The total price of your robot is $ (total:,.2f)\n')
    time.sleep(5)

print ('Tank you. Good bye')
time.sleep(5)

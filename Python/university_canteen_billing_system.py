import datetime

loop_=True

while loop_:

    

    print()

    print("PRESS 1 TO START..... \n")




    products={1:(" Masala dosa         ",30),2:(" Idly                ",20),3:(" Vade                ",15),4:(" Poori               ",35),5:(" Pongal              ",30),6:(" Khara bath          ",30),

    7:(" Kesari bath         ",25),8:(" Rave idly           ",25),9:(" Set dosa            ",40),10:("Rava dosa           ",40),11:("Khali dosa          ",35),12:("Neer dosa           ",40),

    13:("Upma                ",25),14:("Akki rotti          ",30),15:("Bonda soup          ",30),16:("Tea                 ",10),17:("Coffee              ",10),18:("Butter chicken      ",150),

    19:("Kerarla chickenroast",90),20:("Mutton biryani      ",200),21:("Chicken 65          ",120),22:("Gobi manchuri       ",60),23:("Paneer manchuri     ",80),

    24:("Babycorn manchuri   ",70),25:("Fried rice          ",50)}




    now=datetime.datetime.now()




    control_choice=int(input())     #first input to login as  customer

    while control_choice!=1:

        print(" INVALID INPUT PRESS 1 TO START..... \n")

        control_choice=int(input())













    def des_front():

        print("==========================================================")

        print("==================SOUTH  INDIAN CANTEEN===================")

        print("==========================================================")

        print("              PRODUCT MENU     ")

        print("============================================================")

        print("PID       NAME                                        PRICE ")

        print("============================================================")




    def place_order():

        print("=============================")

        print("     PLACE YOUR ORDER        ")

        print("=============================\n")







    def invoice():

        print("==========================================================")

        print("==================ABC UNIVERSTY CANTEEN===================")

        print("==========================================================")

        print("                                   INVOICE           ",now)

        print("===================================================================================================================================================================")

        print(" PID    NAME                        QUANTITY           PRICE            AMOUNT          AMOUNT(+GST & DISCOUNT)")

        print("===================================================================================================================================================================")



















    bill_it=True

    invoice_it=False




    def menu_display(dict):

        des_front()

    

        for k,v in dict.items():

            print(k,"     ",v[0],"                         ",v[1])

        print()

        place_order()
















    menu_display(products)

    values=products.values()

    values=list(values)

    products1={}

    while bill_it:

        if control_choice==1:

            product_choice=int(input("Enter The ID of The Product : ")) #second choice to enter product number

            print()

            quantity=int(input("Quantity :"))   #enter the quantity

            print()

            products1[product_choice]=[values[product_choice-1],quantity]

            an_order=input("Do you want Order another Product ? (y/n) ")

            while an_order.upper()!="Y" and an_order!="n":

                print("Enter only (y/n)\n")

                an_order=input("Do you want Order another Product ? (y/n) ")

        

            print("\n")

            if an_order.upper()=="N":

                print("Thank you for placing the order!!!\n\n")

                bill_it=False

                invoice_it=True

            elif an_order.upper()=="Y":

                bill_it=True













    i=1

    while invoice_it:

        invoice()

        total_cost=0

        with_gst=0

        for v in products1.values():

        

            print(" ",i,"  ",v[0][0],"        ",v[1],"               ",v[0][1],"             ",v[0][1]*v[1],"              ",v[0][1]*v[1]+v[0][1]*v[1]*0.08," ")

            i+=1

            total_cost+=v[0][1]*v[1]

            with_gst+=v[0][1]*v[1]+v[0][1]*v[1]*0.08

        print("===================================================================================================================================================================")

        print("                                                                                         Total  :-TOTAL(excl gst)=",total_cost,"   ","TOTAL(incl gst)=",with_gst)

        print("===================================================================================================================================================================")

        print()

        print("THANK YOU!!!!!  VISIT AGAIN!!!!!")

        break

    print()

    print()




    userwish=input("DO YOU WANT TO BILL AGAIN ? (y/n)")

    if userwish.upper()=="Y":

        loop=True

    else:

        loop=False

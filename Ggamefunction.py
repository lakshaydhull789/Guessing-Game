#GuessingGame Functions
import csv
import random as r
import time
def forget():
    print("\n\tWelcome to our helpdesk")
    print("\n\tHow may we help you in accessing your login")
    RP=input("\n\tDo you remember\n\t1.Your Email ID and Registration ID 2.Username and Registration ID: ")
    f=open("logins.csv","r")
    red=csv.reader(f)
    ldata=[]
    for i in red:
        ldata.append(i)
    f.close()
    if RP=='1':
        while True:
            temp=0
            status="no"
            email=input("\n\tPlease enter your registered email ID: ")
            for i in ldata:
                #print(i)
                if i[2]==email:
                    temp=1
                    rID=input("\n\tPlease enter Registration ID provided to you during registration: ")
                    if rID==i[-1]:
                        print("\n\tVerifying your details....")
                        time.sleep(1)
                        print("\n\tVerification Complete")
                        print("\n\t",end="")
                        print("-"*30)
                        print("Your password is |",i[1],"|")
                        print("\t",end="")
                        print("-"*30)
                        status="yes"
                    else:
                        print("\n\tVerifying your details...")
                        print("\n\tIncorrect Registration ID")
            if temp==0:
                print("\n\tEmail Not Found")
            if status=="yes":
                break
def game(un):
    f=open("logins.csv","r")
    rd1=csv.reader(f)
    fdata=[]
    for i in rd1:
        fdata.append(i)
    f.close()
    for i in fdata:
        if i[0]==un:
            print("\n\tWelcome to the game")
            time.sleep(0.25)
            print("\n\t",end="")
            print("-"*35)
            ai=int(i[3])
            print("\tAmount Invested Till Today:|","$",ai,"|")
            print("\t",end="")
            print("-"*35)
            time.sleep(0.25)
            print("\t",end="")
            aw=int(i[4])
            print("Amount Won till Today: |","$",aw,"|")
            print("\t",end="")
            print("-"*35)
            print("\n\tWelcome to the game")
            time.sleep(0.25)
            pq=input("\n\tPlease pay $10 and press C to play else press any other key: ")
            if pq in 'cC':
                print("\n\tAs per the game you have to select a number,\n\tout of the number shown on screen,\n\tone of them is a lucky number if you entered number matches with that number you'll win $100")
                time.sleep(2)
                iits=0
                wits=0
                while True:
                    ai=ai+10
                    iits=iits+10
                    rnl=[]
                    for i in range(1,100,10):
                        rnl.append(r.randint(i,i+9))
                    print("\n\t")
                    print("-"*40)
                    for i in rnl:
                        print(i,"|",end="")
                    print("\n","-"*40)
                    fr=r.choice(rnl)
                    time.sleep(1)
                    
                    while True:
                        en=int(input("\n\tPlease enter your number: "))
                        if en in rnl:
                            break
                        else:
                            print("\n\tThe number you entered was not from the numbers shown in the screen\n\tPlease try again")
                    if en==fr:
                        print("\n\tCongratulations you won!!!!!")
                        wits=wits+100
                        aw=aw+100
                    else:
                        print("\n\tYour Number: ",en)
                        print("\n\tLucky number was: ",fr)
                        print("\n\tYou looser!!!!!!")
                        time.sleep(0.5)
                        print("\n\tYou lost your money")
                        time.sleep(0.5)
                        print("\n\tI bet you can't win EVER")
                    print("\n\tTotal amount invested till today:",ai)
                    print("\tAmount won till Today:", aw)
                    print("\n\tTotal amount invested in this session:", iits)
                    print("\tAmount Won in this session:",wits)
                    option=input("\n\tTo continue pay $10 and press 'C' else press any other key and backout")
                    if option not in 'cC':
                        break

            else:
                print("\n\tThank you for using our services :)")
    newdata=[]
    for i in fdata:
        if i[0]==un:
            i[3]=ai
            i[4]=aw
            newdata.append(i)
        else:
            newdata.append(i)
    print(newdata)
    f=open("logins.csv","w",newline="")
    rr=csv.writer(f)
    rr.writerows(newdata)
    f.close
                
def login():
    while True:
        n=input("\n\t\tLogin via 1.Username 2.Email ID 3.Forget Password:")
        f=open("logins.csv","r")
        rd=csv.reader(f)
        fdata=[]
        for i in rd:
            fdata.append(i)
        if n=='1':
            un=input("\n\tPlease enter your username: ")
            status=0
            for i in fdata:
                if i[0]==un:
                    status=1
                    pw=input("\n\tPlease enter your Password: ")
                    if i[1]==pw:
                        print("\n\tLogin sucessfull:)")
                        game(un)
                        break
                    else:
                        print("\n\tIncorrect Password")
                        fpw=input("\n\tPress F if you forget password: ")
                        if fpw.lower()=='f':
                            email=input("\n\tPlease enter your email ID which you provided during signup: ")
                            if i[2]==email:
                                print("\n\tYour password is:",i[1])
                                break
                            else:
                                print("\n\tIncorrect Email ID")
                        else:
                            print("Try Again!!!")
            if status==0:
                print("\n\tIncorrect username!!!\n\tPlease try again")
        elif n=='2':
            email=input("\n\tPlease enter your Email ID: ")
            status=0
            for i in fdata:
                if i[2]==email:
                    status=1
                    pw=input("\n\tPlease enter your Password: ")
                    if i[1]==pw:
                        print("\n\tLogin sucessfull:)")
                        break
                    else:
                        print("\n\tIncorrect Password")
                        fpw=input("\n\tPress F if you forget password: ")
                        if fpw.lower()=='f':
                            un=input("\n\tPlease enter your Username which you provided during signup: ")
                            if i[0]==un:
                                print("\n\tYour password is:",i[1])
                                break
                            else:
                                print("\n\tIncorrect username")
                        else:
                            print("Try Again!!!")
            if status==0:
                print("\n\tIncorrect email ID!!!\n\tPlease try again")
        elif n=='3':
            forget()
            
        else:
            print("\n\tInvalid Option Selected!!!\n\tPlease choose valid option")

def signup():
    f=open("logins.csv","r")
    rd=csv.reader(f)
    finaldata=[]
    for i in rd:
        finaldata.append(i)
    log=[]
    while True:
        print("\n\tUsername must contain one upper case letter.\n\tone lower case letter\n\tone digit.\n\tone special character")
        un=input("\n\tPlease enter your User Name: ")
        c=0
        for i in rd:
            
            if i[0]==un:
                c=1
        if c==1:
            print("\n\tUser Name already exists!\n\tPlease try another username")
        if c==0:
            uc=0
            lc=0
            dg=0
            sc=0
            for j in un:
                if j.isupper():
                    uc=1
                if j.islower():
                    lc=1
                if j.isdigit():
                    dg=1
                if not j.isalnum() and j!=' ':
                    sc=1
            if uc==0:
                print("\n\tNo upper case letter found")
            elif lc==0:
                print("\n\tNo lower case letter found in username")
            elif dg==0:
                print("\n\tNo digit found in Username\n\tMust contain atleast 1 digit")
            elif sc==0:
                print("\n\tUsername must contain a special charachter")
            else:
                break
    while True:
        pw=input("\n\tPlease create your Password: ")
        if len(pw)<5:
            print("\n\tPassword is too short please use a password that should have atleast 5 characters")  
        else:
            tt=0
            while True:
                email=input("\n\tPlease enter your email ID: ")
                if '@' in email:
                    if '.' in email:
                        print("\n\tProcessing",end=" ")
                        for i in range(1,6):
                            print(".",end="")
                            time.sleep(0.4)
                        print("\n\tCreating Your Account",end=" ")
                        for i in range(1,6):
                            print(".",end="")
                            time.sleep(0.4)
                        print("\n\t\tUser Created sucessfully")
                        print("\n\tLogin by Pressing A")
                        regcode=[]
                        for i in finaldata:
                            regcode.append(i[5])
                        while True:
                            rd1=r.randint(1,100000)
                            if rd1 in regcode:
                                continue
                            break
                        
                        log.append([un,pw,email,0,0,rd1])
                        print("\n\t\tYour Unique ID is: ",end="\t")
                        print("|  ",rd1,"  |")
                        print("\n\t\tPlease note it down for Future references")
                        tt=1
                        break
                    
                    else:
                        print("\n\tInvalid email ID please enter valid email ID!!!")
                        print("\n\tEmail ID must contain '.'")
                else:
                    print("\n\tInvalid email ID please enter valid email ID!!!")
                    print("\n\tEmail ID must contain '@'")
            if tt==1:
                break
                
    f.close()
    f=open("logins.csv","a",newline="")
    w=csv.writer(f)
    w.writerows(log)
    f.close()


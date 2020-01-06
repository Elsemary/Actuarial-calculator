"""
@author: ABELRHMAN H ELSEMARY ; Collge of science department of mathematics
"""
import reserve_class as reserve
case_dis_or_cont=str(input('Enter the benifit type (dis , cont):  '))




if case_dis_or_cont =='dis':
    inittial_exp=float(input('inittial_exp:  '))# e : e+c*G for first year
    Renwal_exp=float(input('Renwal_exp:  '))# e: e+c*G
    E=float(input('settlement:  '))# settlement
    death_type=str(input('death_type:  '))#level or diffrant amoung years.
    intrest=float(input('i:  '))
    if death_type == 'diff':
        Death_Benifit=[]
        payment=int(input('num of years:  '))
        premuim_Apv=[1]
        surv_benifit=[]
        morta_=[]
        for i in range(1,payment+1):
            payment_1=float(input('payment '+ str(i)+ ':'))
            if i>1:
                mor=float(input('mortalty '+ str(i)+ ':'))
                mortalty1=np.cumprod(morta_[0:i])[i-2]*mor
                Death_Benifit.append(reserve.APV_FB (payment_1,intrest,mortalty1,i))
                morta_.append(1-mor)
            if i ==1 :
                mor=float(input('mortalty '+ str(i)+ ':'))
                Death_Benifit.append(reserve.APV_FB (payment_1,intrest,mor,i))
                morta_.append(1-mor)
        for j in range (1,payment):
            survival=np.cumprod(morta_[0:j+1])[j-1]
            premuim_Apv.append(reserve.Apv_FP (1,survival,intrest,j))
        survival_1=np.cumprod(morta_[0:j+1])[j]
        survival_payment=float(input('survival payment:  '))
        years=payment
        surv_benifit.append(reserve.Apv_FP(survival_payment,survival_1,intrest,years))


    if death_type == 'level' :
        years=int(input('num of years:  '))
        payment=float(input('level payment:  '))
        Death_Benifit=[]
        premuim_Apv=[1]
        surv_benifit=[]
        morta_=[]
        for i in range (1,years+1):
            if i>1:
                mor=float(input('mortalty '+ str(i)+ ':'))
                mortalty=np.cumprod(morta_[0:i])[i-2]*mor
                Death_Benifit.append(reserve.APV_E (payment,mortalty,intrest,i))
                morta_.append(1-mor)
            if i ==1:
                mor=float(input('mortalty '+ str(i)+ ':'))
                Death_Benifit.append(reserve.APV_E (payment,mor,intrest,i))
                morta_.append(1-mor)
        for j in range (1,years):
            survival=np.cumprod(morta_[0:j+1])[j-1]
            premuim_Apv.append(reserve.Apv_FP (1,survival,intrest,j))
        survival_1=np.cumprod(morta_[0:j+1])[j]
        survival_payment=float(input('survival payment:  '))
        surv_benifit.append(reserve.Apv_FP(survival_payment,survival_1,intrest,years))


    net_premium=(sum(Death_Benifit)+sum(surv_benifit))/sum(premuim_Apv)

    d=int(input('period of suttelment exp.:  '))
    percentge=float(input('%:  '))
    percentge_1=float(input('%_:  '))
    Gross_premium=reserve.Gross(d,percentge,percentge_1)

    h=int(input('Reserve at time ?:  '))
    Reserve_=[]
    if death_type == 'level':
        for i in range (h,years):
            morta=1-morta_[i]
            if i==h:
                o=reserve.APV_FB(payment,intrest,morta,i-h+1)
                Reserve_.append(o)
            if i>h:
                morta=1-morta_[i]
                morta__=np.cumprod(morta_[h:i])[0]*morta
                o=reserve.APV_FB(payment,intrest,morta__,i-h+1)
                Reserve_.append(o)
    if death_type == 'diff':
            for i in range (h,years):
                morta=1-morta_[i]
                payment=float(input('Enter the series of payment after year  '+ str(i+1)+ ''))
                if i==h:
                    o=reserve.APV_FB(payment,intrest,morta,i-h+1)
                    Reserve_.append(o)
                if i>h:
                    morta=1-morta_[i]
                    morta__=np.cumprod(morta_[h:i])[0]*morta
                    o=reserve.APV_FB(payment,intrest,morta__,i-h+1)
                    Reserve_.append(o)
    Reserve_.append(reserve.APV_FB(survival_payment,intrest,np.cumprod(morta_[h:i+1])[h-i],i-h+1))

    for i in range (h,d):
        morta=1-morta_[i]
        if i==h:
            o=reserve.APV_E(E,morta,intrest,i-h+1)
            Reserve_.append(o)
        if i>h:
            morta=1-morta_[i]
            morta__=np.cumprod(morta_[h:i])[0]*morta
            o=reserve.APV_E(E,morta,intrest,i-h+1)
            Reserve_.append(o)
    for i in range (h,years):
        if i==h:
            o=reserve.APV_e_cG (Renwal_exp,(1-percentge),Gross_premium,1,0,i-h+1)
            Reserve_.append(o)
        if i>h:
            o=reserve.APV_e_cG (Renwal_exp,(1-percentge),Gross_premium,np.cumprod(morta_[h:i])[h-i],intrest,i-h)
            Reserve_.append(o)
    for i in range (h,years):
         if i==h:
             o=-1*reserve.Apv_FP(Gross_premium,1,0,0)
             Reserve_.append(o)
         if i>h:
             o=-1*reserve.Apv_FP(Gross_premium,np.cumprod(morta_[h:i])[h-i],intrest,i-h)
             Reserve_.append(o)

    Reserve=sum(Reserve_)
    print (Reserve,Gross_premium,net_premium,Death_Benifit)

if case_dis_or_cont =='cont':
    E=float(input('settlement 0 if you have pi :  '))# settlement
    Renwal_exp=float(input('Renwal_exp 0 if you have pi:  '))# e: e+c*G
    b=float(input('survival benifit:  '))#if there is survival
    pi_=float(input('pi(Enter 0 if you have G(1-c)-e ):  '))
    G=float(input('Gross pre. 0 if you have pi:  '))# Gross pre.
    C=float(input('% of premium 0 if you have pi:  '))#function of prem.
    mortalty=float(input('MU or mortality:  '))
    dalta=float(input('dalta:  '))
    
    h=0.25#length of accuracy
    t = np.arange(0, 20, h)

    m=[]
    dx=0
    w=0
    for i in range(0, len(t)):
        # Euler's method
        y=w
        x=1+t[i]
        dx=reserve.dx_dt(x,G,C,Renwal_exp,pi_,dalta,mortalty,b,E)
        w=(dx*h)+ w
        m.append(np.array([x-1,y,dx]))
    reserve=(m[len(m)-1][2])
    print(reserve)

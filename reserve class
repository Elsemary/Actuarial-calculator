"""
@author: ABELRHMAN H ELSEMARY ; Collge of science department of mathematics
"""
import numpy as np

class reserve:
    def APV_FB (Death_benifit_or_ser,intrest,mortality_or_ser,i):
        k=(Death_benifit_or_ser*(mortality_or_ser/(1+intrest)**i))
        return (k)
    
    def APV_E (E,mortality,intrest,i):
        x=(E*(mortality/(1+intrest)**i))
        return (x)
    
    def APV_e_cG (e,c,G,survivial,intrest,i):
        j=(e+(c*G))*((survivial/(1+intrest)**i))
        return (j)
    
    def Apv_FP (p,survivial,intrest,i):
        m=((p)*((survivial/(1+intrest)**i)))
        return (m)

    def Gross (d,percentge,percentge_1):
    
 #    You have to write gross in the folllowing form:
         
 #        b Ax:n + s xEn + E Ax:n-h + initial exp. + e ax:n
 #  G=   __________________________________________
 #                    % ax:n - %_1
         
 #     where b , Ax:n , s , E , h , ax:n , % ans %_1 is benifit term insurance discrete , survival ,
 #     suttelment exp. , the period of suttelment , annuite due , % persentage after some mathmatic opration
 #      and %_ is other percentge . 
        Ax=[]
        for i in range (0,d):
            if i ==0:
                morta=1-morta_[i]
                o=reserve.APV_FB(1,intrest,morta,i+1)
                Ax.append(o)
            if i >0:
                morta=1-morta_[i]
                morta__=np.cumprod(morta_[0:i])[len(np.cumprod(morta_[0:i]))-1]*morta
                o=reserve.APV_FB(1,intrest,morta__,i+1)
                Ax.append(o)
        x=((sum(Death_Benifit)+sum(surv_benifit))+E*sum(Ax)
                  +inittial_exp+Renwal_exp*sum(premuim_Apv))/(percentge*sum(premuim_Apv)-percentge_1)
         
        return(x)


    # dN/dt #contious case
    def dx_dt(x,G,C,e,pi_,dalta,mortalty,b,E):
        return (G*(1-C)-e+pi_+(dalta+mortalty)*x-(b+E)*mortalty)

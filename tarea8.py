# EEEE LL    II     AA     MMMM MMMM 
# E    LL    II    A  A    MM MM  MM 
# EEEE LL    II   AAAAAA   MM     MM 
# E    LL    II  A      A  MM     MM 
# EEEE LLLLL II A        A MM     MM 
ctrE = input("¿Qué caracter quieres para la E? ")
ctrL = input("¿Qué caracter quieres para la L? ")
ctrI = input("¿Qué caracter quieres para la I? ")
ctrA = input("¿Qué caracter quieres para la A? ")
ctrM = input("¿Qué caracter quieres para la M? ")



def letraE( ctr ):
    return print(f"\n{ctr}{ctr}{ctr} \n{ctr} \n{ctr}{ctr}{ctr} \n{ctr} \n{ctr}{ctr}{ctr}\n")

def letraL( ctr ):
    return print(f"{ctr}{ctr}\n{ctr}{ctr}\n{ctr}{ctr}\n{ctr}{ctr}\n{ctr}{ctr}{ctr}{ctr}{ctr}\n")

def letraI( ctr ):
    return print(f"{ctr}{ctr}\n{ctr}{ctr}\n{ctr}{ctr}\n{ctr}{ctr}\n{ctr}{ctr}\n")

def letraA( ctr ):
    return print(f"    {ctr}{ctr}\n   {ctr}  {ctr}\n  {ctr}{ctr}{ctr}{ctr}{ctr}{ctr}\n {ctr}      {ctr}\n{ctr}        {ctr}\n")

def letraM( ctr ):
    return print(f"{ctr}{ctr}{ctr}{ctr} {ctr}{ctr}{ctr}{ctr}\n{ctr}{ctr} {ctr}{ctr}  {ctr}{ctr}\n{ctr}{ctr}     {ctr}{ctr}\n{ctr}{ctr}     {ctr}{ctr}\n{ctr}{ctr}     {ctr}{ctr}\n")


letraE(ctrE)
letraL(ctrL)
letraI(ctrI)
letraA(ctrA)
letraM(ctrM)

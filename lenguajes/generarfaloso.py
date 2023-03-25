import random
    
class generafalso():
    def generarfalsos():
        val = random.randint(1,4)
        dato = random.randint(0,9)
        dato = str(dato)
        randlowercase = chr(random.randint(ord('a'), ord('z')))
        
        if val == 1:
            particion = "{{"+ randlowercase+"}"+ ","+ "{"+randlowercase +","+ dato+"}}"
            return particion
            
        elif val ==2:
            particion = "{{"+ randlowercase +"}}"
            return particion
            
        elif val == 3:
            particion = "{{"+ randlowercase +"}"+","+"{"+randlowercase+"}"+"}" 
            
            return particion
        elif val == 4:
            particion = "{{"+ randlowercase + ","+ dato +","+ dato +"}"+"," +"{"+randlowercase+"}"+"}"
            
            return particion
        

generafalso()
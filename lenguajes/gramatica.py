from nltk import CFG
from nltk.parse.generate import generate
from nltk.corpus import words
import random

conjuntos = []
conjunto1 =[]
conjunto2 = []
conjunto3 = []
class conjuntosal():
    
    def conjunto():
        
        conjuntoval = random.randint(1,4)
        print(conjuntoval)
        if conjuntoval == 1:
            vran1 = 0
            valor= ""
            conjuntos.clear()
            vran1=random.randint(1,36)
            correctos = CFG.fromstring("""
                        A -> KE VC  KS 
                        KE -> '{' 
                        VC -> V C
                        KS -> '}'
                        V -> ' 1' | ' 2' | ' 3' | ' 4' | ' 5' | ' 6' | ' 7' | ' 8' | ' 9' | ' 0' | ' a' | ' b' | ' c' | ' d' | ' e' | ' f' | ' g' | ' h' | ' i' | ' j' | ' k' | ' l' | ' m' | ' n' | ' o' | ' p' | ' q' | ' r'| ' s' | ' t' | ' u' | ' v' | ' w' | ' x' | ' y' | ' z' 
                        C -> ''
                    """)
                
            for s in generate(correctos,n=999):
                        valor = ''.join(s)
                        
                        conjuntos.append(valor)
            resultado1 = conjuntos[vran1]
            resultado1 = resultado1.replace(" ","")
            
            return resultado1
            
            
        elif conjuntoval == 2:
            conjunto1.clear()
            valor1 = ""
            vran2=random.randint(1,999)
            correctos = CFG.fromstring("""
                        A -> KE VC V KS 
                        KE -> '{' 
                        VC -> V C
                        KS -> '}'
                        V -> ' 1' | ' 2' | ' 3' | ' 4' | ' 5' | ' 6' | ' 7' | ' 8' | ' 9' | ' 0' | ' a' | ' b' | ' c' | ' d' | ' e' | ' f' | ' g' | ' h' | ' i' | ' j' | ' k' | ' l' | ' m' | ' n' | ' o' | ' p' | ' q' | ' r'| ' s' | ' t' | ' u' | ' v' | ' w' | ' x' | ' y' | ' z' 
                        C -> ','
                    """)
            for s in generate(correctos,n=999):
                        valor1 = ''.join(s)
                        conjunto1.append(valor1)

            resultado2 = conjunto1[vran2]
            resultado2 = resultado2.replace(" ","")
            return resultado2
            
            
        elif conjuntoval == 3:
            conjunto2.clear()
            valor2 = ""
            vran3=random.randint(1,999)
            correctos = CFG.fromstring("""
                        A -> KE VC VC V KS 
                        KE -> '{' 
                        VC -> V C
                        KS -> '}'
                        V -> ' 1' | ' 2' | ' 3' | ' 4' | ' 5' | ' 6' | ' 7' | ' 8' | ' 9' | ' 0' | ' a' | ' b' | ' c' | ' d' | ' e' | ' f' | ' g' | ' h' | ' i' | ' j' | ' k' | ' l' | ' m' | ' n' | ' o' | ' p' | ' q' | ' r'| ' s' | ' t' | ' u' | ' v' | ' w' | ' x' | ' y' | ' z' 
                        C -> ','
                    """)
            for s in generate(correctos,n=9999):
                        valor2 = ''.join(s)
                        conjunto3.append(valor2)

            resultado3 = conjunto3[vran3]
            resultado3 = resultado3.replace(" ","")
            return resultado3
            
        elif conjuntoval == 4:
            conjunto3.clear()
            valor3 = ""
            correctos4 = ""
            
            vran4=random.randint(1,9999)
            correctos4 = CFG.fromstring("""
                        A -> KE VC VC VC V KS 
                        KE -> '{' 
                        VC -> V C
                        KS -> '}'
                        V -> ' 1' | ' 2' | ' 3' | ' 4' | ' 5' | ' 6' | ' 7' | ' 8' | ' 9' | ' 0' | ' a' | ' b' | ' c' | ' d' | ' e' | ' f' | ' g' | ' h' | ' i' | ' j' | ' k' | ' l' | ' m' | ' n' | ' o' | ' p' | ' q' | ' r'| ' s' | ' t' | ' u' | ' v' | ' w' | ' x' | ' y' | ' z' 
                        C -> ','
                    """)
            
            for s in generate(correctos4,n=99999):
                        valor3 = ''.join(s)
                        conjunto3.append(valor3)

            resultado4 = conjunto3[vran4]
            resultado4 = resultado4.replace(" ","")
            print(resultado4)
            return resultado4
            
            
            
    

                        

            
  











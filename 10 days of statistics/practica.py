def pepa(total,monedas,ind):
    aux=monedas.copy()
    sum=0
    if total==0:
        print("u")
        print(monedas)
        return ind+1
    elif len(monedas)>1:   
        for item in monedas:
            if total==item:
                aux.remove(item)
                return ind+pepa(total,aux,ind)+pepa(total-item,monedas,ind)
            elif total>item:
                aux.remove(item)
                               
                return ind+pepa(total-item,monedas,ind)+pepa(total,aux,ind)
            else:
                aux.remove(item)              
                return ind+pepa(total,aux,ind)
        print('as')   
        return ind
    else:        
         if monedas[0]==total or total%monedas[0]==0: 
             print(total)
             print(" a")
             return 1+ind
         else: 
              
             return ind
        

                
    
            
   
  
                
monedas=[2,5,3,6]
monedas.sort()
monedas.reverse()
n=300

respuesta=pepa(n,monedas,0)

#revision(n,monedas,0)
    
print(respuesta)

#temp.append([])


    
    

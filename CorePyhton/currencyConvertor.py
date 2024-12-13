
def converter(amt,unit="USD"):
    if(unit=="Rs"):
        total=int(amt)/83
        return total
    
    elif(unit=="eur"):
        total=float(amt)*1.05
        return total
    
    elif(unit=="dhr"):
        total=float(amt)*2.65
        return total
    else:
        return amt+unit
        
        
print(converter("150","dhr"))
def hisobla(a, b, amal):
    if amal == "+":
        return a + b
    elif amal == "-":
        return a - b
    elif amal == "*":
        return a * b
    elif amal == "/":
        if b == 0:
            return "Xato: nolga bo'lish mumkin emas"
        else:
            return a / b
    else:
        return "Noto'g'ri amal"

if __name__=="__main__":
    print(hisobla(10, 5, "+"))  
    print(hisobla(10, 5, "-"))  
    print(hisobla(10, 5, "*")) 
    print(hisobla(10, 5, "/"))

        
        
    
    
    

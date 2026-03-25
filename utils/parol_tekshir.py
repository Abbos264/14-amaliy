def kuchlimi(parol):
    if len(parol) >= 8:
        return "Kuchli"
    else:
        return "Kuchsiz"

if __name__=="__main__":
    print(kuchlimi("abc123"))       
    print(kuchlimi("abc12345"))
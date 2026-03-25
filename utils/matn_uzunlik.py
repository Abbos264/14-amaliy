def uzunlik(matn):
    if matn == "":
        return "Bo'sh matn"
    else:
        return len(matn)

if __name__=="main":
    print(uzunlik("Salom")) 
    print(uzunlik(""))
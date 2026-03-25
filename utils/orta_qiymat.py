def orta(sonlar):
    if len(sonlar) == 0:
        return 0
    else:
        return sum(sonlar) / len(sonlar)

if __name__=="__main__":
    print(orta([1, 2, 3, 4, 5]))  
    print(orta([]))
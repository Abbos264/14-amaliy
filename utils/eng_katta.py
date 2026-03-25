def top(sonlar):
    if len(sonlar) == 0:
        return "Ro'yxat bo'sh"
    else:
        return max(sonlar)

if __name__=="__main__":
    print(top([3, 1, 7, 2, 9]))  
    print(top([]))


if __name__ == "__main__":
hall = [[0]*7 for g in range(5)]

def show():
    for y in hall:
        print(y)
 
def book_seats(n):
    for i, y in enumerate(hall):
        for j in range(len(y)-n+1):
            if sum(y[j:j+n]) == 0:
                for k in range(n):
                    y[j+k] = 1
                print(f"Ряд {i+1}, места {j+1}-{j+n}")
                return
    print("Нет мест")

# Пример
show()
book_seats(4)
show()
book_seats(7)
show()
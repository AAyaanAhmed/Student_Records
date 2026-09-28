n = []
m = []

x = int(input("No: "))

for i in range(x):
    n.append(input("Name: "))
    m.append(int(input("Mark: ")))

while True:
    print("1.Show 2.Find 3.Sort 4.Max 5.Min 6.Exit")
    c = input("Choice: ")

    if c == "1":
        for i in range(len(n)):
            print(n[i], m[i])

    elif c == "2":
        s = input("Find: ")
        if s in n:
            i = n.index(s)
            print(n[i], m[i])
        else:
            print("No Data")

    elif c == "3":
        for i in range(len(m)):
            for j in range(i + 1, len(m)):
                if m[i] < m[j]:
                    m[i], m[j] = m[j], m[i]
                    n[i], n[j] = n[j], n[i]

        for i in range(len(n)):
            print(n[i], m[i])

    elif c == "4":
        a = max(m)
        print(n[m.index(a)], a)

    elif c == "5":
        a = min(m)
        print(n[m.index(a)], a)

    elif c == "6":
        break

    else:
        print("Wrong")

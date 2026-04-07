import json
import matplotlib.pyplot as plt
FILE = "data_store.json"
# load data
def read():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []
# save data
def write(d):
    with open(FILE, "w") as f:
        json.dump(d, f)
# add data
def add_data():
    print("\nAdd Expense")
    d = input("Date: ")
    c = input("Type (food/travel/etc): ")
    amt = input("Money spent: ")
    try:
        amt = float(amt)
    except:
        print("Invalid number")
        return
    text = input("Any note: ")
    obj = {"d": d, "c": c, "a": amt, "t": text}
    data = read()
    data.append(obj)
    write(data)
    print("Added successfully")
# view all
def show_all():
    data = read()
    if len(data) == 0:
        print("No entries")
        return
    print("\nAll expenses:")
    for i in range(len(data)):
        print(i, "->", data[i])
# delete entry
def remove():
    data = read()
    if len(data) == 0:
        print("Nothing to delete")
        return
    show_all()
    x = input("Enter index to remove: ")
    try:
        x = int(x)
    except:
        print("Wrong input")
        return
    if x >= 0 and x < len(data):
        data.pop(x)
        write(data)
        print("Removed")
    else:
        print("Index error")
# monthly total
def month_calc():
    m = input("Month (MM): ")
    data = read()
    total = 0
    for i in data:
        if len(i["d"]) >= 7:
            if i["d"][5:7] == m:
                total += i["a"]
    print("Month total =", total)
# category summary
def cat_calc():
    data = read()
    res = {}
    for i in data:
        if i["c"] in res:
            res[i["c"]] += i["a"]
        else:
            res[i["c"]] = i["a"]
    if res == {}:
        print("Empty data")
        return
    print("\nCategory summary:")
    for k in res:
        print(k, ":", res[k])
# graph
def draw():
    data = read()
    res = {}
    for i in data:
        if i["c"] in res:
            res[i["c"]] += i["a"]
        else:
            res[i["c"]] = i["a"]
    if res == {}:
        print("No data for chart")
        return
    names = []
    vals = []
    for k in res:
        names.append(k)
        vals.append(res[k])

    plt.pie(vals, labels=names, autopct="%1.1f%%")
    plt.title("Spending Chart")
    plt.show()
# main loop (different style)
def start_app():
    while True:
        print("\n==== Expense Manager ====")
        print("a -> add")
        print("b -> show")
        print("c -> delete")
        print("d -> monthly")
        print("e -> category")
        print("f -> chart")
        print("x -> exit")
        ch = input("Enter option: ")
        if ch == "a":
            add_data()
        elif ch == "b":
            show_all()
        elif ch == "c":
            remove()
        elif ch == "d":
            month_calc()
        elif ch == "e":
            cat_calc()
        elif ch == "f":
            draw()
        elif ch == "x":
            print("Closing app")
            break
        else:
            print("Invalid choice")
# run
start_app()

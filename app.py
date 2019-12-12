import tkinter
import csv
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image



plt.rcdefaults()
window = tkinter.Tk()
width = window.winfo_screenwidth()-10
height = window.winfo_screenheight()-90
window.minsize(width=width, height=height)
window.geometry("+0+0")




def ByRegion():
        filename = 'ByMonth.csv'
        with open(filename, encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            performance = []
            objects = []
            for row in reader:
                if row[0] == '' or row[0] == "Общо":
                    continue
                objects.append(row[0])
                high = int(row[7], 10)
                performance.append(high)
            y_pos = np.arange(len(objects))

            fig = plt.figure(dpi=128, figsize=(10, 6))
            plt.bar(y_pos, performance, align='center', alpha=0.5)
            # Format Plot
            plt.title("Брой ПТП-та по области", fontsize=24)
            plt.xticks(y_pos, objects)
            plt.xlabel('', fontsize=16)
            plt.ylabel("Брой ПТП-а", fontsize=16)
            plt.tick_params(axis='both', which='major', labelrotation=90, labelsize=8)
            plt.gcf().subplots_adjust(bottom=0.3)

            plt.show()



def ByMonth():
        filename = 'ByMonth.csv'
        with open(filename, encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            performance = []
            objects = []
            row = next (reader)
            for obj in row:
                if obj != '':
                    objects.append(obj)
            for row in reader:
                if row[0] != 'Общо':
                    continue
                for i in range(1 , 7):
                    high = int(row[i], 10)
                    performance.append(high)



            y_pos = np.arange(len(objects))

            fig = plt.figure(dpi=128, figsize=(10, 6))
            plt.bar(y_pos, performance, align='center', alpha=0.5)
            # Format Plot
            plt.title("Брой ПТП-та по месеци", fontsize=24)
            plt.xticks(y_pos, objects)
            plt.xlabel('', fontsize=16)
            plt.ylabel("Брой ПТП-а", fontsize=16)
            plt.tick_params(axis='both', which='major', labelrotation=90, labelsize=8)
            plt.gcf().subplots_adjust(bottom=0.3)
            plt.show()


def Compare2019vs2018():
    filename = '2019vs2018.csv'
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        labels = []
        year2019 = []
        year2018 = []
        for row in reader:

            if row[0] != 'Общо':
                labels.append(row[0])
                ptp2019 = int(row[1], 10)
                year2019.append(ptp2019)
                ptp2018 = int(row[4], 10)
                year2018.append(ptp2018)



        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars
        fig, ax = plt.subplots(dpi=128, figsize=(10, 6))
        plt.tick_params(axis='both', which='major', labelrotation=90, labelsize=8)
        rects1 = ax.bar(x - width / 2, year2019, width, label='2019')
        rects2 = ax.bar(x + width / 2, year2018, width, label='2018')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Брой ПТП-та')
        ax.set_title('Сравнение броя ПТП-та през първите 6 месеца на 2019 и 2018')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()

        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')
        autolabel(rects1)
        autolabel(rects2)

        fig.tight_layout()
        plt.show()

def ByHours():
    filename = 'ByHoursAndDays.csv'
    with open(filename, encoding="utf-8-sig") as f:
         reader = csv.reader(f)
         performance = []
         objects = []
         row = next(reader)
         for row in reader:
            if not row[0].startswith("От"):
                continue
            high = int(row[22], 10)
            performance.append(high)
            objects.append(row[0])
         print(performance)
         y_pos = np.arange(len(objects))

         fig = plt.figure(dpi=128, figsize=(10, 6))
         plt.bar(y_pos, performance, align='center', alpha=0.5)
         # Format Plot
         plt.title("Брой ПТП-та спрямо часовия диапазон", fontsize=24)
         plt.xticks(y_pos, objects)
         plt.xlabel('', fontsize=16)
         plt.ylabel("Брой ПТП-а", fontsize=16)
         plt.tick_params(axis='both', which='major', labelrotation=90, labelsize=8)
         plt.gcf().subplots_adjust(bottom=0.3)
         plt.show()
def ByDays():
    filename = 'ByHoursAndDays.csv'
    with open(filename, encoding="utf-8-sig") as f:
         reader = csv.reader(f)
         performance = []
         objects = []

         for row in reader:
            if row[0] == 'Общо':
                for i in range(1,21,3):
                    high = int(row[i], 10)
                    performance.append(high)
            if "понеделник" in row:
                for elem in row:
                    if elem != '':
                        objects.append(elem)
         print(objects)
         print(performance)
         y_pos = np.arange(len(objects))

         fig = plt.figure(dpi=128, figsize=(10, 6))
         plt.bar(y_pos, performance, align='center', alpha=0.5)
         # Format Plot
         plt.title("Брой ПТП-та спрямо деня от седмицата", fontsize=24)
         plt.xticks(y_pos, objects)
         plt.xlabel('', fontsize=16)
         plt.ylabel("Брой ПТП-а", fontsize=16)
         plt.tick_params(axis='both', which='major', labelrotation=90, labelsize=8)
         plt.gcf().subplots_adjust(bottom=0.3)
         plt.show()
def ByTypeOfWay():
    filename = 'ByTypeOfWay.csv'
    with open(filename, encoding="utf-8-sig") as f:
         reader = csv.reader(f)
         sizes = []
         objects = []

         for row in reader:
            if row[0] != "Общо":
                objects.append(row[0])
                high = int(row[1], 10)
                sizes.append(high)
         print(objects)
         print(sizes)

         fig = plt.figure(dpi=128, figsize=(10, 6))
         plt.pie(sizes, labels=objects, autopct='%1.1f%%',
                  startangle=90)
         # Format Plot
         plt.title("Съотношение на ПТП-тата спрямо категорията път'", fontsize=24)
         plt.xlabel('', fontsize=16)
         plt.tick_params(axis='both', which='major', labelrotation=90, labelsize=8)
         plt.gcf().subplots_adjust(bottom=0.3)
         plt.show()
def Compare2019vs2018ByDiedAndInjured():
    filename = '2019vs2018.csv'
    with open(filename, encoding="utf-8-sig") as f:
         reader = csv.reader(f)
         labels = []
         died2018 = []
         died2019 = []
         injured2018 = []
         injured2019 = []
         for row in reader:
             if row[0] != 'Общо':
                 labels.append(row[0])
                 die2018 = int (row[2], 10)
                 died2018.append(die2018)
                 injure2018 = int(row[3], 10)
                 injured2018.append(injure2018)
                 die2019 = int (row[5], 10)
                 died2019.append(die2019)
                 injure2019 = int(row[6], 10)
                 injured2019.append(injure2019)
    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars
    fig, ax = plt.subplots(dpi=128, figsize=(12, 6))
    plt.tick_params(axis='both', which='major', labelrotation=90, labelsize=8)
    ax.bar(x - 2*width/1.4 , died2019, width, label='Загинали 2019')
    ax.bar(x - width/2 , died2018, width, label='Загинали 2018')
    ax.bar(x + width /2, injured2019, width, label='Ранени 2019')
    ax.bar(x + 2*width /1.4, injured2018, width, label='Ранени 2018')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Брой хора')
    ax.set_title('Сравнение на броя загинали и ранение през 2019 и 2018')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()



    fig.tight_layout()
    plt.show()




MyTitle = tkinter.Label(window, text="Справка за тежките ПТП (с пострадали) в България за периода от 01.01.2019 г. до 30.06.2019 г. ", font="Helvetica 16 bold")
MyTitle.pack()

MyButton1 = tkinter.Button(window, text="По области", command=ByRegion)
MyButton1.pack()
MyButton2 = tkinter.Button(window, text="По месеци", command=ByMonth)
MyButton2.pack()
MyButton3 = tkinter.Button(window, text="По часове", command=ByHours)
MyButton3.pack()
MyButton4 = tkinter.Button(window, text="По дни", command=ByDays)
MyButton4.pack()
MyButton5 = tkinter.Button(window, text="По вид на пътя", command=ByTypeOfWay)
MyButton5.pack()
MyButton6 = tkinter.Button(window, text="2019 срещу 2018", command=Compare2019vs2018)
MyButton6.pack()
MyButton7 = tkinter.Button(window, text="2019 срещу 2018 Брой ранени и загинали", command=Compare2019vs2018ByDiedAndInjured)
MyButton7.pack()

image =Image.open("mvr-znak02.jpg")


image = image.resize((int(width*0.5), int(height*0.60)))
photo_image = ImageTk.PhotoImage(image)
label = tkinter.Label(window, image = photo_image)
label.pack()

window.mainloop()
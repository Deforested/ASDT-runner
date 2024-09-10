import matplotlib.pyplot as plt
import tkinter as tk
import random
import winsound

worldRecords = {
    1964: {
        "time" : "10.06",
        "name" : "Bob Hayes"
    },
    1968: {
        "time" : "9.95",
        "name" : "Jim Hines"
    },
    1983: {
        "time" : "9.93",
        "name" : "Calvin Smith"
    },
    1988: {
        "time" : "9.92",
        "name" : "Carl Lewis"
    },
    1991: {
        "time" : "9.86",
        "name" : "Carl Lewis"
    },
    1994: {
        "time" : "9.85",
        "name" : "Leroy Burrel"
    },
    1996: {
        "time" : "9.84",
        "name" : "Donovan Bailey"
    },
    1999: {
        "time" : "9.79",
        "name" : "Maurice Greene"
    },
    2006: {
        "time" : "9.77",
        "name" : "Asafa Powell"
    },
    2007: {
        "time" : "9.74",
        "name" : "Asafa Powell"
    },
    2008: {
        "time" : "9.69",
        "name" : "Usain Bolt"
    },
    2009: {
        "time" : "9.58",
        "name" : "Usain Bolt"
    },
}

years_records = {year: record for year, record in worldRecords.items() if isinstance(year, int)}

worldRecords["Lions"] = {
    "Simba": {
        "time": "8.50", "name": "Simba"
    },
    "Nala": {
        "time": "8.40", "name": "Nala"
    },
    "Scar": {
        "time": "8.57", "name": "Scar"
    },
    "Mufasa": {
        "time": "8.63", "name": "Mufasa"
    },
    "Jussi": {
        "time": "8.92", "name": "Jussi"
    },
    "Pertti": {
        "time": "8.22", "name": "Pertti"
    },
    "Joni": {
        "time": "9.11", "name": "Joni"
    },
    "Kaapo": {
        "time": "7.99", "name": "Kaapo"
    },
    "Kivi": {
        "time": "8.66", "name": "Kivi"
    },
    "Onni": {
        "time": "8.20", "name": "Onni"
    },
    
}

years = list(years_records.keys())
times = [float(years_records[year]["time"]) for year in years]

plt.figure(figsize=(10,6))
plt.plot(years,times)
plt.title("World record progression")
plt.xlabel("Year")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.gca().invert_yaxis()
plt.show()

ikkuna = tk.Tk()
ikkuna.geometry("400x400+300+50")

canvas = tk.Canvas(ikkuna, width=400,height=300,bg="white")
canvas.pack()

canvas.create_line(100, 10, 100, 410, fill="black", width=3)
canvas.create_line(200, 10, 200, 410, fill="red", width=3)

ernestin_x_koordinaatti = 100
ernestin_y_koordinaatti = 150
kernestin_x_koordinaatti = 100
kernestin_y_koordinaatti = 100
kernestin_aika = random.uniform(10, 16)
ernestin_aika = random.uniform(10, 16) 
ernestin_juoksu_nopeus = 100 / ernestin_aika
kernestin_juoksu_nopeus = 100 / kernestin_aika
kernestin_matka = 0
ernestin_matka = 0
paivitysvali = 1000
ernestin_askelkoko = ernestin_juoksu_nopeus * (paivitysvali / 1000)
kernestin_askelkoko = kernestin_juoksu_nopeus * (paivitysvali / 1000)

ernesti_maaliin = False
kernesti_maaliin = False


Ernesti = canvas.create_text(ernestin_x_koordinaatti, ernestin_y_koordinaatti,text="E")
Kernesti = canvas.create_text(kernestin_x_koordinaatti, kernestin_y_koordinaatti,text="K")

def ernestin_juoksu():
    global ernestin_x_koordinaatti, ernestin_matka, ernesti_maaliin

    if ernestin_matka < 100:
        ernestin_matka += ernestin_askelkoko
        ernestin_x_koordinaatti += ernestin_askelkoko
        winsound.Beep(200,200)
        canvas.coords(Ernesti, ernestin_x_koordinaatti, ernestin_y_koordinaatti)

        if ernestin_x_koordinaatti >= 200:
            ernesti_maaliin = True
            print(f"Ernesti juoksi 100 metriä ajassa {ernestin_aika:.2f} sekuntia!")
            tarkista_voittaja()
        else:
            ikkuna.after(paivitysvali, ernestin_juoksu)
    else:
        ernesti_maaliin = True
        tarkista_voittaja()

def kernestin_juoksu():
    global kernestin_x_koordinaatti, kernestin_matka, kernesti_maaliin

    if kernestin_matka < 100:
        kernestin_matka += kernestin_askelkoko
        kernestin_x_koordinaatti += kernestin_askelkoko
        winsound.Beep(400,200)
        canvas.coords(Kernesti, kernestin_x_koordinaatti, kernestin_y_koordinaatti)

        if kernestin_x_koordinaatti >= 200:
            kernesti_maaliin = True
            print(f"Kernesti juoksi 100 metriä ajassa {kernestin_aika:.2f} sekuntia!")
            tarkista_voittaja()
        else:
            ikkuna.after(paivitysvali, kernestin_juoksu)
    else:
        kernesti_maaliin = True
        tarkista_voittaja()

def yhteis_lahto():
    winsound.Beep(250,1500)
    ernestin_juoksu()
    kernestin_juoksu()

def tarkista_voittaja():
    if ernesti_maaliin and kernesti_maaliin:
        if ernestin_aika < kernestin_aika:
            print("Ernesti voitti")
        elif kernestin_aika < ernestin_aika:
            print("Kernesti voitti")
        else:
            print("Tasapeli")        

painike = tk.Button(ikkuna,text="Ernesti",command=ernestin_juoksu)
painike.pack(side="left", pady=20, padx=20)
painike2 = tk.Button(ikkuna,text="Kernesti",command=kernestin_juoksu)
painike2.pack(side="left", pady=20, padx=20)
painike3 = tk.Button(ikkuna,text="Yhteislähtö",command=yhteis_lahto)
painike3.pack(side="left", pady=20, padx=20,)

ikkuna.mainloop()
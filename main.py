from bank import Bank

def menü_anzeigen():
    print("\n1. Kontostand anzeigen")
    print("2.Geld einzahlen")
    print("3.Geld abheben")
    print("4.Beenden")

def run():
    bank=Bank()
    pin = input("Bitte geben Sie Ihre PIN ein: ")

    user = bank.login(pin)
    if not user:
        print("Falsche PIN.")
        return

    while True:
        menü_anzeigen()
        wahl = input("Wählen Sie eine Option:")

        if wahl == "1":
            print(f"Kontostand: {user.kontostand():.2f} €")
        elif wahl == "2":
            betrag = float(input("Betrag zum Einzahlen: "))
            user.einzahlen(betrag)
            print("Einzahlung erfolgreich.")
        elif wahl == "3":
            betrag = float(input("Betrag zum Abheben: "))
            if user.abheben(betrag):
                print("Abhebung erfolgreich.")
            else:
                print("Nicht genug Guthaben.")
        elif wahl == "4":
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungünstige Auswahl.")

    if __name__ == "__main__":
        run()

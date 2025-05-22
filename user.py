class User:
    def __init(self, pin: str, balance: float = 0.0):
        self.pin = pin
        self.balance = balance

    def einzahlen(self, betrag: float):
        self.balance += betrag

    def abheben(self, betrag: float) -> bool:
        if betrag <= self.balance:
            self.balance -= betrag
            return True
        return False

    def kontostand(self) -> float:
        return  self.balance
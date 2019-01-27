class CashMashine:
    is available = False

    def __init__


    @property
    def is_available(self):
        return False


def test_cash_mashine_is_not_available():
    cash_maschine = CashMshine()
    assert not cash_mashine.is_available()

def test_cash_mashine_put_money():
    cash_maschine = CashMachine()
    cash_machine.put_money ([200, 100, 100, 50])
    assert cash_machine.is_available
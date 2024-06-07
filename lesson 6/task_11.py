import json

import requests

token = '4123saedfasedfsadf4324234f223ddf23'


class LegalAPI:

    BASE_URL = 'https://legal-api.sirotinsky.com'

    def __init__(self, token):
        self.token = token

    def root(self):
        """
        проверка обращения к base_url
        """
        url = f"{self.BASE_URL}"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

    def efrsb_publisher_messages(self, inn):
        """
        возвращает сведения о банкроствах по ИНН лица, включившего такие сведения в ЕФРСБ
        """
        # строка ниже - конструирование URL
        url = f"{self.BASE_URL}/{self.token}/efrsb/publisher_messages/{inn}"
        r = requests.get(url)
        # строка ниже - проверка на 200-й код (если что-то другое, то код будет "падать")
        r.raise_for_status()
        return r.json()

    def efrsb_debtor_messages(self, inn):
        """
        возвращает сведения о банкростве по ИНН должника
        """
        url = f"{self.BASE_URL}/{self.token}/efrsb/debtor_messages/{inn}"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

    def efrsb_manager_all(self):
        """
        возвращает сведения обо всех арбитражных управляюших
        """
        url = f"{self.BASE_URL}/{self.token}/efrsb/manager/all"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

    def efrsb_manager_inn(self, inn):
        """
        возвращает сведения об арбитражном управляюшем по его ИНН
        """
        url = f"{self.BASE_URL}/{self.token}/efrsb/manager/{inn}"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

    def efrsb_trader_all(self):
        """
        возвращает сведения об организаторах торгов
        """
        url = f"{self.BASE_URL}/{self.token}/efrsb/trader/all"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

    def efrsb_trader_inn(self, inn):
        """
        возвращает сведения об организоваторе торгов по его ИНН
        """
        url = f"{self.BASE_URL}/{self.token}/efrsb/trader/{inn}"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

    def efrsb_person_inn(self, inn):
        """
         возвращает сведения о должнике - физ.лице по его ИНН
        """
        url = f"{self.BASE_URL}/{self.token}/efrsb/person/{inn}"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

    def efrsb_organisation_inn(self, inn):
        """
        возвращает сведения о должнике - юр.лице по его ИНН
        """
        url = f"{self.BASE_URL}/{self.token}/efrsb/organisation/{inn}"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()

def main():
    api = LegalAPI(token)

    # root = api.root()
    # print(root)

    # publisher_messages = api.efrsb_publisher_messages(644101410002)
    # ниже вывожу полученные данные через print - вопрос, как их увидеть через дебаггер?
    # print(publisher_messages)

    # debtor_messages = api.efrsb_debtor_messages(7727442614)
    # print(debtor_messages)

    # managers = api.efrsb_manager_all()
    # print(managers)

    # manager = api.efrsb_manager_inn(263411857320)
    # print(manager)

    # traders = api.efrsb_trader_all()
    # print(traders)

    # trader = api.efrsb_trader_inn(5003059717)
    # print(trader)

    # person = api.efrsb_person_inn(380409658341)
    # print(person)

    # organisation = api.efrsb_organisation_inn(7717655500)
    # print(json.dumps(organisation))

# запускаем программу путем вызова функции main
main()
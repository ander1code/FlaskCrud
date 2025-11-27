class Format(object):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Format, cls).__new__(cls)
        return cls.__instance

    def salary_format(self, salary):
        import locale
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(salary / 100, grouping=True)
    
    def birthday_format(self, birthday):
        if not birthday:
            return ""
        return birthday.strftime("%d/%m/%Y")
    
    def decimal_to_maskmoney(self, salary):
        if salary is None:
            return ''
        return f"{salary:.2f}".replace('.', ',')

    def maskmoney_to_decimal(self, value: str):
        if not value:
            return None
        value = value.replace("R$", "").strip()
        value = value.replace('.', '').replace(',', '.')
        try:
            return float(value)
        except ValueError:
            return None
        
    def generate_sha512(self, data):
        import hashlib
        hash_obj = hashlib.sha512(data.encode()) 
        hash_hex = hash_obj.hexdigest()
        return hash_hex



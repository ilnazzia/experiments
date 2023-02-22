from string import ascii_lowercase, digits

class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        self.check_name(name)

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
    
    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")
        for char in name:
            if char not in cls.CHARS_CORRECT:
                raise ValueError("некорректное поле name")

class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        self.check_name(name)

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
    
    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")
        for char in name:
            if char not in cls.CHARS_CORRECT:
                raise ValueError("некорректное поле name")

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
print(login)
html = login.render_template()
print(html)

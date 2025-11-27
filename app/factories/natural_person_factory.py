from werkzeug.utils import secure_filename
from app.models.person import Person
from app.models.natural_person import NaturalPerson

class NaturalPersonFactory(object):
    __instance = None

    def __new__(cls, dto):
        if cls.__instance is None:
            cls.__instance = super(NaturalPersonFactory, cls).__new__(cls)
        cls.dto = dto
        return cls.__instance

    def create_person(self):
        obj = Person(
            name=self.dto.name, 
            email=self.dto.email, 
            status=self.dto.status, 
            description=self.dto.description, 
        )
        return obj
    
    def create_natural_person(self):
        import os

        print(type(self.dto.salary))
        picture_filename = None

        if self.dto.picture:
            picture_filename = secure_filename(self.dto.picture.filename)
            upload_folder = "app/static/pictures"
            os.makedirs(upload_folder, exist_ok=True)
            picture_path = os.path.join(upload_folder, picture_filename)
            self.dto.picture.save(picture_path)

        obj = NaturalPerson(
            cpf=self.dto.cpf.replace('.', '').replace('-', ''),
            gender=self.dto.gender,
            salary=self.dto.salary,
            birthday=self.dto.birthday,
            picture=picture_filename 
        )
        return obj

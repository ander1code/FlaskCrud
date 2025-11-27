from app.factories.natural_person_factory import NaturalPersonFactory
from app.models.person import Person
from app.models.natural_person import NaturalPerson
from app.configs.database import db

class NaturalPersonService(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(NaturalPersonService, cls).__new__(cls)
        return cls.__instance

    def create_natural_person(self, dto):
        npf = NaturalPersonFactory(dto=dto)
        person = npf.create_person()
        try:
            db.session.add(person)
            db.session.flush()
            natural_person = npf.create_natural_person()
            natural_person.person_id = person.id
            db.session.add(natural_person)
            db.session.commit()
            return True
        except Exception as error:
            print(f'Creation error: {error}')
            db.session.rollback()
            return False
        
    def get_natural_person_by_name(self, name_filter=None):
        query = (
            db.session
            .query(NaturalPerson)
            .join(Person, NaturalPerson.person_id == Person.id)
            .order_by(Person.id.desc())
        )
        if name_filter:
            query = query.filter(Person.name.like(f"{name_filter}%"))
        return query
    
    def get_all_natural_person(self):
        return (
            db.session
            .query(NaturalPerson)
            .join(Person, NaturalPerson.person_id == Person.id)
            .order_by(Person.id.desc())
        )
    
    def get_natural_person_by_id(self, id):
        return (
            db.session
            .query(Person, NaturalPerson)
            .join(Person, Person.id == NaturalPerson.person_id)
            .filter(NaturalPerson.id == id)
            .first()
        )
    
    def edit_natural_person(self, id, dto):
        old_person, old_natural_person = self.get_natural_person_by_id(id)
        if old_person is None or old_natural_person is None:
            return None
        try:
            old_person.name = dto.name or old_person.name
            old_person.email = dto.email or old_person.email

            old_natural_person.birthday = getattr(dto, 'birthday', old_natural_person.birthday)
            old_natural_person.cpf = dto.cpf or old_natural_person.cpf
            old_natural_person.gender = dto.gender or old_natural_person.gender
            old_natural_person.salary = dto.salary or old_natural_person.salary

            if getattr(dto, 'picture', None):
                from werkzeug.utils import secure_filename
                import os
                upload_folder = "app/static/pictures"
                os.makedirs(upload_folder, exist_ok=True)
                picture_filename = secure_filename(dto.picture.filename)
                picture_path = os.path.join(upload_folder, picture_filename)
                dto.picture.save(picture_path)
                old_natural_person.picture = picture_filename

            db.session.commit()
            return True
            
        except Exception as error:
            print(f'Error: {error}')
            db.session.rollback()
            return False
    
    def delete_natural_person(self, id):
        person, natural_person = self.get_natural_person_by_id(id)

        if person is None or natural_person is None:
            return False

        try:
            db.session.delete(natural_person)
            db.session.delete(person)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
from db.entities import Data
from models.data_dto import DataDTO
from db.orm import db


class DataService:

    def entry_into_db(self, data_dto:dict):
        print(data_dto)
        data = Data(id=data_dto.id,
            userId=data_dto.userId,
            title=data_dto.title,
            body=data_dto.body
        )
        print(data)
        db.session.add(data)
        db.session.commit()
        db.session.flush()

    def get_all(self):
        res = Data.query.all()
        dtos = []
        if res != None:
            for data in res:
                dto = DataDTO(
                    id=data.id,
                    userId=data.userId,
                    title=data.title,
                    body=data.body
                )
                dtos.append(dto)
        return dtos
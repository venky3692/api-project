from src.db import db
from sqlalchemy import String, DateTime
from datetime import datetime

class file_db(db.Model):
    __tablename__ = 'files'
    source_file_name = db.Column(String(350))
    converted_file_name = db.Column(String(500))
    time_stamp = db.Column(DateTime, default=datetime.utcnow, primary_key = True)

    def __repr__(self) -> str:
        rep = f'File_data + {self.source_file_name} + "," + {self.converted_file_name} + "," + {self.time_stamp}'
        return rep
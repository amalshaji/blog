import databases
import ormar
import sqlalchemy

database = databases.Database("sqlite:///db.sqlite")
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata


class Users(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=64, unique=True)
    password: str = ormar.String(max_length=128)
    is_active: bool = ormar.Boolean(default=True)

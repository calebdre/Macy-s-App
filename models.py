import peewee

db = peewee.SqliteDatabase('macys.db')

class BaseModel(peewee.Model):
        class Meta:
                database = db

class Item(BaseModel):
        code = peewee.CharField(unique=True)
        image_url = peewee.CharField()
        price = peewee.DoubleField()
	name = peewee.CharField()

class Review(BaseModel):
        code = peewee.ForeignKeyField(Item, related_name='reviews')
        stars = peewee.IntegerField()
        comment = peewee.CharField()

if __name__ == '__main__':
	db.create_tables([Item, Review])

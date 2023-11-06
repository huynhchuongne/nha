from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from saleappv2.app import db, app

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image =Column(String(100), default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id),nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        c1 = Product(name='Ihone 13', price= 2000000, category_id=1)
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Desktop')
        db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        db.session.commit()

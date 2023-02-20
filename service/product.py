from models.product import Product
from schemas.product import Product

class ProductService():
    def __init__(self, db) -> None:
        self.db = db

        def get_products(self):
            result = self.db.query(Product).all()
            return result

        def get_product(self, id):
            result = self.db.query(Product).filter(Product.id == id).first()
            return result

        def get_productos_by_name(self, name):
            result = self.db.query(Product).filter(Product.name == name).all()
            return result

        def create_product(self,product: Product):
            new_product = Product(**product.dict())
            self.db.add(new_product)
            self.db.commit()
            return

        def update_product(self, id: int, data: Product):
            product = self.db.query(Product).filter(Product.id == id).first()
            product.name = data.name
            product.price = data.price
            self.db.commit()
            return

        def delete_product(self, id:int):
            product = self.db.query(Product).filter(Product.id == id).first()
            self.db.delete(product)
            self.db.commit()
            return


from saleapp import admin, db
from flask_admin.contrib.sqla import  ModelView
from saleapp.models import Category, Product
from flask_admin import BaseView

class Contact(BaseView):
    def index(self):
        return self.render('')

admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product,db.session))

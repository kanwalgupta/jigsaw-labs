from api.lib.db import *
from api.lib.orm import build_from_record
import api.models as models
class Order:
    __table__ = 'orders'
    columns = ['id', 'customer_id', 'drink_id', 'bartender_id']
    
    def customer(self):
        cursor.execute('SELECT * FROM customers WHERE id = ?', (self.customer_id,))
        customer_record = cursor.fetchone()
        return build_from_record(models.Customer, customer_record)
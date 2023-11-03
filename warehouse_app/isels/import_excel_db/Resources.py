from import_export import resources
from .models import Inventory
 
class InventoryResource(resources.ModelResource):
    class Meta:
        model = Inventory
from models.base_model import BaseModel
class Amenity(BaseModel):
    name = ""
    def __init__(self,*args, **kwargs):
        """Inzialize amenity instance"""
        super().__init__(*args, **kwargs)
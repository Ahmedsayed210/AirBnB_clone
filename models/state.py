from models.base_model import BaseModel
class State(BaseModel):
    name = ""
    def __init__(self, *args, **kwargs):
        """Inzialize state instance"""
        super().__init__(*args, **kwargs)
        
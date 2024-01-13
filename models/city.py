from models.base_model import BaseModel
class City(BaseModel):
    state_id = ""
    name = ""
    def __init__(self, *args, **kwargs):
        """Inzialize city instancce """
        super().__init__(*args, **kwargs)
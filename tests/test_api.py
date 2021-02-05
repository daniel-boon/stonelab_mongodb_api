import main
import pytest
from main import app
db = None

@pytest.mark.asyncio
async def test():
    
def test_ma_repair_data():
    ma_repair_data = db.get_data('2020-01-01 00:37:07.897')
    assert ma_repair_data['toolName'] == 'Boiler'
    assert ma_repair_data['maNote'] == 'ปกติ'
    assert ma_repair_data['plantAlias'] == 'NJ'
    assert ma_repair_data["submitBy"] == 'Vijai phantumart'

client = TestClient(app)

# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello Wrold"}


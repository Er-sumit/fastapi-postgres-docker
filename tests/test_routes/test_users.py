from datetime import datetime
dt_string = datetime.now().strftime("%d%m%Y%H%M%S")
myemail = f"testuse{dt_string}@nofoobar.com"
def test_create_user(client):
    data = {"email":myemail,"password":"testing"}
    response = client.post("/user",json=data)
    assert response.status_code == 200
    assert response.json()["email"] == myemail
    assert response.json()["is_active"] == True
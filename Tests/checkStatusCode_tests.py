import pytest
from IntermidiatePython.restapi import checkSatusCode

url = "https://jsonplaceholder.typicode.com/posts/1"

def test_checkStatusCode():
    response = checkSatusCode(url)
    assert response.status_code == 200

def test_checkUserIdInResponse():
    response = checkSatusCode(url)
    assert "userId" in response.json()

# assert "userId" in response.json()


if __name__ == "__main__":
    pytest.main()
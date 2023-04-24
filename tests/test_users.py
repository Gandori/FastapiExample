from httpx import Response

from tests.__util import Request

request = Request()


def test_all() -> None:
    result: Response = request.get(route='/users')
    assert result.status_code == 200


def test_new(user_payload) -> None:
    result: Response = request.post(route='/users', json=user_payload)
    assert result.status_code == 200


def test_delete(random_id) -> None:
    result: Response = request.delete(route=f'/users/{random_id}')
    assert result.status_code == 200


def test_update(random_id, user_payload) -> None:
    result: Response = request.put(route=f'/users/{random_id}', json=user_payload)
    assert result.status_code == 200

from httpx import Response

from tests.__util import Request

request = Request()


def test_all() -> None:
    result: Response = request.get(route='/items')
    assert result.status_code == 200


def test_new(random_id, item_payload) -> None:
    route: str = f'/items/{random_id}'
    result: Response = request.post(route=route, json=item_payload)
    assert result.status_code == 200


def test_delete(random_id) -> None:
    result: Response = request.delete(route=f'/items/{random_id}')
    assert result.status_code == 200


def test_update(random_id, item_payload) -> None:
    result: Response = request.put(route=f'/items/{random_id}', json=item_payload)
    assert result.status_code == 200

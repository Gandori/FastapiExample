from httpx import Response

from tests.__util import Request, thread_decorator

request = Request()


@thread_decorator
def test_example2() -> None:
    result: Response = request.get_request(route='/example2')
    assert result.status_code == 200

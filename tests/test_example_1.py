from httpx import Response

from tests.__util import Request, thread_decorator

request = Request()


@thread_decorator
def test_example1() -> None:
    result: Response = request.get_request(route='/example1')
    assert result.status_code == 200

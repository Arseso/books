_requests_queue = []


def append_to_queue(request: str) -> None:
    global _requests_queue
    _requests_queue.append(request)


def pop_from_queue() -> str:
    global _requests_queue
    return _requests_queue.pop(0)


def is_queue_not_empty() -> bool:
    return len(_requests_queue) != 0

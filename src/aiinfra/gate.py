class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    if body.get("desired") != body.get("live"): failed.append("drift")
    return {"passed": not failed, "failed": failed, "applied": False}

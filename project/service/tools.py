def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, dict):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))
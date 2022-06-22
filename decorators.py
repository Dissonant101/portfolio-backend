def singleton(cls):
    """Singleton decorator. Only allows one instance of a connection."""

    instances = {}

    def get_instance(*args, **kwargs):
        """Gets instance if it exists or creates an instance."""
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

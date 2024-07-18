def set_global():
    d = {"a": 1, "b": 2}
    globals().update(d)


if __name__ == "__main__":
    set_global()
    print(globals().get("a", None))

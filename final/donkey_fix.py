def donkey_fix(name, chars):
    """
    >>> donkey_fix('coco-elizabeth donkey', 'oy')
    'cc-elizabeth dnke'

    >>> donkey_fix('coco', 'c')
    'oo'
    """
    if len(name) <= 1:
        if name in chars:
            return ""
        return name
    return donkey_fix(name[0], chars) + donkey_fix(name[1:], chars)
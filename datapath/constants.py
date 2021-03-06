# -------------------------------------------------------------------------- #
# These keys form a single integer bit vector, and therefore cannot repeat
# the same values

TYPE_LEAF = 1
TYPE_LIST = 2
TYPE_DICT = 4
TYPE_MASK = 0x000F

KEY_LITERAL = 1 << 8
KEY_WILD = 2 << 8
KEY_RECURSE = 4 << 8  # TODO - Is recurse a key type or a traversal?
KEY_MASK = 0x00F0

ANCHOR_LOCAL = 1 << 16
ANCHOR_ABSOLUTE = 2 << 16
ANCHOR_MASK = 0x0F00


# -------------------------------------------------------------------------- #

CHARS_RESERVED = '."[]'
CHARS_WILD = '*'
# TODO - This isn't used, we look for the chars separately in the parser
CHARS_RECURSE = '..'

WALK_CONTINUE = None
WALK_TERMINATE = 1
WALK_PRUNE = 2

ON_MISSING_CONTINUE = 3
ON_MISSING_CREATE = 4

ON_MISMATCH_CONTINUE = 6
ON_MISMATCH_FAIL = 5

# -------------------------------------------------------------------------- #
# These values are compound values of the above

STRINGS = {
    TYPE_LEAF: 'TYPE_LEAF',
    TYPE_LIST: 'TYPE_LIST',
    TYPE_DICT: 'TYPE_DICT',
    KEY_LITERAL: 'KEY_LITERAL',
    KEY_WILD: 'KEY_WILD',
    KEY_RECURSE: 'KEY_RECURSE'
}

TYPE_TO_TYPE_CODE = {
    dict: TYPE_DICT,
    list: TYPE_LIST,
    tuple: TYPE_LIST,
    str: TYPE_LEAF,
    int: TYPE_LEAF,
    unicode: TYPE_LEAF
}

TYPE_CODE_TO_TYPE = {
    TYPE_DICT: dict,
    TYPE_LIST: list,
    TYPE_LEAF: lambda: None,
}

# -------------------------------------------------------------------------- #
# Helper functions related to constants


def describe(bit_constant):
    labels = []
    for code, description in STRINGS.iteritems():
        if code & bit_constant:
            labels.append(description)

    return labels


def describe_path(path_parts):
    return tuple((describe(bits), value) for bits, value in path_parts)



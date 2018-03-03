from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class HashTests(TranspileTestCase):
    pass


class BuiltinHashFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["hash"]

    not_implemented = [
        'test_bool',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_float',
        'test_frozenset',
        'test_int',
        'test_list',
        'test_None',
        'test_NotImplemented',
        'test_range',
        'test_set',
        'test_str',
        'test_tuple',
    ]

#!/usr/bin/env python3

# i found this online. it might check a pickle object for rce but need to verify

import builtins
import io
import pickle
import collections
import torch
import os
import numpy
import _codecs

def encode(*args):
    out = _codecs.encode(*args)
    print(f'encode({args}) = {out}')
    return out

class RestrictedUnpickler(pickle.Unpickler):
    def persistent_load(self, saved_id):
        assert saved_id[0] == 'storage'
        return torch.storage._TypedStorage()

    def find_class(self, module, name):
        print(f'find class {module} {name}')
        if module == 'collections' and name == 'OrderedDict':
            return getattr(collections, name)
        if module == 'torch._utils' and name == '_rebuild_tensor_v2':
            return torch._utils._rebuild_tensor_v2
        if module == 'torch' and name in ['FloatStorage', 'HalfStorage']:
            return torch.FloatStorage
        if module == 'numpy.core.multiarray' and name == 'scalar':
            return numpy.core.multiarray.scalar
        if module == 'numpy' and name == 'dtype':
            return numpy.dtype
        if module == '_codecs' and name == 'encode':
            return encode
        # Forbid everything else.
        raise pickle.UnpicklingError("global '%s/%s' is forbidden" %
                                     (module, name))

def restricted_loads(s):
    """Helper function analogous to pickle.loads()."""
    return RestrictedUnpickler(io.BytesIO(s)).load()

# To test that it catches this RCE:
# restricted_loads(b"cos\nsystem\n(S'echo hello world'\ntR.")

# unzip model.ckpt archive/data.pkl
with open('archive/data.pkl', 'rb') as f: st = f.read()
d = restricted_loads(st)
print(dir(d))
print(d.keys())
print(d['callbacks'])

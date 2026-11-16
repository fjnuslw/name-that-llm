"""G07 outer fusion. Public-parent/postprocessing implementations are external.

Formula follows the credited Omer V1 pipeline. This standalone interface
exposes the project's configurable outer shares; it does not ship trained assets.
"""
import numpy as np

def softmax(x):
    x = np.asarray(x, dtype=np.float64)
    x = x - x.max(axis=-1, keepdims=True)
    e = np.exp(x)
    return e / e.sum(axis=-1, keepdims=True)

def fuse(parent, own27, own9_logp, postprocess, a27=.55, b9=.4):
    """postprocess receives N x 18 probabilities and returns probabilities."""
    parent = np.asarray(parent, dtype=np.float64)
    own27 = np.asarray(own27, dtype=np.float64)
    own9_logp = np.asarray(own9_logp, dtype=np.float64)
    if not (0 <= a27 <= 1 and 0 <= b9 < 1):
        raise ValueError("invalid shares")
    if parent.ndim != 2 or parent.shape[1] != 18:
        raise ValueError("parent must be N x 18")
    if own27.shape != parent.shape or own9_logp.shape != (5, *parent.shape):
        raise ValueError("unaligned branch shapes")
    for p in (parent, own27, np.exp(own9_logp)):
        if not np.isfinite(p).all() or (p < 0).any() or not np.allclose(p.sum(-1), 1, atol=1e-6):
            raise ValueError("invalid probabilities")
    p1 = (1-a27)*parent + a27*own27
    output = []
    for lp in own9_logp:
        q = softmax((1-b9)*np.log(np.maximum(p1, 1e-15)) + b9*lp)
        p = np.asarray(postprocess(q), dtype=np.float64)
        if p.shape != parent.shape or not np.isfinite(p).all() or (p < 0).any() or not np.allclose(p.sum(-1), 1, atol=1e-6):
            raise ValueError("postprocess must return aligned probabilities")
        output.append(p)
    return np.mean(output, axis=0)

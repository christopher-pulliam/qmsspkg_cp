import pandas as pd
"""
    Concatenates two pandas categoricals.

    Parameters
    ----------
    a : pandas.core.arrays.categorical.Categorical
      A pandas categorical.
    b : pandas.core.arrays.categorical.Categorical
      A pandas categorical that you wish to concatenate to a.

    Returns
    -------
    pandas.core.arrays.categorical.Categorical
      The new concatenated pandas categorical.

    Examples
    --------
    >>> from qmsspkg import qmsspkg
    >>> a = pd.Categorical(["character", "hits", "your", "eyeballs"])
    >>> b = pd.Categorical(["but", "integer", "where it", "counts"])
    >>> qmsspkg.catbind(a, b)
    [character, hits, your, eyeballs, but, integer, where it, counts]
    Categories (8, object): [but, character, counts,
    eyeballs, hits, integer, where it, your]
    """
def catbind(a, b):
  concatenated = pd.concat([pd.Series(a.astype("str")),
                            pd.Series(b.astype("str"))])
  return pd.Categorical(concatenated)
Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> import pandas
>>> df1-pandas.DataFrame([2,4,6],[10,20,30])
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'df1' is not defined
>>> df1 = pandas.DataFrame([2,4,6],[10,20,30])
>>> df1
    0
10  2
20  4
30  6
>>> df1 = pandas.DataFrame([[2,4,6],[10,20,30]])
>>> df1
    0   1   2
0   2   4   6
1  10  20  30
>>> df1 = pandas.DataFrame([[2,4,6],[10,20,30]],columns = ["price","age","value"])
>>> df1
   price  age  value
0      2    4      6
1     10   20     30
>>> df1 = pandas.DataFrame([[2,4,6],[10,20,30]],columns = ["price","age","value"], index = ["First","Second"])
>>> df1
        price  age  value
First       2    4      6
Second     10   20     30
>>> df2 = pandas.DataFrame([("Name":"John"),("Name":"Jack")])
  File "<console>", line 1
    df2 = pandas.DataFrame([("Name":"John"),("Name":"Jack")])
                                   ^
SyntaxError: invalid syntax
>>> df2 = pandas.DataFrame([("Name":"John"),("Name":"Jack")])
  File "<console>", line 1
    df2 = pandas.DataFrame([("Name":"John"),("Name":"Jack")])
                                   ^
SyntaxError: invalid syntax
>>> df2 = pandas.DataFrame([("Name":"John"),("Name":"Jack")])
  File "<console>", line 1
    df2 = pandas.DataFrame([("Name":"John"),("Name":"Jack")])
                                   ^
SyntaxError: invalid syntax
>>> df2 = pandas.DataFrame([("Name":"John","surname":"Joooo"),("Name":"Jack")])
  File "<console>", line 1
    df2 = pandas.DataFrame([("Name":"John","surname":"Joooo"),("Name":"Jack")])
                                   ^
SyntaxError: invalid syntax
>>> df1
        price  age  value
First       2    4      6
Second     10   20     30
>>> df2
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'df2' is not defined
>>> df2 = pandas.DataFrame([{"Name":"John","surname":"Joooo"},{"Name":"Jack"})
  File "<console>", line 1
    df2 = pandas.DataFrame([{"Name":"John","surname":"Joooo"},{"Name":"Jack"})
                                                                             ^
SyntaxError: invalid syntax
>>> df2 = pandas.DataFrame([{"Name":"John","surname":"Joooo"},{"Name":"Jack"}])
>>> df2
   Name surname
0  John   Joooo
1  Jack     NaN
>>> df1
        price  age  value
First       2    4      6
Second     10   20     30
>>> type(df1)
<class 'pandas.core.frame.DataFrame'>
>>> df1.mean()
price     6.0
age      12.0
value    18.0
dtype: float64
>>> dir(df1)
['T', '_AXIS_ALIASES', '_AXIS_IALIASES', '_AXIS_LEN', '_AXIS_NAMES', '_AXIS_NUMBERS', '_AXIS_ORDERS', '_AXIS_REVERSED', '_AXIS_SLICEMAP', '__abs__', '__add__', '__and__', '__array__', '__array_wrap__', '__bool__', '__bytes__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__div__', '__doc__', '__eq__', '__finalize__', '__floordiv__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__invert__', '__ipow__', '__isub__', '__iter__', '__itruediv__', '__le__', '__len__', '__lt__', '__mod__', '__module__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__or__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__unicode__', '__weakref__', '__xor__', '_accessors', '_add_numeric_operations', '_add_series_only_operations', '_add_series_or_dataframe_operations', '_agg_by_level', '_align_frame', '_align_series', '_apply_broadcast', '_apply_empty_result', '_apply_raw', '_apply_standard', '_at', '_box_col_values', '_box_item_values', '_check_inplace_setting', '_check_is_chained_assignment_possible', '_check_percentile', '_check_setitem_copy', '_clear_item_cache', '_combine_const', '_combine_frame', '_combine_match_columns', '_combine_match_index', '_combine_series', '_combine_series_infer', '_compare_frame', '_compare_frame_evaluate', '_consolidate_inplace', '_construct_axes_dict', '_construct_axes_dict_for_slice', '_construct_axes_dict_from', '_construct_axes_from_arguments', '_constructor', '_constructor_expanddim', '_constructor_sliced', '_convert', '_count_level', '_create_indexer', '_dir_additions', '_dir_deletions', '_ensure_valid_index', '_expand_axes', '_flex_compare_frame', '_from_arrays', '_from_axes', '_get_agg_axis', '_get_axis', '_get_axis_name', '_get_axis_number', '_get_axis_resolvers', '_get_block_manager_axis', '_get_bool_data', '_get_cacher', '_get_index_resolvers', '_get_item_cache', '_get_numeric_data', '_get_values', '_getitem_array', '_getitem_column', '_getitem_frame', '_getitem_multilevel', '_getitem_slice', '_iat', '_iget_item_cache', '_iloc', '_indexed_same', '_info_axis', '_info_axis_name', '_info_axis_number', '_info_repr', '_init_dict', '_init_mgr', '_init_ndarray', '_internal_names', '_internal_names_set', '_is_cached', '_is_datelike_mixed_type', '_is_mixed_type', '_is_numeric_mixed_type', '_is_view', '_ix', '_ixs', '_join_compat', '_loc', '_maybe_cache_changed', '_maybe_update_cacher', '_metadata', '_needs_reindex_multi', '_protect_consolidate', '_reduce', '_reindex_axes', '_reindex_axis', '_reindex_columns', '_reindex_index', '_reindex_multi', '_reindex_with_indexers', '_repr_fits_horizontal_', '_repr_fits_vertical_', '_repr_html_', '_repr_latex_', '_reset_cache', '_reset_cacher', '_sanitize_column', '_series', '_set_as_cached', '_set_axis', '_set_axis_name', '_set_is_copy', '_set_item', '_setitem_array', '_setitem_frame', '_setitem_slice', '_setup_axes', '_slice', '_stat_axis', '_stat_axis_name', '_stat_axis_number', '_typ', '_unpickle_frame_compat', '_unpickle_matrix_compat', '_update_inplace', '_validate_dtype', '_values', '_where', '_xs', 'abs', 'add', 'add_prefix', 'add_suffix', 'age', 'align', 'all', 'any', 'append', 'apply', 'applymap', 'as_blocks', 'as_matrix', 'asfreq', 'asof', 'assign', 'astype', 'at', 'at_time', 'axes', 'between_time', 'bfill', 'blocks', 'bool', 'boxplot', 'clip', 'clip_lower', 'clip_upper', 'columns', 'combine', 'combineAdd', 'combineMult', 'combine_first', 'compound', 'consolidate', 'convert_objects', 'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'dropna', 'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'eval', 'ewm', 'expanding', 'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 'floordiv', 'from_csv', 'from_dict', 'from_items', 'from_records', 'ftypes', 'ge', 'get', 'get_dtype_counts', 'get_ftype_counts', 'get_value', 'get_values', 'groupby', 'gt', 'head', 'hist', 'iat', 'icol', 'idxmax', 'idxmin', 'iget_value', 'iloc', 'index', 'info', 'insert', 'interpolate', 'irow', 'is_copy', 'isin', 'isnull', 'items', 'iteritems', 'iterkv', 'iterrows', 'itertuples', 'ix', 'join', 'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lookup', 'lt', 'mad', 'mask', 'max', 'mean', 'median', 'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 'ndim', 'ne', 'nlargest', 'notnull', 'nsmallest', 'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 'price', 'prod', 'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_axis', 'reindex_like', 'rename', 'rename_axis', 'reorder_levels', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 'rpow', 'rsub', 'rtruediv', 'sample', 'select', 'select_dtypes', 'sem', 'set_axis', 'set_index', 'set_value', 'shape', 'shift', 'size', 'skew', 'slice_shift', 'sort', 'sort_index', 'sort_values', 'sortlevel', 'squeeze', 'stack', 'std', 'style', 'sub', 'subtract', 'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dense', 'to_dict', 'to_excel', 'to_gbq', 'to_hdf', 'to_html', 'to_json', 'to_latex', 'to_msgpack', 'to_panel', 'to_period', 'to_pickle', 'to_records', 'to_sparse', 'to_sql', 'to_stata', 'to_string', 'to_timestamp', 'to_xarray', 'transpose', 'truediv', 'truncate', 'tshift', 'tz_convert', 'tz_localize', 'unstack', 'update', 'value', 'values', 'var', 'where', 'xs']
>>> df1.mean()
price     6.0
age      12.0
value    18.0
dtype: float64
>>> df1.mean().mean
<bound method Series.mean of price     6.0
age      12.0
value    18.0
dtype: float64>
>>> df1.mean().mean()
12.0
>>> type(df1.mean())
<class 'pandas.core.series.Series'>
>>> df1.Price
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\MALOA\AppData\Local\Programs\Python\Python35\lib\site-packages\pandas\core\generic.py", line 2744, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'Price'
>>> df1.price
First      2
Second    10
Name: price, dtype: int64
>>> type(df1.price)
<class 'pandas.core.series.Series'>
>>> df1.price.mean()
6.0
>>> df1.price.mean().mean()
6.0
>>> df1.price.mean().max()
6.0
>>> df1.price.max()
10
>>> 
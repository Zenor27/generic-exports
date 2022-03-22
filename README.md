# Benchmarks / Logs

## CPython

```
Called export_users
Called get_data
Done get_data in 27.031921863555908 seconds
retrieved 100000 users
Called generic_export
Called handle_xlsx
Done handle_xlsx in 14.340934753417969 seconds
Done generic_export in 17.85335612297058 seconds
Done export_users in 47.80450987815857 seconds
```

## Pypy

```
Called export_users
Called get_data
Done get_data in 14.208070993423462 seconds
Called generic_export
Called handle_xlsx
Done handle_xlsx in 5.629085063934326 seconds
Done generic_export in 6.414600849151611 seconds
Done export_users in 20.74511480331421 seconds
```

# CPython with SQLAlchemy Core

```
Called export_users
Called get_data
Done get_data in 0.4149630069732666 seconds
Called get_addresses_per_user_id
Done get_addresses_per_user_id in 3.2696430683135986 seconds
Called generic_export
Done generic_export in 3.8310599327087402 seconds
Done export_users in 7.783042907714844 seconds
```

# Pypy with SQLAlchemy Core

```
Called export_users
Called get_data
Done get_data in 0.5241069793701172 seconds
Called get_addresses_per_user_id
Done get_addresses_per_user_id in 2.9715161323547363 seconds
Called generic_export
Done generic_export in 1.5337448120117188 seconds
Done export_users in 5.178534984588623 seconds
```
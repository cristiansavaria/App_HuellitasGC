# Huellitas GC

This project is a Django application. When running in production, make sure to define the following environment variable:

- `DJANGO_SECRET_KEY`: secret key used by Django for cryptographic signing.
  If the variable is not set and `DEBUG` is `False`, the application will raise
  a `RuntimeError` during startup. When `DEBUG` is `True`, a default unsafe
  value is used.


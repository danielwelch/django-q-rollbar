### Note
This is a proposed [Django Q](https://github.com/Koed00/django-q/) plugin intended to serve as an accompaniment to the changes in Django Q proposed in [this fork](https://github.com/danielwelch/django-q/tree/error-reporter). This package does nothing until those changes are incorporated.

# django-q-rollbar
A [Django Q](https://github.com/Koed00/django-q/) Error Reporter plugin adding [Rollbar](https://rollbar.com/) support.

### Installation
This plugin is intended to be included with Django Q as [setuptools extra](https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies).

`$ pip install django-q[rollbar]`

Or add `django-q[rollbar]` to `requirements.txt`.

### Usage
Configure Rollbar via the Django Q `Q_CLUSTER` dictionary in your Django project's `settings.py`. It is important that the `rollbar` key be set in the `error_reporter` dictionary, as this name aligns with the project's entry point for this plugin.
```python
Q_CLUSTER = {
    'error_reporter': {
        'rollbar': {
            'access_token': '32we33a92a5224jiww8982',
            'environment': 'Django-Q'
        }
    }
}
```
Please check the [Pyrollbar configuration reference](https://rollbar.com/docs/notifier/pyrollbar/) for more options. Additional options defined in `Q_CLUSTER` are passed directly as kwargs to Pyrollbar's `rollbar.init`.

Of course, you will need a Rollbar account and access token to use this plugin.

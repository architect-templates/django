<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cdn.architect.io/logo/horizontal-inverted.png">
    <source media="(prefers-color-scheme: light)" srcset="https://cdn.architect.io/logo/horizontal.png">
    <img width="320" alt="Architect Logo" src="https://cdn.architect.io/logo/horizontal.png">
  </picture>
</p>

<p align="center">
  A dynamic microservices framework for building, connecting, and deploying cloud-native applications.
</p>

---

# Running Django on Architect

This example will show you the use-case for using Python on Architect leveraging the Django tutorial application – [Polls](//docs.djangoproject.com/en/4.0/intro/tutorial01/). In this example, we've written a component spec (the `architect.yml` file) that defines a component to run a Python based web application.

[Learn more about the architect.yml file](//docs.architect.io/components/architect-yml/)

## Running locally

Architect component specs are declarative, so it can be run locally or remotely with a single deploy command:

```sh
# Clone the repository and navigate to this directory
$ git clone https://github.com/architect-templates/django.git
$ cd ./django

# Register the component to the local registry
$ architect link .

# Deploy using the dev command
$ architect dev .
```

Once the deploy has completed, you can reach your new service by going to http://app.arc.localhost/.

Default values of `admin` and `password` have been set for the `/admin` page. To access or change the default admin user credentials, modify the parameters on the top of the `architect.yml` file.

```yaml
parameters:
  django_admin_email:
    default: noreply@architect.io
  django_admin_username:
    default: admin
  django_admin_password:
    default: password
```

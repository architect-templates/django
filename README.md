<p align="center">
  <a href="//architect.io" target="blank"><img src="https://docs.architect.io/img/logo.svg" width="320" alt="Architect Logo" /></a>
</p>

<p align="center">
  A dynamic microservices framework for building, connecting, and deploying cloud-native applications.
</p>

---

# Running Django on Architect

This example will show you the use-case for using Python and Django on Architect leveraging the Django tutorial application – [Polls](//docs.djangoproject.com/en/4.0/intro/tutorial01/).

In this example, we've written a component spec (the `architect.yml` file) that defines a component to run a Python based web application.

[Learn more about the architect.yml file](//docs.architect.io/configuration)

## Running locally

Architect component specs are declarative, so it can be run locally or remotely with a single deploy command:

```sh
# Clone the repository and navigate to this directory
$ git clone https://github.com/architect-team/architect-cli.git
$ cd ./architect-cli/examples/django

# Register the component to the local registry
$ architect link .

# Deploy using the dev command
$ architect dev examples/django -e local
```

Once the deploy has completed, you can reach your new service by going to http://web.arc.localhost/.

Default values of `username` and `password` have been set to use on the `/admin` page. To access or change the default admin user credentials, modify the parameters on the top of the `architect.yml` file.

```yaml
parameters:
  django_admin_email:
    default: noreply@architect.io
  django_admin_username:
    default: username
  django_admin_password:
    default: password
```

## Deploying to the cloud

Want to try deploying this to a cloud environment? Architect's got you covered there too! Just click the button below to deploy it to a sample Kubernetes cluster powered by Architect Cloud:

[![Deploy Button](https://docs.architect.io/deploy-button.svg)](https://cloud.architect.io/examples/components/django/deploy?tag=latest&interface=http%3Ahttp)

Alternatively, if you're already familiar with Architect and have your own environment registered, you can use the command below instead:

```sh
$ architect deploy examples/django:latest -a <account-name> -e <environment-name> -i http:http
```

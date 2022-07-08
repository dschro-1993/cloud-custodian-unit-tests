# cc-test

Cloud Custodian docs ==> [here](https://cloudcustodian.io/docs/index.html)

Thanks to [Zendesk](https://zendesk.engineering/validating-cloud-custodian-on-aws-with-moto-203a30ee5505) for this brilliant idea.

## Prerequisites

- python 3.9
- pipenv

## Setup

```
pipenv install
pipenv shell
custodian --help
```

## Tests

```
pytest tests/
```

...

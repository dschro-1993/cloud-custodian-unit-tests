# c7n-unit-tests

Cloud Custodian docs ==> [here](https://cloudcustodian.io/docs/index.html)

Thanks to Zendesk for this brilliant [idea](https://zendesk.engineering/validating-cloud-custodian-on-aws-with-moto-203a30ee5505) how to unit-test c7n policies.

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

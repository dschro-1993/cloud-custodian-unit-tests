import os
import unittest
from unittest.mock import patch, PropertyMock

class CustodianPolicyTest(unittest.TestCase):
    @staticmethod
    def extract_output(call_args_list: any):
        elements = []
        metadata = []
        for i, element in enumerate(call_args_list):
            if i % 2 == 0:
                elements.extend(element[0][0])
            else:
                metadata.append(element[0][0])
        return (elements, metadata)

    def execute_policy(self, policy_name: str, dumps: any):
        from c7n.commands import run
        from c7n.config   import Config

        policy_path = os.getcwd() + "/policies/" + policy_name

        args   = {"output_dir": ".output", "configs": [policy_path], "vars": None}
        config = Config.empty(**args)

        # https://cloudcustodian.io/docs/aws/aws-modes.html
        # modify input to "pull" so that also cloudtrail- and cloudwatch-based functions can be executed/tested locally
        with patch("c7n.policy.Policy.execution_mode", new_callable=PropertyMock) as em:
            em.return_value = "pull"
            run(config)

        return self.extract_output(dumps.call_args_list)

        # ...

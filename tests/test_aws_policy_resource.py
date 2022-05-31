import itertools
import os
from unittest import TestCase
from json import loads
from app.utils.logger_util import logger
from app.constant.constant import Constant


class TestAWSEC2SecurityRulePolicy(TestCase):

    def setUp(self):
        self.test_passed = False
        logger.debug("Getting security group configuration file")
        fp = open(os.getcwd() + "/tests/data/test_aws_security_group_policy.json", "r")
        content = fp.read()
        fp.close()
        self.resources = loads(content)

    def tearDown(self):
        if not self.test_passed:
            logger.debug("Test case failed, kindly check security configuration and run remediation script to update "
                         "configuration")
            logger.error("Find the eks cluster details below to perform analysis")
            logger.debug(self.ports_dict)
        else:
            logger.debug("Test Cases passed successfully.")

    def test_security_group_correct_port_assigned(self):
        """
        Check if Security Group Policy Rule is assigned with port 443  or not.
        """
        self.ports_dict = dict()
        for sg_groups in self.resources:
            for sg in sg_groups:
                from_port = sg['IpPermissions'][0].get('FromPort')
                to_port = sg['IpPermissions'][0].get('ToPort')
                self.ports_dict[sg["GroupName"]] = [from_port, to_port]

        port_values = [port for port in self.ports_dict.values()]
        ports = list(itertools.chain(*port_values))
        checks = [port == Constant.PORT.value for port in ports]
        self.test_passed = all(checks)

        self.assertEqual(True, self.test_passed, msg="Ports is not configured correctly")

import json, os
from app.discovery.aws_discovery import AWSDiscovery
from app.discovery.aws_network import Network
from app.utils.logger_util import logger


class EKSClusterClient:
    def __init__(self):
        self.eks_client = AWSDiscovery()

    def get_eks_metadata(self):
        try:
            cluster_resource = self.eks_client.get_clusters()

            # Implementing multiple cluster support
            vpc_ids = [cluster["vpcId"] for cluster in cluster_resource]
            security_group_rules = []
            for vpc_id in vpc_ids:
                aws_network = Network({'id': vpc_id})
                rules = aws_network.get_security_group()
                security_group_rules.append(rules)

            json_obj = json.dumps(security_group_rules, indent=2)
            with open(os.getcwd() + "/tests/data/test_aws_security_group_policy.json", "w") as file:
                file.write(json_obj)
            logger.debug("Execution Completed Successfully.")

        except Exception as e:
            logger.error("Error while performing action %s. Error: %s" % (str(e)))



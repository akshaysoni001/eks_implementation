from app.discovery.connection import AWS



class Network(AWS):
    def __init__(self,
                 resource: dict,
                 **kwargs,
                 ) -> None:
        """
        """
        try:
            super(Network, self).__init__()
            self.conn = self.client("ec2")
            self.network = resource

        except Exception as ex:
            raise Exception(ex)

    def get_resource_inventory(self):
        """
        Fetches instance details.
        Args:
        instance_id (str): Ec2 instance id.
        return: dictionary object.
        """
        subnets = self.get_subnet()
        network_acl = self.get_network_acl()

        self.network = {
            **self.network,
            "subnets": subnets,
            "network_acl": network_acl,
            "security_group": self.get_security_group(),
            "flow_logs": self.get_flow_logs()
        }
        return self.network

    def get_subnet(self):
        def fetch_subnet(subnetwork_list=None, continueToken: str = None):
            request = {
                "Filters": [
                    {
                        "Name": "vpc-id",
                        "Values": [self.network['id']]
                    }
                ]
            }
            if continueToken:
                request['NextToken'] = continueToken
            response = self.conn.describe_subnets(**request)
            continueToken = response.get('NextToken', None)
            current_subnets = [] if not subnetwork_list else subnetwork_list
            current_subnets.extend(response.get('Subnets', []))

            return current_subnets, continueToken

        try:
            subnets, nextToken = fetch_subnet()

            while nextToken:
                subnets, nextToken = fetch_subnet(subnets, nextToken)
        except Exception as ex:
            print("subnet fetch error: ", ex)
            return []

        return subnets

    def get_network_acl(self):
        def fetch_network_acl(acl_list=None, continueToken: str = None):
            request = {
                "Filters": [
                    {
                        "Name": "vpc-id",
                        "Values": [self.network['id']]
                    }
                ]
            }
            if continueToken:
                request['NextToken'] = continueToken
            response = self.conn.describe_network_acls(**request)
            continueToken = response.get('NextToken', None)
            current_acls = [] if not acl_list else acl_list
            current_acls.extend(response.get('NetworkAcls', []))

            return current_acls, continueToken

        try:
            acls, nextToken = fetch_network_acl()

            while nextToken:
                acls, nextToken = fetch_network_acl(acls, nextToken)
        except Exception as ex:
            print("network acl fetch error: ", ex)
            return []

        return acls

    def get_security_group(self):
        def fetch_security_group(sg_list=None, continueToken: str = None):
            request = {
                "Filters": [
                    {
                        "Name": "vpc-id",
                        "Values": [self.network['id']]
                    }
                ]
            }
            if continueToken:
                request['NextToken'] = continueToken
            response = self.conn.describe_security_groups(**request)
            continueToken = response.get('NextToken', None)
            current_sg = [] if not sg_list else sg_list
            current_sg.extend(response.get('SecurityGroups', []))

            return current_sg, continueToken

        try:
            sg_data, nextToken = fetch_security_group()

            while nextToken:
                sg_data, nextToken = fetch_security_group(sg_data, nextToken)
        except Exception as ex:
            print("network SG fetch error: ", ex)
            return []

        return sg_data

    def get_flow_logs(self):
        def fetch_flow_logs(flow_log_list=None, continueToken: str = None):
            request = {
                "Filters": [
                    {
                        "Name": "resource-id",
                        "Values": [self.network['id']]
                    }
                ]
            }
            if continueToken:
                request['NextToken'] = continueToken
            response = self.conn.describe_flow_logs(**request)
            continueToken = response.get('NextToken', None)
            current_flow_logs = [] if not flow_log_list else flow_log_list
            current_flow_logs.extend(response.get('FlowLogs', []))

            return current_flow_logs, continueToken

        try:
            flow_logs, nextToken = fetch_flow_logs()

            while nextToken:
                flow_logs, nextToken = fetch_flow_logs(flow_logs, nextToken)
        except Exception as ex:
            print("network Flow log fetch error: ", ex)
            return []

        return flow_logs

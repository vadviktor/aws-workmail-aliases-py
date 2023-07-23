from typing import List

import boto3


def get_workmail_domains() -> List[str]:
    client = boto3.client("route53domains", region_name="us-east-1")
    response = client.list_domains()
    return [domain["DomainName"] for domain in response["Domains"]]


def get_workmail_aliases() -> List[str]:
    client = boto3.client("workmail")
    response = client.list_aliases(
        OrganizationId="m-397baa3e7ba44fb0accc969bbd428fb7",
        EntityId="a7ee5e92-d25a-4781-8961-051004d405af",
    )
    return response["Aliases"]

from typing import List, Dict
from os import environ

import boto3



def get_workmail_domains() -> List[str]:
    client = boto3.client("route53domains", region_name=environ.get("AWS_REGION_GLOBAL"))
    response = client.list_domains()
    return [domain["DomainName"] for domain in response["Domains"]]


def get_workmail_aliases() -> List[str]:
    client = boto3.client("workmail")
    response = client.list_aliases(
        OrganizationId=environ.get("AWS_ORG_ID"),
        EntityId=environ.get("AWS_USER_ID"),
    )
    return response["Aliases"]


def delete_workmail_alias(alias: str) -> Dict[str, str]:
    client = boto3.client("workmail")
    response = client.delete_alias(
        OrganizationId=environ.get("AWS_ORG_ID"),
        EntityId=environ.get("AWS_USER_ID"),
        Alias=alias,
    )

    return response


def create_workmail_alias(alias: str) -> Dict[str, str]:
    client = boto3.client("workmail")
    response = client.create_alias(
        OrganizationId=environ.get("AWS_ORG_ID"),
        EntityId=environ.get("AWS_USER_ID"),
        Alias=alias,
    )

    return response

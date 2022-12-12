import pytest
from code.iam import cdfIamPolicy, cdfIamPolicyParse, cdfIamStatement
from aws_cdk import aws_iam as iam
from pydantic import ValidationError

def test_cdfIamStatement():
    statement = cdfIamStatement(Action="s3:*", Resource="arn:aws:s3:::my_bucket", Effect="Allow")
    policy_statement = statement.getPolicyStatement()
    assert policy_statement.resources == ["arn:aws:s3:::my_bucket"]
    assert policy_statement.actions == ["s3:*"]
    assert policy_statement.effect == iam.Effect.ALLOW

    statement = cdfIamStatement(Action="s3:*", Resource="arn:aws:s3:::my_bucket", Effect="Deny")
    policy_statement = statement.getPolicyStatement()
    assert policy_statement.resources == ["arn:aws:s3:::my_bucket"]
    assert policy_statement.actions == ["s3:*"]
    assert policy_statement.effect == iam.Effect.DENY


def test_getPolicyStatement():
    # Create a cdfIamStatement object with specific values
    statement = cdfIamStatement(
        Action="s3:ListBucket",
        Resource="arn:aws:s3:::my-bucket",
        Effect="Allow"
    )

    # Call the getPolicyStatement method
    policy_statement = statement.getPolicyStatement()

    # Assert that the returned iam.PolicyStatement has the expected values
    assert policy_statement.resources == ["arn:aws:s3:::my-bucket"]
    assert policy_statement.actions == ["s3:ListBucket"]
    assert policy_statement.effect == iam.Effect.ALLOW


def test_cdfIamPolicyParse():
    # Create a cdfIamPolicy object with specific values
    policy = cdfIamPolicy(
        Statement=[
            cdfIamStatement(
                Action="s3:ListBucket",
                Resource="arn:aws:s3:::my-bucket",
                Effect="Allow"
            ),
            cdfIamStatement(
                Action="s3:GetObject",
                Resource="arn:aws:s3:::my-bucket/*",
                Effect="Deny"
            )
        ]
    )

    # Create a JSON configuration that matches the values of the cdfIamPolicy object
    json_config = {
        "Statement": [
            {
                "Action": "s3:ListBucket",
                "Resource": "arn:aws:s3:::my-bucket",
                "Effect": "Allow"
            },
            {
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::my-bucket/*",
                "Effect": "Deny"
            }
        ]
    }

    # Call the cdfIamPolicyParse function with the JSON configuration
    parsed_policy = cdfIamPolicyParse(json_config)

    # Assert that the returned cdfIamPolicy has the same values as the original cdfIamPolicy
    assert parsed_policy == policy

def test_cdfIamPolicy_init():
    # Create a cdfIamPolicy object with specific values
    policy = cdfIamPolicy(
        Statement=[
            cdfIamStatement(
                Action="s3:ListBucket",
                Resource="arn:aws:s3:::my-bucket",
                Effect="Allow"
            ),
            cdfIamStatement(
                Action="s3:GetObject",
                Resource="arn:aws:s3:::my-bucket/*",
                Effect="Deny"
            )
        ]
    )

    # Assert that the Statement property of the cdfIamPolicy object has the expected values
    assert len(policy.Statement) == 2
    assert policy.Statement[0].Action == "s3:ListBucket"
    assert policy.Statement[0].Resource == "arn:aws:s3:::my-bucket"
    assert policy.Statement[0].Effect == "Allow"
    assert policy.Statement[1].Action == "s3:GetObject"
    assert policy.Statement[1].Resource == "arn:aws:s3:::my-bucket/*"
    assert policy.Statement[1].Effect == "Deny"

from pydantic import BaseModel
from typing import List, Union, Literal
from aws_cdk import aws_iam as iam

class cdfIamStatement(BaseModel):
    Action: str
    Resource: str
    Effect: Union[Literal["Allow"], Literal["Deny"]]

    def getPolicyStatement(self) -> iam.PolicyStatement:
        # effect: iam.Effect = iam.Effect.ALLOW if state
        effect: iam.Effect = iam.Effect.ALLOW if self.Effect == "Allow" else iam.Effect.DENY

        return iam.PolicyStatement(
            resources=[self.Resource],
            actions=[self.Action],
            effect=effect
        )
class cdfIamPolicy(BaseModel):
    Statement: List[cdfIamStatement]

def cdfIamPolicyParse(json_config: dict) -> cdfIamPolicy:
    policy: cdfIamPolicy = cdfIamPolicy.parse_obj(json_config)
    return policy
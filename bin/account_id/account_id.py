import boto3
import argparse

def get_accounts(env_name):
    
    next_token = None
    while True:
        if next_token != None:
            r = org_client.list_accounts(
                NextToken=next_token
            )
        else:
            r = org_client.list_accounts()

        for a in r["Accounts"]:

            if a["Name"] == env_name:
                return a["Id"]

        if "NextToken" in r:
            next_token = r["NextToken"]
        else:
            break
           
if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--aws_profile', help='name of aws profile',default="default")
    parser.add_argument('--aws_region', help='name of the aws region',default="eu-west-1")
    parser.add_argument('--env_name', help='aws account name')

    args=parser.parse_args()

    session = boto3.Session(profile_name=args.aws_profile,region_name=args.aws_region)
    org_client = session.client("organizations")

    print(get_accounts(env_name=args.env_name))

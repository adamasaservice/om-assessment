def create_or_modify_ec2(instance_id, git_commit_hash, region="us-east-1"):
   
    ec2 = boto3.client("ec2", region_name=region)

    try:
       
        ec2.create_tags(
            Resources=[instance_id],
            Tags=[{"Key": "gitcommithash", "Value": git_commit_hash}]
        )
        print(f"✅ Updated 'gitcommithash' tag to: {git_commit_hash}")

    except ec2.exceptions.ClientError as e:
        if "InvalidInstanceID.NotFound" in str(e):
            
            response = ec2.run_instances(
                ImageId="ami-0c55b159cbfafe1f0",  # Amazon Linux 2 (us-east-1)
                InstanceType="t2.micro",
                MinCount=1,
                MaxCount=1,
                TagSpecifications=[{
                    "ResourceType": "instance",
                    "Tags": [
                        {"Key": "Name", "Value": "Git-Tagged-Instance"},
                        {"Key": "gitcommithash", "Value": git_commit_hash},
                        {"Key": "ManagedBy", "Value": "create_or_modify_script"}
                    ]
                }]
            )
            new_id = response["Instances"][0]["InstanceId"]
            print(f"✅ Created new instance {new_id} with gitcommithash={git_commit_hash}")
        else:
            raise

   
    tags = ec2.describe_tags(
        Filters=[{"Name": "resource-id", "Values": [instance_id]}]
    )["Tags"]
    print("\n📋 Current Tags:")
    for tag in tags:
        print(f"  {tag['Key']}: {tag['Value']}")

if _name_ == "_main_":
    parser = argparse.ArgumentParser(description="Manage EC2 instance tags")
    parser.add_argument("--instance-id", required=True, help="EC2 instance ID")
    parser.add_argument("--commit-hash", required=True, help="Git commit hash value")
    parser.add_argument("--region", default="us-east-1", help="AWS region")
    args = parser.parse_args()

    create_or_modify_ec2(args.instance_id, args.commit_hash, args.region)


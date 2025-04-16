# ADD CODE HERE
# change script to whatever language you are comfortable with
# main.tf
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "backstage" {
  ami           = "ami-0c55b159cbfafe1f0" # Amazon Linux 2
  instance_type = "t2.micro"
  
  tags = {
    Name        = "backstage"
    Environment = "production"
    Owner       = "devops-team"
    
  }
}

resource "aws_ec2_tag" "backstage_gitcommithash" {
  resource_id = aws_instance.backstage.id
  key         = "gitcommithash"
  value       = var.git_commit_hash
}


# variables.tf
variable "git_commit_hash" {
  description = "The git commit hash to tag the instance with"
  type        = string
  default     = "initial" # Default value, override when applying
}

# outputs.tf
output "instance_id" {
  value = aws_instance.backstage.id
}

output "public_dns" {
  value = aws_instance.backstage.public_dns
}

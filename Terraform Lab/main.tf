provider "aws" {
    region = "us-east-1"
}

resource "aws_s3_bucket" "my_bucket" {
    bucket = "arav-terraform-lab-bucket-12345"
    
    tags = {
        Name = "TerraformLabBucket"
        Environment = "Development"
        Project = "TerraformLab"
    }
}

resource "aws_vpc" "myvpc" {
    cidr_block = "10.0.0.0/16"
    tags = {
        Name = "myvpc"
    }
}

resource "aws_subnet" "mysubnet1" {
    vpc_id = aws_vpc.myvpc.id
    cidr_block = "10.0.1.0/24"
    tags = {
        Name = "mysubnet1"
    }
}
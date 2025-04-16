# Add steps/actions here:

1. If we use count Terraform understands that to mean that all of resource instances are equivalent

2. Use the for_each argument and specify a meaningful name for each of the instances, which then means you can remove a particular key without affecting any others.

resource "example" "example" {
  for_each = toset(["db1", "db2", "db3", "db4", "db5"])

  # ...
}

After the above we can remove one without affecting ot changing the other resources

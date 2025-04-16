# Add steps/actions here:

1. count is for situations where all of the instances are equivalent - so it will affect the other instance when you delete one

2. will need to switch to using for_each so that there will be a way to describe to Terraform exactly which of the instances should be deleted, using its key.

3. complete the step to move to for_each first, and then you can separately destroy the instance.

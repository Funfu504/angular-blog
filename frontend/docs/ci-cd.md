CI/CD setup.

# Overview

My current CI/CD setup is to deploy to the development environment in AWS any "feature/*" branch or main branch push.  The AWS credentials are stored as secrets associated to the DEV environment.

# Lessons Learned:

1) In the YAML file, Configure-aws-credentials@v4 expects for aws-region to be an environment variable, not a secret!  Very poorly documented...

2) When dealing with S3 Buckets, the bucket name is required...not the ARN ID.  This is probably the same for most AWS interactions when not dealing with CloudFormations type work...keep that in mind for future efforts.

3) The package-lock.json file needs to be checked into the solution.  This is probably the same for other -lock files as well...keep that in mind for future efforts.

4) When syncing deploy files with AWS, ensure that you grant get,put,delete object permissions to the bucket contents, example, ::bucketname::/*  

Debugging CI/CD can consume ur credits quickly.  Verify these things above before kicking off the build to save yourself some headaches.

# TODOs

1) Update the YAML file to configure pushes to MAIN to deploy to the production AWS environment.
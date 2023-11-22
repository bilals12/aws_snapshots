# aws snapshots

## summary
some python scripts here to make capturing aws snapshots a little easier. using aws sso for authentication and boto3 for the aws stuff.

###the scripts:
1. **aws_sso.py**
- set up your aws session. uses sso, so no creds are hardcoded inside the script.
- run it and a browser window will open for the sso login. follow the prompts to login.

2. **aws_test.py**
- quick test script. lists running ec2 instances from your aws account.
- good for checking if your sso session setup is working correctly.

3. **aws_snapshot.py**
- the main function. creates snapshots of all your running ec2 instances (will add feature to list dead ones too, in the future)
- accepts cli args so you can specify region and instance state. 
- `python aws_snapshot.py --region us-west-1 --state running`

###use:
1. **prereqs**
- python and boto3
- clone the repo to your local

2. **running**
- start with `aws_sso.py` to get your session going.
- `aws_test.py` is next, just so you can make sure everything is working.
- then run `aws_snapshot.py` with your desired args.

3. **tips**
- make sure aws cli is set up right and you have the necessary perms inside aws.
- the scripts themselves are simple and straightforward but feel free to tweak them for your setup.
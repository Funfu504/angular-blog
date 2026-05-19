# build-lambda.ps1
param (
    [string]$LambdaName = "lambda_read_posts"
)

# Paths
$BackendDir = "$PSScriptRoot\backend"
$ApiDir     = "$BackendDir\api"
$CoreDir    = "$BackendDir\core"
$ServiceDir = "$BackendDir\src"
$BuildDir   = "$BackendDir\build\$LambdaName"


# 1️⃣ Clean previous build
if (Test-Path $BuildDir) {
    Remove-Item $BuildDir -Recurse -Force
}
New-Item -ItemType Directory -Path $BuildDir | Out-Null

# 2️⃣ Copy Lambda handler and shared code
Copy-Item "$ApiDir\$LambdaName.py" $BuildDir\
Copy-Item "$ServiceDir\*" $BuildDir\ -Recurse
Copy-Item "$CoreDir" $BuildDir\ -Recurse

# 3️⃣ Install dependencies (linux versions) locally into build folder.  leverage Docker, AWS Linux image python3.13 installed.
docker run --rm `
  -v "${PWD}:/var/task" `
  -w /var/task `
  public.ecr.aws/sam/build-python3.13 `
  pip install -r /var/task/backend/requirements-lambda.txt -t /var/task/backend/build/$LambdaName

# 4️⃣ Create zip
$ZipFile = "$BackendDir\build\$LambdaName.zip"
if (Test-Path $ZipFile) {
    Remove-Item $ZipFile -Force
}
cd $BuildDir
Compress-Archive -Path * -DestinationPath $ZipFile
cd $BackendDir

Write-Host "✅ Lambda package created: $ZipFile"
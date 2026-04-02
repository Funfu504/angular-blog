# build-lambda.ps1
param (
    [string]$LambdaName = "lambda_read_posts"
)

# Paths
$BackendDir = "$PSScriptRoot\backend"
$ApiDir     = "$BackendDir\api"
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

# 3️⃣ Install dependencies locally into build folder
pip install -r "$BackendDir\requirements-lambda.txt" -t $BuildDir

# 4️⃣ Create zip
$ZipFile = "$BackendDir\build\$LambdaName.zip"
if (Test-Path $ZipFile) {
    Remove-Item $ZipFile -Force
}
cd $BuildDir
Compress-Archive -Path * -DestinationPath $ZipFile
cd $BackendDir

Write-Host "✅ Lambda package created: $ZipFile"
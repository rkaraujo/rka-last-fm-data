# Set variables
$pyFileName = "last-fm-analyze-main.py"
$pyTargetDir = "spark-apps"
$containerPyPath = "/opt/spark-apps/$pyFileName"

if (-Not (Test-Path $pyFileName)) {
    Write-Host "Python file not found: $pyFileName" -ForegroundColor Red
    exit 1
}

Write-Host "Copying Python file to $pyTargetDir..."
New-Item -ItemType Directory -Force -Path $pyTargetDir | Out-Null
Copy-Item -Force $pyFileName "$pyTargetDir/"

Write-Host "Submitting Spark Python job to Docker cluster..."

docker exec -it spark-master spark-submit `
    --conf spark.jars.ivy=/.ivy2 `
    --master spark://spark-master:7077 `
    $containerPyPath

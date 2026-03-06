$RG="monitor-dashboard-rg"
$LOCATION="uksouth"
$APPNAME="log-dashboard-app"
$BICEP_FILE="../bicep/main.bicep"

Write-Host "Step 1: Checking Azure login..."
az account show > $null 2>&1
if ($LASTEXITCODE -ne 0) {
    az login
}

# Check if the resource group already exists
Write-Host "Step 2: Creating resource group..."
az group create `
    --name $RG `
    --location $LOCATION

Write-Host "Step 3: Deploying infrastructure (Bicep)..."

az deployment group create `
    --resource-group $RG `
    --template-file $BICEP_FILE `
    --parameters appName=$APPNAME

Write-Host "Step 4: Deploying Flask app code..."

az webapp up `
    --name $APPNAME `
    --resource-group $RG `
    --runtime "PYTHON:3.11"

Write-Host "Deployment complete 🚀"
$RG="monitor-dashboard-rg"

Write-Host "Deleting environment..."

az group delete `
    --name $RG `
    --yes `
    --no-wait

Write-Host "Environment scheduled for deletion"
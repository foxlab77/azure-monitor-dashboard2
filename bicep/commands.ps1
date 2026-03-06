az deployment group create --resource-group rg-dashboard-lab2 --template-file bicep/main.bicep

az webapp deployment list-publishing-profiles --name log-dashboard-app --resource-group rg-dashboard-2

# Create a service principal with contributor role scoped to the resource group
az ad sp create-for-rbac --name github-dashboard-deployer --role contributor --scopes /subscriptions/50a9d9a5-9bab-4d7a-86f0-39a6ebb9e6b6/resourceGroups/rg-dashboard-2 --sdk-auth
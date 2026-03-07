import os
from datetime import timedelta
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient

workspace_id = os.environ.get("LOG_ANALYTICS_WORKSPACE_ID")

credential = DefaultAzureCredential()
client = LogsQueryClient(credential)


def get_log_volume():

    query = """
    CustomAppLogs_CL
    | summarize count() by bin(TimeGenerated, 5m)
    | order by TimeGenerated asc
    """

    result = client.query_workspace(
        workspace_id,
        query,
        timespan=timedelta(hours=1)
    )

    timestamps = []
    counts = []

    for row in result.tables[0].rows:
        timestamps.append(str(row[0]))
        counts.append(row[1])

    return timestamps, counts


def get_recent_logs():

    query = """
    CustomAppLogs_CL
    | project TimeGenerated, Message_s
    | order by TimeGenerated desc
    | take 20
    """

    result = client.query_workspace(
        workspace_id,
        query,
        timespan=timedelta(hours=1)
    )

    logs = []

    for row in result.tables[0].rows:
        logs.append({
            "time": str(row[0]),
            "message": row[1]
        })

    return logs
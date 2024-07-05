def analyze_campaigns(campaign_data):
    analysis = {}
    for campaign, data in campaign_data.items():
        cpc = data['Cost'] / data['Clicks'] if data['Clicks'] != 0 else float('inf')
        ctr = data['Clicks'] / data['Impressions'] if data['Impressions'] != 0 else 0
        cpa = data['Cost'] / data['Conversions'] if data['Conversions'] != 0 else float('inf')
        analysis[campaign] = {'CPC': cpc, 'CTR': ctr, 'CPA': cpa}
    return analysis




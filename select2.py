 SELECT count(*) FROM Transaction WHERE name LIKE '%getLoadv2/loadv2%' AND (appName LIKE '%nonprod-test%' OR appName LIKE '%dev') FACET tags.Customer, tags.Environment SINCE 30 MINUTES AGO TIMESERIES 20 SECONDS LIMIT MAX

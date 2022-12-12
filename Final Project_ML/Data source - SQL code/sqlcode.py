WITH query_settings AS (
  SELECT
    '20160801' AS start_date,
    '20171031' AS end_date), 

session_level AS (
SELECT 
visitNumber,
visitId,
totals.visits,
totals.hits,
totals.pageviews,
totals.timeOnSite,
totals.bounces,
totals.transactions,
totals.transactionRevenue,
totals.newVisits,
totals.screenviews,
totals.uniqueScreenviews,
totals.timeOnScreen,
totals.totalTransactionRevenue,
trafficSource.source,
trafficSource.medium,
device.browser,
device.operatingSystem,
device.isMobile,
device.deviceCategory,
geoNetwork.continent,
geoNetwork.country,
geoNetwork.city,
hits.hitNumber,
hits.time,
hits.hour,
hits.minute,
hits.page.searchKeyword,
hits.page.searchCategory,
hits.page.pagePath,
hits.page.hostname,
hits.page.pageTitle,
hits.transaction.transactionId,
hits.transaction.transactionRevenue,
hits.transaction.currencyCode,
hits.transaction.transactionCoupon,
hits.item.productName,
hits.item.productCategory,
hits.type,
fullVisitorId,
userId,
clientId
FROM `bigquery-public-data.google_analytics_sample.ga_sessions_*`, query_settings, unnest(hits) AS hits
WHERE _TABLE_SUFFIX BETWEEN start_date AND end_date)

SELECT *
FROM session_level AS sl
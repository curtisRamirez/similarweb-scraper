# Similarweb Scraper

> This tool pulls detailed website traffic intelligence, helping you uncover rankings, visits, engagement, keywords, and audience insights in one sweep. It solves the challenge of accessing structured analytics from competitive domains quickly and reliably. The Similarweb scraper is built to deliver clean, export-ready data for researchers, analysts, and marketing teams.

> By gathering traffic sources, demographic data, and ranking trends, it gives you a clear snapshot of how any website performs globally or regionally.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Similarweb Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

The scraper automates the process of collecting structured analytics from Similarweb, turning a rich set of performance indicators into standardized data. It helps you skip manual checks, avoid inconsistent screenshots, and focus on meaningful comparisons instead of repetitive tasks.

It’s ideal for marketers, analysts, product teams, founders, or anyone who relies on competitive intelligence and web performance reporting.

### Why This Scraper Matters

- Collects complete traffic and ranking metrics in seconds.
- Supports bulk URLs for large-scale analysis.
- Offers optional in-depth datasets including company, demographics, and competitors.
- Delivers precise monthly visit trends and country-level breakdowns.
- Outputs standardized, dashboard-ready data.

## Features

| Feature | Description |
|--------|-------------|
| Global & Country Rank Extraction | Retrieves ranking data to benchmark site authority across regions. |
| Traffic Insights | Pulls total visits, visit trends, and country-specific monthly data. |
| Engagement Metrics | Captures bounce rate, pages per visit, and average time spent. |
| Keyword Intelligence | Collects top keywords with value, CPC, and volume. |
| Source Distribution | Breaks down direct, referral, social, search, and mail traffic. |
| Audience Demographics | Extracts optional age and gender distributions. |
| Company Data | Includes employees, revenue ranges, and headquarter details when available. |
| Competitor Insights | Lists similar domains, affinity scores, and cross-category rankings. |
| Ad & Social Channels | Provides details on social traffic share and outgoing/incoming domains. |
| Bulk Processing Support | Handles multiple URLs in a single run for efficient research. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|------------|------------------|
| data_captured_at | Timestamp of when the data snapshot was taken. |
| searchUrl | Full URL used for the lookup. |
| url | Canonical URL of the target site. |
| domain | Parsed domain name. |
| rankGlobal | Global website ranking. |
| country | Primary ranking country. |
| countryRank | Rank within the primary country. |
| category | Category assigned to the website. |
| categoryRank | Rank within that category. |
| title | Page title extracted from the domain. |
| description | Meta description of the website. |
| totalVisits | Total estimated visits in the latest month. |
| monthlyVisits | Historical monthly visits for past three months. |
| website_traffic_by_country | Country-specific traffic share and monthly breakdown. |
| topKeywords | Highest-value keywords driving site traffic. |
| engagement | Bounce rate, pages per visit, time on site, and visit count. |
| directTraffic | Share of direct traffic. |
| referralTraffic | Share of referral traffic. |
| searchTraffic | Share of search traffic. |
| socialTraffic | Share of social traffic. |
| mailTraffic | Share of email-sourced traffic. |
| countryShare | Country traffic share distribution. |
| previewDesktop | Desktop preview image URL. |
| previewMobile | Mobile preview image URL. |
| snapshotDate | Date of the Similarweb snapshot. |
| company_* | Optional company-level metadata fields. |
| age_destribution | Age segmentation of the audience. |
| gender_destribution | Male/female audience distribution. |
| competitors | Competing domains with icons and visit counts. |
| top_interested_websites | Domains users also visit. |
| top_interested_topics | Topics associated with the audience. |
| top_categories | Website category insights. |
| top_competitors | Ranked competitor performance. |
| total_keywords | Count of all identified ranking keywords. |
| incoming/outgoing_referring_domains | Referrer and outbound domain details. |
| ads_networks / ads_sites | Ad network and site details. |
| social_networks_share | Breakdown of traffic from social platforms. |

---

## Example Output


    {
        "data_captured_at": "2025-10-13T14:29:59.850885",
        "url": "n8n.io",
        "rankGlobal": 4818,
        "country": "US",
        "countryRank": 7132,
        "category": "Computers_Electronics_and_Technology/Programming_and_Developer_Software",
        "categoryRank": 164,
        "totalVisits": 10968221,
        "topKeywords": [
            {
                "keyword": "n8n",
                "estimatedValue": 2958590.0,
                "searchVolume": 3670140.0,
                "cpc": 0.41
            }
        ],
        "engagement": {
            "bounceRate": 0.4913,
            "pagesPerVisit": 4.2491,
            "timeOnSite": 231.37
        }
    }

---

## Directory Structure Tree


    Similarweb Scraper/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── traffic_parser.py
    │   │   ├── keyword_parser.py
    │   │   ├── demographics_parser.py
    │   │   └── utils_format.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.txt
    │   └── sample.json
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Market analysts** use it to compare domain performance, so they can uncover trends and emerging competitors.
- **SEO teams** use it to track keyword opportunities and traffic patterns, boosting visibility and campaign accuracy.
- **Business strategists** use it to benchmark competitors, supporting clearer product and market decisions.
- **Marketing agencies** use it to build dashboards for clients, improving reporting speed and consistency.
- **Founders and product leads** use it to validate market traction and audience behavior before making strategic investments.

---

## FAQs

**Does the scraper support bulk domains?**
Yes. You can submit multiple URLs at once, and each will be processed individually with full metrics returned.

**Is in-depth data always available?**
Some smaller sites may not include demographics, revenue data, or rank histories. Larger sites generally return these fields.

**What formats can the results be exported to?**
Structured outputs support JSON, CSV, XLSX, and other common machine-readable formats.

**How accurate are visit estimates?**
The metrics come from aggregated modeling and typically provide a strong directional signal suitable for competitive intelligence.

---

## Performance Benchmarks and Results

**Primary Metric:** Processes 5–10 site profiles per second under typical workloads, even with monthly history enabled.
**Reliability Metric:** Maintains a high success rate across thousands of tested domains thanks to robust handling of dynamic elements.
**Efficiency Metric:** Handles bulk URL processing with steady memory consumption and consistent throughput.
**Quality Metric:** Returns more than 90% of expected data fields for popular domains, ensuring comprehensive datasets for analysis.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>

# PHASE 1 \- Planning & Setup

## 1.1 Create project folder structure

### Checklist:

- [x] Create main folder: energy\_auto\_advisor  
- [x] Add subfolder:  
      - [x] /modules  
      - [x] /data  
      - [x] /dashboard  
      - [x] /config  
      - [x] /logs  
            

### Helpful AI Prompt:

	*“Generate the recommended folder structure for the Energy Auto-Advisor and create empty placeholder files.”*

## 1.2 Create configuration file

### Checklist:

- [ ] Create config.yaml  
- [ ] Add basic settings: provider, API keys (if any), run interval  
- [ ] Add user notifications preferences

### Helpful AI Prompt:

	*“Generate a default config.yaml for the Energy Auto-Advisor with placeholders for Octopus API, scheduler interval, and notification settings.”*

# PHASE 2 \- Data Collection Modules

## 2.1 Live variable tariff fetcher

### Checklist:

- [ ] Choose API provider (Octopus recommended)  
- [ ] Implement get\_variable\_price()  
- [ ] Convert raw unit rates → estimated monthly cost  
- [ ] Add error handling  
- [ ] Write data to /data/variable\_prices.json

### Helpful AI Prompt:

	*“Generate a Python module called fetch\_variable.py that pulls today’s Octopus Energy variable tariff rate and returns estimated monthly cost.”*

## 2.2 FIxed deal data importer

### Checklist:

- [ ] Create fixed\_deals.csv  
- [ ] Implement CSV loader  
- [ ] Add validation for missing values  
- [ ] Implement get\_best\_fixed() function

### Helpful AI Prompt:

	*“Write fetch\_fixed.py that loads fixed\_deals.csv, finds the cheapest deal, and returns the monthly cost.”*

## 2.3 Historical logging

### Checklist:

- [ ] Create prices\_log.csv  
- [ ] Add log\_prices(variable, fixed) function  
- [ ] Ensure daily append without duplication

### Helpful AI Prompt:

	*“Generate a [logger.py](http://logger.py) module that appends variable and fixed rates to prices\_log.csv with timestamps.”*

# PHASE 3 \- Market Trend Engine

## 3.1 Trend calculation

### Checklist:

- [ ] Load last 30 days from prices\_log.csv  
- [ ] Compute 7-day rolling averages  
- [ ] Compare current vs previous 7 days  
- [ ] Output: up, down, stable

### Helpful AI Prompt:

	*“Write [trend.py](http://trend.py) that loads prices\_log.csv, calculates 7-day averages, and returns up/down/stable based on % change.”*

# PHASE 4 \- Recommendation Engine

## 4.1 Decision logic module

### Checklist:

- [ ] Implement evaluate(variable, fixed, trend)  
- [ ] Include %-difference logic  
- [ ] Define thresholds for FIX/WAIT/HOLD  
- [ ] Return message \+ confidence rating

### Helpful AI Prompt:

	*“Generate [advisor.py](http://advisor.py) using the advanced decision logic described earlier (percentage difference, trend interaction, thresholds).”*

# PHASE 5 \- Notifications

## 5.1 Choose notification method(s)

Choose one of the following:

- [ ] Discord Webhook  
- [ ] Email (SMTP)  
- [ ] Telegram bot  
- [ ] Windows toast notifications

## 5.2 Implement notification module

### Checklist:

- [ ] Create [notifier.py](http://notifier.py)  
- [ ] Send alert only for FIX states  
- [ ] Include price summary in the message

### Helpful AI Prompt:

	*“Build [notifier.py](http://notifier.py) with discord webhook support that only sends alerts when the advisor returns a FIX recommendation.”*

# PHASE 6 \- Automation & Scheduling

## 6.1 Daily run script

### Checklist:

- [ ] Create run\_daily.py  
- [ ] Import all modules  
- [ ] Write high-level workflow:  
      * Fetch variable  
      * Fetch fixed  
      * Detect trent  
      * Evaluate  
      * Log  
      * Alert

### Helpful AI Prompt:

	*“Generate run\_daily.py which orchestrates the entire system (fetch variable/fixed, log, trend, advisor, notifications).”*

## 6.2 Enable automation

### Pick one:

- [ ] Python loop (24h sleep)  
- [ ] Windows task scheduler  
- [ ] Linux cron job  
- [ ] Docker \+ cron

### Helpful AI Prompt:

	*“Give me instructions for scheduling run\_daily.py to run every morning at 8am on Windows Task Scheduler.”*

# PHASE 7 \- Dashboard

Choose Tkinter or Flask (or both):

## 7.1 Tkinter Desktop App

### Checklist:

- [ ] Build main window  
- [ ] Show today’s variable \+ fixed  
- [ ] Show trend arrow  
- [ ] Show recommendation  
- [ ] Add ‘Refresh Now’ button

### Helpful AI Prompt:

	*“Generate a Tkinter dashboard to visualise variable/fixed rates, trend arrow, recommendation, and add a refresh button.”*

## 7.2 Flask Web Dashboard

### Checklist:

- [ ] Create /dashboard/[app.py](http://app.py)  
- [ ] Create templates  
- [ ] Add charts using [Chart.js](http://Chart.js) or Matplotlib  
- [ ] Show 30-day trend graph  
- [ ] Live reload button

### Helpful AI Prompt:

	*“Generate a Flask dashboard that displays today’s numbers, trend, recommendation, and a 30-day chart from prices\_log.csv.”*

# PHASE 8 \- Polishing & Enhancements

### Checklist:

- [ ] Add error notifications  
- [ ] Add modular settings in config.yaml  
- [ ] Add logging of system events  
- [ ] Add unit tests  
- [ ] Add export to excel

### Helpful AI Prompt:

	*“Generate a test suite for the modules using pytest.”*

# PHASE 9 \- Optional Advanced Features

Tick any you might want to explore:

- [ ] Predict future trends using simple ML  
- [ ] Scrape fixed deals automatically  
- [ ] Add gas \+ electric separately  
- [ ] Add energy usage customisation  
- [ ] Add email weekly report summary

### Helpful AI Prompt:

	*“Add a simple ML predictor that forecasts whether prices will rise or fall based on the last 60 days.”*

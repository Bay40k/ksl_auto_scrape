# ksl_auto_scrape

* Uses ParseHub

This program will get the listing of cars from a KSL Autos listing, and email them to you.

You can schedule `startscrape.py` and `sendemail.py` to run repeatadely (i.e. daily), using cron jobs, or task scheduler (Windows).


## Setup:
1. Download ParseHub
1. Import `ksl.com_Project.phj`, into ParseHub
1. Configure and rename `config_EXAMPLE.py` to `config.py`
1. Scrape data by running `startscrape.py`
1. When data is done scraping, run `sendemail.py` to send the data to your email.

## Example cron job:

Runs scrape every 12 hours, runs sendemail every 12 hours:30 minutes (or 30 minutes after the scrape).

```bash
0 */12 * * * python ~/ksl_auto_scraper/startscrape.py

30 */12 * * * python ~/ksl_auto_scraper/sendemail.py
```

## TODO
* Add code comments
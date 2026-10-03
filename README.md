# Pakistan Toshakhana Files: gift analysis, 2002-2022

Exploratory analysis of the gifts recorded in Pakistan's Toshakhana, the government department that holds gifts given to officials by foreign dignitaries. A recipient can keep a gift by paying a share of its assessed value (the *retention cost*).

The data has 4,198 gift records, from 8 January 2002 to 24 October 2022.

- Notebook: [`toshakhana_gift_analysis.ipynb`](toshakhana_gift_analysis.ipynb), with the cleaning, stats and charts
- PDF summary: [`toshakhana_report.pdf`](toshakhana_report.pdf), a 5-page report of the main tables and charts
- Data source: [Kaggle: zusmani/pakistan-toshakhana-files](https://www.kaggle.com/datasets/zusmani/pakistan-toshakhana-files)

All amounts are nominal Pakistani rupees (PKR), not adjusted for inflation.

## Headline numbers

| Metric | Value |
|---|---|
| Gift records | 4,198 |
| Total assessed value | PKR 1,352.6 million |
| Total paid by recipients to retain gifts | PKR 204.0 million (15.1% of assessed) |
| Records retained by the recipient | 3,726 (88.8%) |
| Retained at zero cost | 2,367 (63.5% of retained), worth PKR 37.6 million |
| Median assessed value | PKR 8,000 |
| Mean assessed value | PKR 322,272 |
| Gifts assessed at PKR 1 million or more | 129 |

## Records and extremes

### Highest

- Most valuable gift: a Rolex wrist watch assessed at PKR 140 million, recorded for PM Shehbaz Sharif on 12 May 2022. It was not retained and is listed as displayed at the Prime Minister House.
- Most valuable gift that was retained: a set of security vehicles (BMW 760 Li, Toyota Lexus LX 470 and others) assessed at PKR 107.8 million, recorded for President Asif Ali Zardari on 26 January 2009. PKR 16.2 million (15%) was paid.
- Highest amount paid to retain a gift: PKR 20.18 million, by PM Imran Khan for a Graff watch set assessed at PKR 100.9 million (24 September 2018).
- Most valuable gift retained for free: an 18-carat gold and diamond jewellery set assessed at PKR 14.9 million, recorded for the wife of President Pervez Musharraf on 3 April 2007.
- Highest-value year: 2017, with PKR 314.6 million from only 113 records.
- Highest-value household: Shahid Khaqan Abbasi, PKR 233 million across 32 records, of which PKR 123 million was recorded against family members. That averages PKR 7.3 million per record.
- Largest auctioned item: a jewellery set assessed at PKR 10.3 million, recorded for Sartaj Aziz in January 2016.

### Lowest

- Lowest non-zero assessments: PKR 50 each, for two scarves (Shaukat Aziz, 2004) and a ladies' dupatta (Jahangir Khan Tareen, 2005, auctioned). A paper hand fan was assessed at PKR 75.
- Lowest-value year: 2010, with PKR 1.8 million from 136 records.
- Fewest records in a year: 2013 (65).
- 589 records (14%) have an assessed value of zero.
- Lowest retention rate among the large groups: PTI-labelled records at 67.8% retained, against 97.2% for PPP and 94.2% for the Musharraf-era government.

### Most

- Most gift records for one person: Shaukat Aziz with 849 (one in five of all records). They total only PKR 31.2 million, a median of PKR 3,000 each.
- Most common gift: a carpet. "One carpet" is the entire description 91 times, and 250 records are carpets.
- Most common category: watches, with 1,163 records. That is 28% of records and 67% of all value (PKR 905 million).
- Most common watch brand: Rolex, with 130 records worth PKR 371 million, or 41% of all watch value.
- Busiest year: 2005 (470 records).
- Busiest single dates: 22 July 2010 (46 records) and 11 May 2010 (45), almost all recorded for President Zardari.
- Busiest weekday and month: Tuesday (966 records) and March (450). Sunday has only 64.

### Concentration

- The top 10 gifts hold 49% of all assessed value and the top 100 hold 83%.
- The 22 gifts assessed above PKR 10 million (0.5% of records) hold 63% of the value.
- 57% of records are assessed at PKR 10,000 or less. Together they hold under 1% of the value.
- Watches, jewellery and vehicles make up 96% of the value.

### Paying to keep gifts

- 63.5% of retained gifts were kept for free, but they are mostly cheap items worth only 2.8% of total assessed value between them.
- Paid retentions cluster around 15% and 20% of assessed value.
- The share of retained gifts kept for free was highest in 2002 (81.7%) and lowest in 2017 (20.2%).
- Of the main affiliations, PTI-labelled records have the highest paid share (27.1% of assessed value) and the Musharraf-era government the lowest (9.6%).
- 174 records are gifts to spouses and children of office holders, worth PKR 251 million (19% of all value).

### Unusual entries

- A tractor, a motorcycle, and a buffalo with its calf (Chief Minister Punjab Pervez Elahi, 2005; declared but not deposited).
- Three Toyota vehicles in April 2006 (two Lexus 470s and a VXR), listed as declared but not deposited.
- A golden rifle assessed at PKR 600,000 (Chairman Senate Sadiq Sanjrani, 2019).
- Four photographs of the President with Mr and Mrs G. W. Bush.
- A model made of chocolate.

## By affiliation

| Affiliation | Records | Assessed (PKR m) | Paid (PKR m) | Paid % |
|---|---:|---:|---:|---:|
| PMLN | 256 | 425.3 | 53.2 | 12.5 |
| Unlabelled | 1,006 | 403.4 | 57.5 | 14.3 |
| PPP | 246 | 175.2 | 22.1 | 12.6 |
| PTI | 261 | 154.6 | 41.8 | 27.1 |
| Military | 732 | 82.5 | 14.7 | 17.8 |
| Bureaucracy | 299 | 47.9 | 6.8 | 14.2 |
| Musharraf govt | 1,147 | 40.0 | 3.9 | 9.6 |
| Police | 119 | 16.3 | 3.0 | 18.5 |
| Media | 121 | 6.3 | 0.9 | 13.8 |

## By office holder (household)

| Person | Records | Assessed (PKR m) | Paid (PKR m) |
|---|---:|---:|---:|
| Shahid Khaqan Abbasi | 32 | 233.1 | 46.5 |
| Shehbaz Sharif | 66 | 161.3 | 0.5 |
| Asif Ali Zardari | 170 | 145.5 | 21.3 |
| Nawaz Sharif | 58 | 136.4 | 25.8 |
| Imran Khan | 109 | 123.8 | 34.4 |
| Khawaja Asif | 10 | 67.8 | 11.3 |
| Pervez Musharraf | 144 | 33.7 | 2.8 |
| Shaukat Aziz | 849 | 31.2 | 2.9 |
| Arif Alvi | 118 | 27.2 | 2.0 |
| Mamnoon Hussain | 87 | 22.6 | 7.4 |

Shehbaz Sharif's paid amount is low because his largest gifts were displayed at the Prime Minister House rather than retained.

## Caveats

These figures describe the dataset as published. It is not an audited record.

- Affiliation is incomplete. It is the dataset author's label and 24% of rows have none, so party totals are indicative only.
- Categories are partly inferred. The source leaves the item category blank for 1,876 rows; these were filled with keyword rules and 321 remain "Other".
- Some amounts are extraction errors. In 55 rows the amount paid is larger than the assessed value, which is why 2020 shows paid above 100% of assessed.
- People are mapped by name matching against 19 prominent office holders, and 2,166 records fall outside them. Gifts to spouses and children are counted under the office holder.
- 16 exact duplicate rows were removed. 3 records have no usable date.

## Folder layout

    toshakhana_gift_analysis.ipynb        main analysis notebook, saved with outputs
    toshakhana_report.pdf                 PDF summary of stats and charts
    make_report.py                        regenerates the PDF from the clean CSV
    requirements.txt
    data/toshakhana_refined_raw.csv       Kaggle "Refined_TK_data ver 2.csv", unmodified
    data/toshakhana_files_original.xlsx   Kaggle "Toshakhana Files 2.xlsx", unmodified
    data/toshakhana_clean.csv             cleaned output written by the notebook

## Running it

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

jupyter notebook toshakhana_gift_analysis.ipynb   # run all cells; writes data/toshakhana_clean.csv
python make_report.py                             # writes toshakhana_report.pdf
```

## Credits

Dataset compiled by Zeeshan-ul-hassan Usmani and published on Kaggle. The underlying records were released by the Cabinet Division, Government of Pakistan.

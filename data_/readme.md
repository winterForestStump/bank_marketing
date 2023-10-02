# bank_marketing

source: https://archive.ics.uci.edu/dataset/222/bank+marketing

The data is related with direct marketing campaigns (phone calls) of a Portuguese banking institution. The classification goal is to predict if the client will subscribe a term deposit (variable y).

The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be (or not) subscribed. 

There are two datasets: 
* bank-full.csv with all examples, ordered by date (from May 2008 to November 2010).
* bank.csv with 10% of the examples (4521), randomly selected from bank-full.csv. The smallest dataset is provided to test more computationally demanding machine learning algorithms (e.g. SVM).

Number of Instances: 45211 for bank-full.csv (4521 for bank.csv)

Number of Attributes: 16 + output attribute.

Attribute information:

Input variables:

bank client data:
 - age (numeric)
 - job : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur","student","blue-collar","self-employed","retired","technician","services") 
 - marital : marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)
 - education (categorical: "unknown","secondary","primary","tertiary")
 - default: has credit in default? (binary: "yes","no")
 - balance: average yearly balance, in euros (numeric) 
 - housing: has housing loan? (binary: "yes","no")
 - loan: has personal loan? (binary: "yes","no") related with the last contact of the current campaign:
 - contact: contact communication type (categorical: "unknown","telephone","cellular") 
 - day: last contact day of the month (numeric)
 - month: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")
 - duration: last contact duration, in seconds (numeric)

other attributes:
 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)
 - previous: number of contacts performed before this campaign and for this client (numeric)
 - poutcome: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")

Output variable (desired target):
- y - has the client subscribed a term deposit? (binary: "yes","no")

Missing Attribute Values: None

Created by: Paulo Cortez (Univ. Minho) and Sérgio Moro (ISCTE-IUL) @ 2012

This dataset is public available for research. The details are described in [Moro et al., 2011]. 

[Moro et al., 2011] S. Moro, R. Laureano and P. Cortez. Using Data Mining for Bank Direct Marketing: An Application of the CRISP-DM Methodology. 

In P. Novais et al. (Eds.), Proceedings of the European Simulation and Modelling Conference - ESM'2011, pp. 117-121, Guimarães, Portugal, October, 2011. EUROSIS.

Available at: [pdf] http://hdl.handle.net/1822/14838
              [bib] http://www3.dsi.uminho.pt/pcortez/bib/2011-esm-1.txt

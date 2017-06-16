# Facebook Group Files Downloader

---

## Description:

---
Python scripts to enable mass downloading of facebook group files (notes, doc, docx, presentation, pdf).

(work in progress...)

---
## Instructions To Use:
---
### Getting All The Files In One Page:
At first we are going to automate the most tiresome work - pressing the **"[see more](#)"**- button countless number of times. Plain old scrapping just using **`mechanize`** with **`beautifulsoup`** etc just not gonna work as pressing **"[see more](#)"** executes a JavaScript function that makes an Ajax call and thus populates the page. That is why we are going to use **`selenium`** as it is actually a real browser that scupports scripting.

We are going to start with downloding [selenium chrome webdriver](https://chromedriver.storage.googleapis.com/index.html?path=2.30/). Once the download is completed unzip it and add its path to *`env`* (windows users) / *`PATH`* (unix users) variable. Alternatively you can just put it in some place that is already known to system (i.e `/usr/local/bin`)

Then download **`selenium`** using python or pip from your terminal/cmd for example using the command ***`pip install selenium`***
(I am assuming you have python and pip installed. Incase you do not have them and/or have little knowledge about them, My suggestino to you would be installing **anaconda or miniconda or some other virtual environment managers** and creating a virtual env only for this purpose. Just search youtube with something like "Basic Anaconda Tutorial")

Now we can run our script. Though before running it we will need to adjaust few lines (Filename: massDownloader.py). Just edit the ***`email`, `password`*** with your valid cradentials and the ***`groupURL`*** variable with the group's(the one's files you want to downlaod.) file section's url.

Now run the script from terminal using the command ***`python massDownloader.py`*** and wait till it says **"Done"**.

Once the script is finish executing you should see a single page that links all the files.

***NOTE: *** **IF YOU SEE ANY KIND OF POPUPS OR MESSAGES IN THE BROWSER ASKING TO "ALLOW NOTIFICATION" JUST BLOCK THEM ONCE.**

---
### Saving As A PDF:
If you were just looking to avoid loading all the files everytime you need to search (using browsers search functionality **Ctrl + F**) you can just keep a *pdf* version of the page by printing it as a file using the command **Ctrl + P** (untick all the options (headers and footers, background graphics) if they are already ticked to get a better pdf) and saving it.

---
### Saving As An Offline Static Page:
You can also save it as an offline static page. But simply viewing page source and copying it to an .html file will not work. You will get the same first page with the button **"[see more](#)"** again. One way to get the page as it is, is to opening the "Dev Tools" by *right clicking* anyware in the page and then selecting **"Inspect Element"**; Once the dev tools is open *right click* on the ***`<html>`*** tag and select **"Edit as HTML"** and then just copy everything to save in a .html file(name it allfiles.html).

(**Will try to automate this part later**)

#### Fixing Local Page's Relative URL Problem:
Now if you try to open the saved static html file you will see that clicking on file links does not work. It redirects you to some path starting with **"file:///"**. This is simply because of the relative url structure of the facebook group file links(you don't need to know what a relative url is to make it work if you do not know already). If you fix this there is one more problem you will face that is even the fixed links does not open any files but pdf. This one is because of facebook's ajax call (They do not reload a page to load a note when we manually click on a link on their live page). So we have two more remaining problems. To solve them you do not need to do anything fancy but editing the ***`localURl`*** variable(filename: fixURL.py) with the local path of that file (right click on the saved file and select **open with a browser** and then copy the link from the address bar) and then running the command ***`python fixURL.py`***. Once it is done you will see a fixed static page named as **"all-files.html"**. (you will need `mechanize` and `beautifulsoup` for this. Try `pip install mechanize` and `pip install bs4`)

---
### Downloading All The PDFs, DOCs, DOCXs , Presentations And Notes(as PDFs/Texts):
Now that we have a local copy of the page, we can apply trivial scraping techniques on it to extract links or to download all the files (or whatever you wish :D).

***Working on it. Will update pretty soon....***

---

---

## Contact:
[**Email:**](fozleazimrabi2@gmail.com) fozleazimrabi2@gmail.com

[**Facebook Profile**](https://www.facebook.com/rabi.seu)

Any contribution / suggestion will be highly appriciated.

---

---


# <span style="color:red">Please Kinldy Check Facebook's Data Scraping Policy And Use At Your Own Risk</span>

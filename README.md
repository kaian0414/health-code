# health-code
This is the codes for automatic generating the health code with using the web version on 13-Sept-2021. It is just for learning, If you want to use this code for further learning, please be careful of inputting **REAL** information and health states.

## ***Since the concepts of version 1 is not really good in implementation, I updated version 2 at night. All the information in this repository is updated.***

## Pre-requisites
- Basic Python knowledge
- Basic HTML knowledge

Note: The knowledge of automatic inserting data is not difficult at all, you can learn it while working of this mini-project.

## Environment Setting
Assume that everyone has the Python programing environment. I only mentioned the extra settings here.

Suppose that, everyone are using Google Chrome in this project, I will introduce the settings related to Google Chrome. If you are using other browser, please search the settings online, or download Google Chrome.

Download Google Chrome: https://www.google.com/intl/zh-TW/chrome/

**Step 1: Check your Google Chrome Verion in setting**

![checkChromeVersion](https://user-images.githubusercontent.com/34164281/133873888-e7ba5aab-fdc1-409f-986d-9b6fa057288a.png)

**Step 2: Download the suitable version of ChromeDriver**

https://sites.google.com/a/chromium.org/chromedriver/downloads

**Step 3: Put 'chromedriver.exe' under the folder where the 'chrome.exe' is in.**

My directory: ```C:\Program Files (x86)\Google\Chrome\Application```
Your directory may *similar* as mine.


**Step 4: Start Coding**

## Coding
You can copy my code and insert your own information and setting.

Please note that you need to install selenium before running the code. ```pip install selenium```

After that, learn from the code. I put some comment while coding and I hope you can understand.

## Information of using my code
- line 11: Please the directory of 'chromedriver.exe'
- line 21-29: Please put your own information
- line 72: Getting your address for health code from government
- line 28-29 and 75-83: Inserting the address by yourself
- line 98: Selecting the directory where you want to save the screenshot of health code

Note:
- If you want to insert your address yourseslf, please don't comment line 28-29 and 75-83 but commented on line 72.
- For line 28-29, the information should be tested by yourself.
- For this coding, I tested what I should input in order to get only one option to choose.
  - search_address: your input text
  - complete_address: the information that can be searched from the website

![building](https://github.com/kaian0414/healthy-code/blob/main/building.png)

## Result

![healthCode_result](https://github.com/kaian0414/healthy-code/blob/main/healthCode_result.jpg)

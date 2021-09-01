# TradingView-trading-record-crawler
匯出自己 TradingView Paper Trading 交易數據

## 【說明】
這隻爬蟲可以透過網頁版 Trading View 爬取「Paper Trading」歷史交易數據，並輸出 XLSX/CSV 檔案。

## 【使用說明】
1. 在專案內新增「personal_account.txt」，並輸入「帳號」、「密碼」，程式執行時會自動讀取本文件。
2. 執行程式，輸出的檔案會放在「./portfolio_record_archieve/」內。
3. 若需要增加爬取資料筆數，可以調整 loading loop (line 97)，增加 Page Scrolling 次數。

---

## 【Description】
This crawler can help to export the "paper trading record" in TradingView from web page into xlsx or csv format.

## 【Guide】
1. Add a new .txt named "personal_account.txt" and key in your TradingView account and password in two line.
2. Run the script, the exported file will be saved in "./portfolio_record_archieve/"
3. You can modify the num of "Loading Loop" (line 97) to increase the num of loading data if needed.

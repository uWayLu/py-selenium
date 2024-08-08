# README

## Traditoinal

### Requirements
+ requirements.txt
+ chrome and corresponded chromedriver
  https://www.chromium.org/getting-involved/download-chromium/ 

## Deploy with Docker/Podman
`cd deploy` first

### start service
`docker-compose up -d`

### run scripts
+ rfp print `docker-compose exec py-selenium ./print_rfp_url.sh ${URL}`
+ chrome native print `docker-compose exec py-selenium ./print_to_pdf.sh ${URL}`

### stop service
`docker-compose stop`

## References
+ Official
+ [Sample Code](https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/drivers/test_remote_webdriver.py)
+ https://blog.csdn.net/weixin_42333581/article/details/124382171
+ [Chrome New Headless: disable print header/footer](https://stackoverflow.com/questions/55418415/disable-chromes-default-headers-footers-in-headless-print-to-pdf)
+ [disable selenium(Chrome) print header/footer](https://stackoverflow.com/questions/60609330/how-do-i-disable-headers-and-footers-selenium-printing)
+ [GitHub: SeleniumHQ/docker-selenium](https://github.com/SeleniumHQ/docker-selenium)
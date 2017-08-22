var page = require('webpage').create();
headers = {
    "Origin": "http://www.gsxt.gov.cn", 
    "Proxy-Connection": "keep-alive", 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36", 
    "Host": "www.gsxt.gov.cn", 
    "Referer": "http://www.gsxt.gov.cn/index.html", 
    "Cache-Control": "max-age=0"
}
url = 'http://www.gsxt.gov.cn/%7B_pWUDrNMwf72zyd7L0uL_rwgBKPLfirkASiNY9iqgMZbNJX-my8ZQIt9CZjwMKtMCI1iN-27tZX32a1gM06sbXy9yJ68_o7ktMZnd522VgxeJoBjGIoz8jA23bc880EZlCXSRI9UhDH2ZTxaoKWjFA-1503397350926%7D'
page.open(url,headers,function(){
	page.render('test1.png');
	phantom.exit();
});

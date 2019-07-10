# coding = 'utf-8'
import json
import requests
import time
import datetime

city_list = [
        "北京", "上海", "天津", "重庆", "香港","澳门" ,"哈尔滨","齐齐哈尔","牡丹江","大庆","伊春","双鸭山","鹤岗","鸡西","佳木斯","七台河","黑河","绥化","大兴安岭",
        "长春","延吉","吉林","白山","白城","四平","松原","辽源","大安","通化","沈阳","大连","葫芦岛","盘锦","本溪","抚顺","铁岭","辽阳","营口","阜新","朝阳","锦州","丹东","鞍山",
        "呼和浩特","呼伦贝尔","锡林浩特","包头","赤峰","海拉尔","乌海","鄂尔多斯","通辽","石家庄","唐山","张家口","廊坊","邢台","邯郸","沧州","衡水","承德","保定","秦皇岛",
        "郑州","开封","洛阳","平顶山","焦作","鹤壁","新乡","安阳","濮阳","许昌","漯河","三门峡","南阳","商丘","信阳","周口","驻马店",
        "济南","青岛","淄博","威海","曲阜","临沂","烟台","枣庄","聊城","济宁","菏泽","泰安","日照","东营","德州","滨州","莱芜","潍坊",
        "太原","阳泉","晋城","晋中","临汾","运城","长治","朔州","忻州","大同","吕梁","银川","固原","中卫","石嘴山","吴忠",
        "南京","苏州","昆山","南通","太仓","吴县","徐州","宜兴","镇江","淮安","常熟","盐城","泰州","无锡","连云港","扬州","常州","宿迁",
        "合肥","巢湖","蚌埠","安庆","六安","滁州","马鞍山","阜阳","宣城","铜陵","淮北","芜湖","毫州","宿州","淮南","池州","西安","韩城","安康","汉中","宝鸡","咸阳","榆林","渭南","商洛","铜川","延安",
        "兰州","白银","庆阳","酒泉","天水","武威","张掖","甘南","临夏","平凉","定西","金昌","西宁","海北","海西","黄南","果洛","玉树","海东","海南",
        "武汉","宜昌","黄冈","恩施","荆州","神农架","十堰","咸宁","襄阳","孝感","随州","黄石","荆门","鄂州","长沙","邵阳","常德","郴州","吉首","株洲","娄底","湘潭","益阳","永州","岳阳","衡阳","怀化","韶山","张家界",
        "杭州","湖州","金华","宁波","丽水","绍兴","衢州","嘉兴","台州","舟山","温州","南昌","萍乡","九江","上饶","抚州","吉安","鹰潭","宜春","新余","景德镇","赣州",
        "福州","厦门","龙岩","南平","宁德","莆田","泉州","三明","漳州","贵阳","安顺","赤水","遵义","铜仁","六盘水","毕节","凯里","都匀",
        "成都","泸州","内江","凉山","阿坝","巴中","广元","乐山","绵阳","德阳","攀枝花","雅安","宜宾","自贡","甘孜州","达州","资阳","广安","遂宁","眉山","南充",
        "广州","深圳","潮州","韶关","湛江","惠州","清远","东莞","江门","茂名","肇庆","汕尾","河源","揭阳","梅州","中山","德庆","阳江","云浮","珠海","汕头","佛山",
        "南宁","桂林","阳朔","柳州","梧州","玉林","桂平","贺州","钦州","贵港","防城港","百色","北海","河池","来宾","崇左",
        "昆明","保山","楚雄","德宏","红河","临沧","怒江","曲靖","思茅","文山","玉溪","昭通","丽江","大理","海口","三亚","儋州","琼山","通什","文昌",
        "乌鲁木齐","阿勒泰","阿克苏","昌吉","哈密","和田","喀什","克拉玛依","石河子","塔城","库尔勒","吐鲁番","伊宁","拉萨","阿里","昌都","那曲","日喀则","山南","林芝","台北","高雄"
]
header ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}
city_dirt = {}

def get_whether():
    for city_name in city_list:
        url = " http://wthrcdn.etouch.cn/weather_mini?city=" + city_name
        response = requests.get(url, params=header)
        wether_dirt = response.json()
        if 'data' in wether_dirt.keys() and 'yesterday' in wether_dirt['data'].keys():
            city_dirt[wether_dirt['data']['city']] = {'high': wether_dirt['data']['yesterday']['high'], 'low': wether_dirt['data']['yesterday']['low'], 'type': wether_dirt['data']['yesterday']['type']}
        else:
            city_dirt[city_name] = "无数据"
    filename1 = 'C:/Users/Administrator/Desktop/whether/'
    filename2 = (str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day - 1) + '.json')
    with open(str(filename1 + filename2), 'w') as f:
        json.dump(city_dirt, f)
    print("气温天气成功抓取：", (str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day - 1) + '.json'))

if __name__ == '__main__':
    get_whether()


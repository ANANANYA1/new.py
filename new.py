import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#chrome_driver_path = 'C:\\Users\\admin\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe'
#driver = webdriver.Chrome()
#url="http://xl.upol.cn/portal/home.aspx"
#driver.get(url)
#driver.refresh()
#driver.find_element(by=By.ID, value="username").send_keys("jianghao")
#driver.find_element(by=By.ID, value="password").send_keys("Upol@280019")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
# selenium 运行时会从系统的环境变量中查找 webdriver.exe
# 一般把 webdriver.exe 放到 python 目录中，这样就不用在代码中指定。
chrome_driver = "C:\\Users\\a1315\\Documents\\Tencent Files\\1315197836\\FileRecv\\chromedriver_win32 (3)\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver , chrome_options=chrome_options)

#driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/div[4]/a[3]").click()

driver.find_element(by=By.ID, value="next").click()
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/div[3]/div[31]/input").clear()
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/div[3]/div[32]/input").clear()
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/div[3]/div[33]/input").clear()
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/div[3]/div[34]/input").clear()
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/div[3]/div[35]/input").clear()
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/div[3]/div[36]/input").clear()
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/div[3]/div[37]/input").clear()
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/div[3]/div[38]/input").clear()
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/div[3]/div[39]/input").clear()
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/div[3]/div[40]/input").clear()

for i in range(1, 11, 1):
    x = ""
    x = str(30 + i)
    # num = str(x)
    # suoyin = "[tabindex='"+num+"']"
    # driver.find_element(by=By.CSS_SELECTOR, value=suoyin).send_keys(0)
    mystr = str(i + 1)
    fullpath = "/html/body/div[2]/div/div/div[2]/div[3]/div[" + mystr + "]/form/div/div[1]/div/div/div[2]/div"
    daanpath = "/html/body/div[2]/div/div/div[2]/div[3]/div[" + mystr + "]/form/div/div[1]/div/div/div[3]"
    wentitext = driver.find_element(by=By.XPATH,
                                    value=fullpath).text
    daantext = driver.find_element(by=By.XPATH, value=daanpath).text
    if wentitext == "题目：计算机控制系统由哪几部分组成，各有什么作用？":
        score = 0.0
        if (daantext.find("硬件") != -1):
            score += 2
        if (daantext.find("软件") != -1):
            score += 2
        if (daantext.find("调节规律") != -1):
            score = 6
        if (daantext.find("输入") != -1):
            score += 1
        if (daantext.find("输出") != -1):
            score += 1
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：等效离散化设计方法存在哪些缺陷？":
        score = 0.0
        if (daantext.find("采样周期") != -1):
            score += 2
        if (daantext.find("失控") != -1):
            score += 2
        if (daantext.find("超过它") != -1):
            score += 2
        if (daantext.find("近似设计") != -1):
            score = 6
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：简述PID调节器的作用。":
        score = 0.0
        if (daantext.find("P") != -1 or daantext.find("比例") != -1):
            score += 2
        if (daantext.find("I") != -1 or daantext.find("积分") != -1):
            score += 2
        if (daantext.find("D") != -1 or daantext.find("微分") != -1):
            score += 2
        if (daantext.find("动态性能") != -1):
            score = 6
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：计算机控制系统有哪四种形式的信号？各有什么特点?":
        score = 0.0
        if (daantext.find("连续") != -1):
            score += 2
        if (daantext.find("阶梯") != -1):
            score += 2
        if (daantext.find("脉冲") != -1 or daantext.find("采样") != -1):
            score += 2
        if (daantext.find("数字") != -1 or daantext.find("离散") != -1):
            score += 2
        if (daantext.find("量化处理") != -1):
            score = 6
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：梯形图与继电器电路图有哪些异同点？":
        score = 0.0
        if (daantext.find("电压要求") != -1):
            score += 2
        if (daantext.find("回路") != -1):
            score += 2
        if (daantext.find("触点") != -1):
            score += 2
        if (daantext.find("通电后会产生变化") != -1):
            score += 2
        if (daantext.find("注意先后") != -1):
            score += 2
        if (daantext.find("下降沿") != -1):
            score += 2
        if (daantext.find("常开点") != -1):
            score = 6
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：简述程序存储器与数据存储器的区别？":
        score = 0.0
        if (daantext.find("只读") != -1):
            score += 2
        if (daantext.find("数据") != -1):
            score += 2
        if (daantext.find("断电") != -1):
            score += 2
        if (daantext.find("将丢失") != -1):
            score = 6
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：简述输入继电器、输出继电器、定时器及计数器的用途？":
        score = 0.0
        if (daantext.find("输入") != -1):
            score += 2
        if (daantext.find("延时控制") != -1):
            score += 1
        if (daantext.find("输出") != -1):
            score += 2
        if (daantext.find("计数") != -1 or daantext.find("个数") != -1):
            score += 1
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：非积算定时器与积算定时器的区别？":
        score = 0.0
        if (daantext.find("保持") != -1):
            score += 2
        if (daantext.find("复位") != -1):
            score += 2
        if (daantext.find("计数") != -1):
            score += 2
        if (daantext.find(
                ",在定时过程中,若遇停电或驱动定时器线圈的输入断开,定时器内的脉冲计数器将不保存计数值,当复电后或驱动定时器线圈的输入再次接通后,计数器又从零开始计数. 积算定时器由于有锂电池后备,当定时过程中突然停电或驱动定时器线圈的输入断开") != -1):
            score = 4
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：简述89C51单片机终端的概念。":
        score = 0.0
        if (daantext.find("外部发生的某一事件请求CPU迅速去处理") != -1):
            score = 6
        if (daantext.find("领导") != -1):
            score += 2
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：在国内外有哪些公司生产PLC，他们有哪些主要的产品？":
        score = 0.0
        if (len(daantext) >= 20):
            score = 4
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：请说明MC与MCR指令在应用中的注意要点？":
        score = 0.0
        if (len(daantext) > 10): score += 1
        if (daantext.find("NO指令") != -1 or daantext.find("NO 指令") != -1 or daantext.find("N0指令") != -1):
            score = 6
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：简述PLC的工作过程？":
        score = 0.0
        if (daantext.find("输入") != -1):
            score += 2
        if (daantext.find("程序处理") != -1):
            score += 2
        if (daantext.find("输出") != -1):
            score += 2
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：什么是最少拍设计？":
        score = 0.0
        if (daantext.find("最少拍") != -1):
            score += 1
        if (daantext.find("输入信号") != -1):
            score += 2
        if (daantext.find("稳态误差为零") != -1):
            score += 4
        if (daantext.find("最少拍设计") != -1):
            score += 1
        if (daantext.find("稳态") != -1):
            score += 2
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：M8002、M8013的功能是什么？":
        score = 0.0
        if (daantext.find("初始") != -1):
            score += 3
        if (daantext.find("1秒") != -1 or daantext.find("一秒") != -1 or daantext.find("1s") != -1):
            score += 3
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：有哪几种改进型数字PID 算法？":
        score = 0.0
        if (daantext.find("积分分离") != -1):
            score += 2
        if (daantext.find("遇限") != -1):
            score += 2
        if (daantext.find("不完全微分") != -1):
            score += 2
        if (daantext.find("微分项的输入滤波") != -1 or daantext.find("微分先行") != -1):
            score += 2
        if (daantext.find("不对设定值产生微分作用") != -1):
            score += 2
        if (daantext.find("具有不灵敏区的PID") != -1 or daantext.find("死区") != -1):
            score += 2
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：PLC有哪些主要的性能指标？":
        score = 0.0
        if (daantext.find("储存") != -1 or daantext.find("存储") != -1):
            score += 2
        if (daantext.find("I/O") != -1):
            score += 2
        if (daantext.find("数量") != -1 or daantext.find("复杂") != -1):
            score += 2
        if (daantext.find("种类") != -1):
            score += 2
        if (daantext.find("特殊") != -1):
            score += 2
        if (daantext.find("拓展") != -1):
            score += 2
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：一个计算机控制系统的最小采样周期受到什么因素限制？":
        score = 0.0
        if (daantext.find("采样") != -1):
            score += 2
        if (daantext.find("给定") != -1):
            score += 2
        if (daantext.find("被控") != -1):
            score += 2
        if (daantext.find("执行") != -1):
            score += 2
        if (daantext.find("算法") != -1):
            score += 2
        if (daantext.find("回路") != -1):
            score += 2
        if (daantext.find("开销") != -1):
            score += 2
        if (daantext.find("处理速度") != -1):
            score += 2
        if (daantext.find("意义不大") != -1):
            score += 6
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：为什么说计算机集成制造系统是工业自动化的发展趋势？":
        score = 0.0
        if (len(daantext) > 30):
            score = 3
        if (daantext.find("大规模及超大规模集成电路的发展，提高了计算机的可靠性和性能价格比") != -1):
            score += 6
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：简述计算机控制系统的硬件和软件的组成。":
        score = 0.0
        if (daantext.find("控制对象") != -1):
            score += 2
        if (daantext.find("检测环节") != -1):
            score += 2
        if (daantext.find("计算机") != -1):
            score += 2
        if (daantext.find("输入输出通道") != -1):
            score += 2
        if (daantext.find("外部设备") != -1):
            score += 2
        if (daantext.find("操作台") != -1):
            score += 2
        if (daantext.find("系统软件") != -1):
            score += 2
        if (daantext.find("软件") != -1):
            score += 2
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：模拟调节器与数字调节器有何区别？":
        score = 0.0
        if (daantext.find("数字信号") != -1):
            score += 2
        if (daantext.find("信号匹配") != -1):
            score += 2
        if (daantext.find("模拟") != -1):
            score += 2
        if (daantext.find("相互转换") != -1):
            score += 2
        if (daantext.find("直接输出") != -1):
            score += 2
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：简要说明什么是计算机控制系统？":
        score = 0.0
        if (daantext.find("计算机控制系统") != -1):
            score += 1
        if (daantext.find("自动控制系统") != -1):
            score += 2
        if (daantext.find("模拟控制装置") != -1):
            score += 2
        if (daantext.find("硬件") != -1):
            score += 2
        if (daantext.find("软件") != -1):
            score += 2
        if (daantext.find("这里的计算机通常指数字计算机，可以有各种规模，如从微型到大型的通用或专用计算机。") != -1):
            score = 4
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：计算机控制系统有哪些优点？":
        score = 0.0
        if (daantext.find("灵活") != -1 or daantext.find("简单") != -1):
            score += 2
        if (daantext.find("性能指标") != -1 or daantext.find("实时性好，可靠性高和适应性强") != -1):
            score += 2
        if (daantext.find("抗干扰") != -1):
            score += 2
        if (daantext.find("控制精度") != -1):
            score += 2
        if (daantext.find("性价比") != -1):
            score += 2
        if (daantext.find("自动化程度") != -1):
            score += 2
        if (daantext.find("智能化") != -1):
            score += 2
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：简述PLC的发展趋势。":
        score = 0.0
        if (daantext.find("高速度") != -1):
            score += 1
        if (daantext.find("大型") != -1 or daantext.find("小型") != -1):
            score += 1
        if (daantext.find("智能") != -1 or daantext.find("通信") != -1):
            score += 1
        if (daantext.find("故障") != -1 or daantext.find("检测") != -1 or daantext.find("处理") != -1):
            score += 2
        if (daantext.find("编程") != -1 or daantext.find("多样化") != -1):
            score += 2
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：什么是脉冲传递函数？":
        score = 0.0
        if (daantext.find("(z)") != -1 or daantext.find("脉冲") != -1 or daantext.find("初始静止") != -1):
            score = 6
        elif (daantext.find("拉氏") != -1 or daantext.find("变换") != -1):
            score = 3
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：线性离散系统的脉冲传递函数的定义是什么？":
        score = 0.0
        if (daantext.find("拉氏") != -1 or daantext.find("变换") != -1 or daantext.find("z") != -1):
            score = 6
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：什么是低压电器？低压电器是怎样分类的？":
        score = 0.0
        if (daantext.find("50Hz") != -1 or daantext.find("1200V") != -1 or daantext.find("1500V") != -1):
            score += 5
        if (daantext.find("开关") != -1 or daantext.find("电器") != -1):
            score += 2
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：简述PLC的主要功能有哪些？":
        score = 0.0
        if (daantext.find("逻辑") != -1):
            score += 1
        if (daantext.find("定时") != -1):
            score += 1
        if (daantext.find("计数") != -1):
            score += 1
        if (daantext.find("步进") != -1):
            score += 1
        if (daantext.find("数据处理") != -1):
            score += 1
        if (daantext.find("过程控制") != -1):
            score += 1
        if (daantext.find("通信联网") != -1):
            score += 1
        if (daantext.find("监控") != -1):
            score += 1
        if (daantext.find("停电") != -1):
            score += 1
        if (daantext.find("故障诊断") != -1):
            score += 1
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：什么是机电一体化系统？":
        score = 0.0
        if (daantext.find("引入") != -1):
            score += 1
        if (daantext.find("机械") != -1):
            score += 1
        if (daantext.find("执行部件") != -1):
            score += 1
        if (daantext.find("计算机") != -1):
            score += 1
        if (daantext.find("软件") != -1):
            score += 1
        if (daantext.find("系统") != -1):
            score += 2
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：梯形图编程的设计原则是什么？":
        score = 0.0
        if (daantext.find("左母线") != -1):
            score += 2
        if (daantext.find("垂直线") != -1):
            score += 2
        if (daantext.find("并联块串联") != -1 or daantext.find("左重右轻") != -1):
            score += 2
        if (daantext.find("串联块并联") != -1 or daantext.find("重下轻") != -1):
            score += 2
        if (daantext.find("双线圈") != -1):
            score += 2
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：如何消除比例和微分饱和现象？":
        score = 0.0
        if (daantext.find("积分补偿") != -1):
            score += 6
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：阶跃响应不变法的基本思想是什么？":
        score = 0.0
        if (daantext.find("离散") != -1):
            score += 6
        if (daantext.find("采样值") != -1):
            score += 6
        if (daantext.find("阶跃") != -1):
            score += 6
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：片机89C51有哪些中断源，对其中断请求如何进行控制？":
        score = 0.0
        if (daantext.find("5") != -1):
            score += 1
        if (daantext.find("INT0") != -1):
            score += 1
        if (daantext.find("INT1") != -1):
            score += 1
        if (daantext.find("T0") != -1):
            score += 1
        if (daantext.find("T1") != -1):
            score += 1
        if (daantext.find("TXD") != -1):
            score += 1
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：如何定义计数器的设定值？":
        score = 0.0
        if (daantext.find("K100") != -1):
            score += 6
        if (daantext.find("D10") != -1):
            score += 6
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：简述51系列单片机中断响应的条件。":
        score = 0.0
        if (daantext.find("请求") != -1):
            score += 1
        if (daantext.find("EA=1") != -1):
            score += 1
        if (daantext.find("允许位") != -1):
            score += 1
        if (daantext.find("被服务") != -1):
            score += 1
        if (daantext.find("指令周期") != -1):
            score += 1
        if (daantext.find("RETI") != -1):
            score += 1
        if(daantext.find("判断-------中断响应-------中断返回") != -1):
            score = 4
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：何为积分饱和现象？":
        score = 0.0
        if (daantext.find("控制系统") != -1):
            score += 2
        if (daantext.find("启动") != -1 or daantext.find("停止") != -1 or daantext.find("降低") != -1):
            score += 1
        if (daantext.find("偏差") != -1):
            score += 2
        if (daantext.find("消除") != -1):
            score += 1
        if (daantext.find("极限") != -1):
            score += 1
        if (daantext.find("绝对值") != -1):
            score += 1
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    elif wentitext == "题目：什么是主令电器？常用的主令电器有哪些？":
        score = 0.0
        if (daantext.find("控制系统") != -1):
            score += 1
        if (daantext.find("控制电路") != -1 or daantext.find("停止") != -1 or daantext.find("降低") != -1):
            score += 1
        if (daantext.find("指令") != -1):
            score += 1
        if (daantext.find("控制") != -1):
            score += 1
        if (daantext.find("开关电器") != -1):
            score += 3
        if (daantext.find("控制按钮") != -1):
            score += 2
        if (daantext.find("行程开关") != -1):
            score += 2
        if (daantext.find("接近开关") != -1):
            score += 2
        if (daantext.find("万能转换开关") != -1):
            score += 2
        if (daantext.find("主令控制器") != -1):
            score += 2
        if (daantext.find("主令电器") != -1):
            score += 2
        if (daantext.find("脚踏开关") != -1):
            score += 2
        if (daantext.find("倒顺开关") != -1):
            score += 2
        if (daantext.find("紧急开关") != -1):
            score += 2
        if (daantext.find("钮子开关") != -1):
            score += 2
        if (score > 6): score = 6
        driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='" + x + "']").send_keys(str(score))
    else:
        print("有新的题目请补充答案")

driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/div[2]/span[8]").click()
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div[2]/div[4]/a[1]").click()





'''

driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='33']").send_keys("6")
driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='34']").send_keys("6")
driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='35']").send_keys("6")
driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='36']").send_keys("6")
driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='37']").send_keys("6")
driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='38']").send_keys("6")
driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='39']").send_keys("6")
driver.find_element(by=By.CSS_SELECTOR, value="[tabindex='40']").send_keys("6")
'''
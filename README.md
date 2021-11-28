# fifth_project
青年大学习16倍速播放＋自动答题+截图保存
注意：
1、自动答题不会去识别题目，就是单纯的选某个选项，因为青年大学习只看你有没有完成，不看其中的答题情况。
2、代码需要更改的地方为
  Select(driver.find_element_by_css_selector('#province')).select_by_visible_text('浙江省')
  Select(driver.find_element_by_css_selector('#city')).select_by_visible_text('绍兴市')
只需将这里的"浙江省""绍兴市"改成你青年大学习的省和市。
3、运行代码首先需要输入这期青年大学习的网址，获取方式手机和电脑上都能获取。手机上就是在点开始学习按钮时，右上角三个点点击复制链接。
4、倒数第五行（如下，实现的功能是截屏保存到桌面）如果发现运行不了，就只能老老实实用上一行注释掉的语句，并把路径更改为自己桌面。
  driver.get_screenshot_as_file(r'{}\{}.png'.format(desktop_path(), a))
5、如果不需要截图保存，就将最后一个try except语句注释即可！！！

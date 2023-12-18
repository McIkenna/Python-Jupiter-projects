from mercywebsite.mercy import Mercy

with Mercy() as bot:
    bot.land_first_page()
    # bot.toggle_menu('svg[data-testid="MenuOutlinedIcon"]')
    # bot.change_mode('svg[data-testid="LightModeOutlinedIcon"]')

    bot.click_on_sidebar('skill')
    # bot.click_date('td[data-date="2023-04-04"]')
    #bot.select_nav_items("pro-inner-item", "svg")
    # bot.click_on_sidebar('dashboard')
    # bot.click_on_sidebar('education')
    # bot.click_on_sidebar('work')
    # bot.click_on_sidebar('project')
    # bot.click_on_sidebar('publication')
    # bot.click_on_sidebar('piechart')
    # bot.click_on_sidebar('funnelchart')
    # bot.click_on_sidebar('calender')
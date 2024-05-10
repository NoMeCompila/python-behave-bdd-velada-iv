from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given(u'Navego a la velada IV')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://lavelada.es/")

@when(u'Busco el titulo')
def step_impl(context):
    #txt = context.driver.find_element_by_xpath("//a/span[@class='relative']").text()
    txt = context.driver.find_element(By.XPATH, "//a/span[@class='relative']").text
    assert txt == "twitch.tv/ibai"
    #time.sleep(3)

@then(u'Valido que sea el canal de Ibai')
def step_impl(context):
    context.driver.quit()

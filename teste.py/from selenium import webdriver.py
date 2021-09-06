from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.atualcard.com.br/')
driver.execute_script("window.open('https://www.imprimarapido.com.br/', '_blank')")
driver.switch_to_window(driver.window_handles[1])
driver.execute_script("window.open('https://www.paulistacartoes.com.br/', '_blank')")
driver.switch_to_window(driver.window_handles[2])
driver.execute_script("window.open('https://www.cartoesmaisbarato.com.br/', '_blank')")
driver.switch_to_window(driver.window_handles[3])
driver.execute_script("window.open('https://www.graficacores.com.br/', '_blank')")
driver.switch_to_window(driver.window_handles[4])
driver.execute_script("window.open('https://www.graficacartaodevisita.com.br/', '_blank')")
driver.switch_to_window(driver.window_handles[5])
driver.execute_script("window.open('https://www.graficadasgraficas.com.br/', '_blank')")
driver.switch_to_window(driver.window_handles[6])
driver.execute_script("window.open('https://www.fabricadolivro.com.br/', '_blank')")
driver.switch_to_window(driver.window_handles[7])
driver.execute_script("window.open('https://www.graficapolitica.com.br/', '_blank')")
driver.switch_to_window(driver.window_handles[8])
driver.execute_script("window.open('https://www.nordestegraf.com.br/', '_blank')")
driver.switch_to_window(driver.window_handles[9])
driver.execute_script("window.open('https://www.graficadoevento.com.br/', '_blank')")
driver.switch_to_window(driver.window_handles[10])
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + SHIFT + 't')
driver.execute_script("window.open('https://savecash.atualcard.com.br/', '_blank')")







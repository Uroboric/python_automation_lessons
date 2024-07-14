import allure
from allure_commons.types import AttachmentType


def add_screenshots(driver):
    """
    Capture and attach a screenshot to the Allure report.
    """
    try:
        png = driver.get_screenshot_as_png()
        allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')
    except Exception as e:
        allure.attach(body=str(e), name='screenshot_error', attachment_type=AttachmentType.TEXT)


def add_logs(driver):
    """
    Capture and attach browser logs to the Allure report.
    """
    try:
        log = "".join(f'{text}\n' for text in driver.get_log(log_type='browser'))
        allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')
    except Exception as e:
        allure.attach(body=str(e), name='log_error', attachment_type=AttachmentType.TEXT)


def add_html(driver):
    """
    Capture and attach the page source (HTML) to the Allure report.
    """
    try:
        html = driver.page_source
        allure.attach(html, 'page_source', AttachmentType.HTML, '.html')
    except Exception as e:
        allure.attach(body=str(e), name='html_error', attachment_type=AttachmentType.TEXT)


def add_video(driver):
    """
    Attach the video recording of the browser session to the Allure report.
    """
    try:
        video_url = f"https://selenoid.autotests.cloud/video/{driver.session_id}.mp4"
        html = (
            "<html><body><video width='100%' height='100%' controls autoplay>"
            f"<source src='{video_url}' type='video/mp4'></video></body></html>"
        )
        allure.attach(html, f'video_{driver.session_id}', AttachmentType.HTML, '.html')
    except Exception as e:
        allure.attach(body=str(e), name='video_error', attachment_type=AttachmentType.TEXT)

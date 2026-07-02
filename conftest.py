from pathlib import Path

import pytest
import pytest_html
from config import url
from playwright.sync_api import sync_playwright


@pytest.fixture()
def page():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)

    videos_dir = Path("videos")
    videos_dir.mkdir(exist_ok=True)

    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(videos_dir),
    )
    page = context.new_page()

    page.goto(url)
    page.wait_for_load_state("load")

    yield page

    try:
        context.close()
    except Exception:
        pass

    try:
        browser.close()
    except Exception:
        pass

    try:
        p.stop()
    except Exception:
        pass


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = list(getattr(report, "extra", []))

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            screenshot_path = screenshots_dir / f"{item.name}.png"
            page.screenshot(path=str(screenshot_path))
            extra.append(pytest_html.extras.image(str(screenshot_path)))

            video_path = None
            try:
                video_path = page.video.path() if getattr(page, "video", None) else None
            except Exception:
                video_path = None

            if not video_path and getattr(page, "context", None):
                try:
                    page.context.close()
                except Exception:
                    pass

                try:
                    video_path = page.video.path() if getattr(page, "video", None) else None
                except Exception:
                    video_path = None

            if video_path and Path(video_path).exists():
                extra.append(pytest_html.extras.url(str(video_path)))

        report.extra = extra
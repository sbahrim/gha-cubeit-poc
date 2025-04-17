from playwright.sync_api import Page, expect

BASE_URL = "http://127.0.0.1:8000/"

def test_cubeit(page: Page):
    page.goto(BASE_URL)

    input = page.get_by_placeholder("enter number...")
    input.fill("3")

    page.get_by_role("button", name="Cube").click()
    
    result = page.locator("css=p#result")

    expect(result).to_contain_text("27")

def test_empty_input(page: Page):
    page.goto(BASE_URL)

    input = page.get_by_placeholder("enter number...")
    input.fill("")

    page.get_by_role("button", name="Cube").click()

    result = page.locator("css=p#result")

    expect(result).to_contain_text("Enter something!")
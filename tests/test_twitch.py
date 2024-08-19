import pytest
from assertpy import assert_that

from pages.twitch_channels_results_page import TwitchChannelsResultsPage
from pages.twitch_home_page import TwitchHomePage
from pages.twitch_results_page import TwitchResultsPage
from pages.twitch_streamer_page import TwitchStreamerPage
from tests.conftest import take_screenshot


@pytest.mark.usefixtures('create_driver')
class TestTwitch:

    @pytest.mark.run()
    # This test clicks on a Streamer in Twitch
    def test_twitch_streamer_ui(self, prep_properties):
        # Navigates to Twitch
        twitch_home_page = TwitchHomePage(self.driver)

        # Search by Starcraft II
        twitch_home_page.search("Starcraft II")

        # Click on View All Channels
        twitch_results_page = TwitchResultsPage(self.driver)
        twitch_results_page.click_on_view_all_channels()

        # Scroll down 2 times
        twitch_channels_results_page = TwitchChannelsResultsPage(self.driver)
        twitch_channels_results_page.scroll_down()
        twitch_channels_results_page.scroll_down()

        # Click on the first streamer
        twitch_channels_results_page.click_on_channel()
        twitch_streamer_page = TwitchStreamerPage(self.driver)

        # Perform assertions and take a screenshot
        assert_that(twitch_streamer_page.is_visible(twitch_streamer_page.STREAMER_LOGO)).is_true()
        assert_that(twitch_streamer_page.is_visible(twitch_streamer_page.STREAMER_NAME)).is_true()
        assert_that(twitch_streamer_page.is_visible(twitch_streamer_page.FOLLOW_BUTTON)).is_true()
        assert_that(twitch_streamer_page.is_visible(twitch_streamer_page.VIDEO_PLAYER)).is_true()
        assert_that(twitch_streamer_page.is_visible(twitch_streamer_page.CHAT_WELCOME_MESSAGE)).is_true()
        assert_that(twitch_streamer_page.is_visible(twitch_streamer_page.CHAT_AREA)).is_true()

        take_screenshot(self.driver)
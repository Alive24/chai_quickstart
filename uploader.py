from chai_py import Metadata, package, upload_and_deploy, wait_for_deployment
from chai_py import share_bot
from chai_py.auth import set_auth

from starter_bot import Bot

from chai_py.defaults import GUEST_UID, GUEST_KEY

DEVELOPER_UID = None
DEVELOPER_KEY = None

if DEVELOPER_KEY is None or DEVELOPER_UID is None:
    raise RuntimeError("Please fetch your UID and KEY from the bottom of the Chai Developer Platform. https://chai.ml/dev")

set_auth(DEVELOPER_UID, DEVELOPER_KEY)
BOT_IMAGE_URL = "https://cutt.ly/lx0gnM9"

package(
    Metadata(
        name="Your First Bot! 🎉 🤖",
        image_url=BOT_IMAGE_URL,
        color="f1a2b3",
        description="Thank you for creating me ❤️",
        input_class=Bot,
     )
)

bot_uid = upload_and_deploy(
    "package.zip"
)

wait_for_deployment(bot_uid)

share_bot(bot_uid)

import streamlit.components.v1 as components
import os
from typing import Optional, Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


_RELEASE = True
COMPONENT_NAME = "streamlit_chat"

if _RELEASE:  # use the build instead of development if release is true
    root_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(root_dir, "frontend/build")

    _streamlit_chat = components.declare_component(
        COMPONENT_NAME,
        path = build_dir
    )
else:
    _streamlit_chat = components.declare_component(
        COMPONENT_NAME,
        url = "http://localhost:3001"
    )

def message(message: str, 
            is_user: Optional[bool] = False, 
            seed: Optional[Union[int, str]] = 88,
            key: Optional[str] = None,
            allow_html: Optional[bool] = False,
            is_table: Optional[bool] = False):
    """
    Creates a new instance of streamlit-chat component

    Parameters
    ----------
    message: str
        The message to be displayed in the component
    is_user: bool 
        if the sender of the message is user, if `True` will align the 
        message to right, default is False.
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns: None
    """
    _streamlit_chat(message=message, seed=seed, isUser=is_user, key=key, allow_html=allow_html, is_table=is_table)


if not _RELEASE:
    import streamlit as st  
    # testing
    long_message = """A chatbot or chatterbot is a software application used to conduct an on-line chat conversation via text or text-to-speech, in lieu of providing direct contact with a live human agent. 
    Designed to convincingly simulate the way a human would behave as a conversational partner, chatbot systems typically require continuous tuning and testing, and many in production remain unable to adequately converse, while none of them can pass the standard Turing test. 
    The term "ChatterBot" was originally coined by Michael Mauldin (creator of the first Verbot) in 1994 to describe these conversational programs.
    """

    message("Hello, I am a Chatbot, how may I help you?")
    message("Hey, \nwhat's a chatbot?", is_user=True)
    message(long_message)
    st.text_input("Message:")

# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-3.1-pro-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_bytes(
                    mime_type="application/vnd.google-apps.document",
                    data=base64.b64decode(
                        """ewogICJlcnJvciI6IHsKICAgICJjb2RlIjogNDAzLAogICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAiZXJyb3JzIjogWwogICAgICB7CiAgICAgICAgIm1lc3NhZ2UiOiAiT25seSBmaWxlcyB3aXRoIGJpbmFyeSBjb250ZW50IGNhbiBiZSBkb3dubG9hZGVkLiBVc2UgRXhwb3J0IHdpdGggRG9jcyBFZGl0b3JzIGZpbGVzLiIsCiAgICAgICAgImRvbWFpbiI6ICJnbG9iYWwiLAogICAgICAgICJyZWFzb24iOiAiZmlsZU5vdERvd25sb2FkYWJsZSIsCiAgICAgICAgImxvY2F0aW9uIjogImFsdCIsCiAgICAgICAgImxvY2F0aW9uVHlwZSI6ICJwYXJhbWV0ZXIiCiAgICAgIH0KICAgIF0KICB9Cn0K"""
                    ),
                ),
                types.Part.from_text(text="""I need a warm aesthetic coffee shop landing page."""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""**Defining the Project Scope**

Okay, I've got a handle on the objective: a Carrd-compatible coffee shop landing page, aesthetically warm. The JSON format is firm, and I'm organizing my thoughts around the four keys: design, structure, copy, and code. I'm focusing on defining scope.


**Refining the JSON Structure**

I'm now zeroing in on the JSON format constraints. It's clear that double-quoted strings are essential. Also, comments and control tokens, like newlines, are off-limits. I'm focusing on single-line JSON output, space-separated or using escaped characters if needed, completely eliminating raw newlines. My aim is a perfectly valid, compact JSON structure for the landing page. The overall theme will be \"Warm, aesthetic coffee\".


**Outlining the Design Elements**

I'm now outlining the design elements. I've defined the key aesthetic themes as \"Warm, cozy, aesthetic, inviting.\" I've selected a warm off-white background color, along with elegant fonts and accent colors. I'm focusing on providing the user with an \"aesthetic escape\" in the heart of the city. I'm choosing the appropriate headlines, subheadings, and CTAs. I'm also including all design notes.


**Implementing the Code Snippet**

I've crafted a custom CSS snippet for a warm hover effect on primary buttons. This \"Warm Mocha Button Hover Effect\" will provide a subtle coffee-toned glow to primary buttons on hover. I've focused on ensuring the code is clear, concise, and easy to implement within Carrd, using a transition for a smooth visual effect, which I am very happy with.


**Constructing the JSON Structure**

I'm now implementing the JSON structure, paying close attention to the formatting rules. All quotes are double quotes, and I'm ensuring there are absolutely no newlines or tabs in the final output. The draft outlines a \"design\" object with theme details and a \"structure\" array, outlining the hero and about sections. I'm focusing on crafting a valid, compact, single-line JSON string.


**Adding Feature Sections**

I'm now adding feature sections to the JSON. I've defined a 'Features' section with a three-column layout and light caramel background. I'm adding icons and text for three features. The footer has also been defined with location, hours, and social media links, using a dark espresso background.


**Finalizing the Snippet**

I've incorporated the custom CSS block as a \"Warm Mocha Button Hover Effect\" and I've now added detailed implementation instructions, which involves embedding a custom CSS block in a Hidden Embed element (set to Head or Body End) for the smooth effect on primary buttons. All keys have been verified. I'm focusing on ensuring it's a completely single-line JSON string.



**Defining the Key Sections**

I'm now diving into the JSON structure of the coffee shop landing page. I've defined the hero, about us, features, and footer sections, along with their respective container settings and elements. I'm focusing on ensuring these core content sections are accurately reflected in the JSON, including the container settings and essential elements for each.


"""),
                types.Part.from_text(text="""{\"design\":{\"theme_vibe\":\"Warm, aesthetic, cozy coffee shop\",\"background_color\":\"#FDFBF7\",\"primary_font\":\"Playfair Display\",\"secondary_font\":\"Lora\",\"accent_colors\":[\"#8C5A35\", \"#D9A05B\", \"#4A3B32\"]},\"structure\":[{\"section_name\":\"Hero Section\",\"container_settings\":\"Full width, background image of aesthetic coffee pour with warm brown overlay at 40 percent opacity\",\"elements_to_add\":[\"Text (Heading 1)\", \"Text (Subheadline)\", \"Button (Primary CTA)\"]},{\"section_name\":\"About Us\",\"container_settings\":\"Default width, centered, padding 4rem top/bottom, cream background\",\"elements_to_add\":[\"Text (Heading 2)\", \"Text (Paragraph: Brand Story)\", \"Image (Cozy cafe interior)\"]},{\"section_name\":\"Features\",\"container_settings\":\"Columns (3), staggered alignment, light caramel background #F4EFE6\",\"elements_to_add\":[\"Icon (Coffee bean)\", \"Text (Feature 1)\", \"Icon (Croissant)\", \"Text (Feature 2)\", \"Icon (Wifi)\", \"Text (Feature 3)\"]},{\"section_name\":\"Footer\",\"container_settings\":\"Full width, dark espresso background #4A3B32\",\"elements_to_add\":[\"Text (Location and Hours)\", \"Icons (Social Media Links)\"]}],\"copy\":{\"hero_h1\":\"Brewed with Love, Served with Warmth.\",\"hero_subheadline\":\"Your aesthetic escape in the heart of the city. Experience artisanal coffee and house-baked pastries in a cozy, sunlit space.\",\"primary_cta\":\"View Our Menu\",\"feature_bullets\":[\"Ethically sourced, locally roasted beans\", \"Fresh artisanal pastries baked daily\", \"Cozy corners with free high-speed Wi-Fi\"]},\"code\":[{\"plugin_name\":\"Warm Mocha Button Hover Effect\",\"instructions\":\"Embed this custom CSS block in a Hidden Embed element (set to Head or Body End) to add a smooth coffee-toned glow to all primary buttons.\",\"code_snippet\":\"<style>.button:hover { background-color: #8C5A35 !important; box-shadow: 0 4px 15px rgba(140, 90, 53, 0.4) !important; transition: all 0.3s ease-in-out; color: #FFF !important; }</style>\"}]}"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type = genai.types.Type.OBJECT,
            required = ["design", "structure", "copy", "code"],
            properties = {
                "design": genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["theme_vibe", "background_color", "primary_font", "secondary_font", "accent_colors"],
                    properties = {
                        "theme_vibe": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "background_color": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "primary_font": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "secondary_font": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "accent_colors": genai.types.Schema(
                            type = genai.types.Type.ARRAY,
                            items = genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                        ),
                    },
                ),
                "structure": genai.types.Schema(
                    type = genai.types.Type.ARRAY,
                    items = genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["section_name", "container_settings", "elements_to_add"],
                        properties = {
                            "section_name": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "container_settings": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "elements_to_add": genai.types.Schema(
                                type = genai.types.Type.ARRAY,
                                items = genai.types.Schema(
                                    type = genai.types.Type.STRING,
                                ),
                            ),
                        },
                    ),
                ),
                "copy": genai.types.Schema(
                    type = genai.types.Type.OBJECT,
                    required = ["hero_h1", "hero_subheadline", "primary_cta", "feature_bullets"],
                    properties = {
                        "hero_h1": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "hero_subheadline": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "primary_cta": genai.types.Schema(
                            type = genai.types.Type.STRING,
                        ),
                        "feature_bullets": genai.types.Schema(
                            type = genai.types.Type.ARRAY,
                            items = genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                        ),
                    },
                ),
                "code": genai.types.Schema(
                    type = genai.types.Type.ARRAY,
                    items = genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        required = ["plugin_name", "instructions", "code_snippet"],
                        properties = {
                            "plugin_name": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "instructions": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                            "code_snippet": genai.types.Schema(
                                type = genai.types.Type.STRING,
                            ),
                        },
                    ),
                ),
            },
        ),
        system_instruction=[
            types.Part.from_text(text="""You are an expert Carrd Template Architect. Base your answers strictly on the provided documentation. Output your response in strict JSON format with four keys: 'design', 'structure', 'copy', and 'code'.\""""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()


